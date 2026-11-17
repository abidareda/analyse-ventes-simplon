"""Analyse reproductible du CSV fourni et création des trois graphiques."""
from pathlib import Path
import sqlite3
import pandas as pd
import plotly.express as px

# Un chemin relatif à ce fichier fonctionne quel que soit le dossier du terminal.
DOSSIER = Path(__file__).resolve().parent
SORTIE = DOSSIER / 'resultats'
SORTIE.mkdir(exist_ok=True)
ventes = pd.read_csv(DOSSIER / 'ventes.csv')

# Contrôles explicites : ne pas supprimer silencieusement une ligne suspecte.
colonnes = ['date', 'produit', 'prix', 'qte', 'region']
if list(ventes.columns) != colonnes or ventes.empty:
    raise ValueError('Structure du CSV incorrecte ou fichier vide.')
if ventes.isna().any().any():
    raise ValueError('Le fichier contient des valeurs manquantes.')
ventes['date'] = pd.to_datetime(ventes['date'], format='%Y-%m-%d', errors='raise')
for colonne in ['prix', 'qte']:
    ventes[colonne] = pd.to_numeric(ventes[colonne], errors='raise')
    if (ventes[colonne] < 0).any():
        raise ValueError(f'Valeurs négatives dans {colonne}.')
if (ventes['qte'] % 1 != 0).any():
    raise ValueError('Les quantités doivent être entières.')
print(f'{len(ventes)} lignes ; {ventes.duplicated().sum()} doublon(s) exact(s).')

# Calcul au niveau de chaque ligne, AVANT de regrouper.
ventes['chiffre_affaires'] = ventes['prix'] * ventes['qte']
produits = ventes.groupby('produit', as_index=False).agg(
    quantite_vendue=('qte', 'sum'), chiffre_affaires=('chiffre_affaires', 'sum'))
regions = ventes.groupby('region', as_index=False).agg(
    quantite_vendue=('qte', 'sum'), chiffre_affaires=('chiffre_affaires', 'sum'))

# Vérification indépendante : SQL et pandas doivent donner les mêmes résultats.
with sqlite3.connect(':memory:') as connexion:
    ventes[colonnes].to_sql('ventes', connexion, index=False)
    total_sql = connexion.execute('SELECT SUM(prix*qte) FROM ventes').fetchone()[0]
    assert total_sql == ventes['chiffre_affaires'].sum()
    for cle, tableau in [('produit', produits), ('region', regions)]:
        sql = pd.read_sql_query(
            f'SELECT {cle}, SUM(qte) AS quantite_vendue, '
            f'SUM(prix*qte) AS chiffre_affaires FROM ventes GROUP BY {cle} ORDER BY {cle}',
            connexion)
        pd.testing.assert_frame_equal(sql, tableau.sort_values(cle).reset_index(drop=True), check_dtype=False)

# Même graphique régional que le modèle, sur des quantités agrégées.
figures = {
    'ventes-par-region.html': px.pie(regions, values='quantite_vendue', names='region',
        title='Quantités vendues par région'),
    'ventes-par-produit.html': px.bar(produits, x='produit', y='quantite_vendue',
        text='quantite_vendue', title='Quantités vendues par produit',
        labels={'produit': 'Produit', 'quantite_vendue': 'Quantité vendue (unités)'}),
    'chiffre-affaires-par-produit.html': px.bar(produits, x='produit', y='chiffre_affaires',
        text='chiffre_affaires', title="Chiffre d’affaires par produit",
        labels={'produit': 'Produit', 'chiffre_affaires': 'Chiffre d’affaires (unité monétaire non précisée)'})}
for nom, figure in figures.items():
    figure.update_layout(template='plotly_white', font=dict(family='Arial', size=15),
        title=dict(subtitle=dict(text='Extrait du 1er au 20 janvier 2022')))
    # JavaScript embarqué : consultation hors ligne sans dépendance à un CDN.
    figure.write_html(SORTIE / nom, include_plotlyjs=True, full_html=True)
    print(f'Graphique généré : resultats/{nom}')
produits.to_csv(SORTIE / 'ventes_par_produit.csv', index=False)
regions.to_csv(SORTIE / 'ventes_par_region.csv', index=False)
print(f"Chiffre d'affaires total : {total_sql:,.0f}")
print(produits.to_string(index=False))
print(regions.to_string(index=False))
print('Vérification SQL / pandas : réussie.')
