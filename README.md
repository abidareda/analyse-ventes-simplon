# Analyse des ventes d’une PME — SQL et Python

Projet pédagogique construit à partir du [modèle fourni par Simplon](https://github.com/paufabregat/projet-devia-data-analyst-simplon). Il calcule les ventes avec SQL et Python puis génère des graphiques Plotly.

## Démarrage

Dans un terminal ouvert dans le dossier du projet :

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

Versions utilisées pour la vérification : pandas 2.2.3 et Plotly 7.1.0. Les résultats sont générés dans `resultats/`. Le fichier CSV local est utilisé au lieu de la source distante du modèle afin de travailler sur l’extrait fourni, même sans accès à Google Sheets.

Télécharger puis ouvrir les fichiers HTML dans un navigateur pour consulter les graphiques. GitHub affiche habituellement le code HTML, pas le graphique interactif directement. Dans le Codespace du modèle, utiliser la prévisualisation prévue par son environnement.

## Fichiers

| Fichier | Rôle |
|---|---|
| `ventes.csv` | Données originales, inchangées |
| `requetes.sql` | Requêtes à exécuter sur la table `ventes` |
| `app.py` | Contrôles, agrégations et graphiques |
| `requirements.txt` | Dépendances Python |
| `SYNTHESE.md` | Résultats, interprétations et limites |
| `GUIDE.md` | Explications et étapes à réaliser personnellement |
| `resultats/` | Graphiques HTML et tableaux de résultats CSV |

## Résultats de référence

39 lignes ; 3 380 unités vendues ; chiffre d’affaires total de 44 825 unités monétaires. Aucune devise n’est spécifiée dans les données. Les agrégations par produit et région ont été comparées entre SQLite et pandas avec succès.

## État de réalisation

Le programme et les requêtes ont été vérifiés localement. L’import dans SQLiteOnline et l’export via son menu restent à réaliser par le candidat. La publication sur son dépôt GitHub et l’envoi du lien sont également à effectuer.

Ce dossier est une base accompagnée préparée avec une assistance IA. Le candidat doit comprendre, exécuter et adapter les éléments avant de les présenter ; les consignes de Simplon demandent un travail personnel. Ne pas présenter les étapes non réalisées comme acquises.
