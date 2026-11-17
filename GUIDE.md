# Comprendre et finaliser le mini-projet

## 1. Comprendre une ligne

`2022-01-01,Produit A,10,100,Nord` signifie : le 1er janvier, 100 unités du produit A ont été vendues dans le Nord à un prix unitaire de 10. Le chiffre d’affaires associé est `10 × 100 = 1 000`. Le prix n’est pas le montant total ; la quantité n’est pas le nombre de lignes.

Avant de poursuivre, retrouve manuellement le montant d’une ligne du produit B puis du produit C. Compare avec le calcul Python.

## 2. Réaliser l’étape SQL demandée

1. Ouvre https://sqliteonline.com/ et sélectionne SQLite.
2. Utilise l’import de fichier CSV proposé par l’interface. Choisis `ventes.csv`, la virgule comme séparateur et la première ligne comme noms de colonnes.
3. Nomme la table `ventes`. Vérifie que `prix` et `qte` sont numériques et que les cinq colonnes sont bien séparées.
4. Exécute `SELECT * FROM ventes;`. Tu dois retrouver 39 lignes, pas une seule colonne de texte.
5. Copie les requêtes de `requetes.sql` et exécute-les successivement. Confronte les résultats à `SYNTHESE.md`.
6. Exporte ton travail avec le menu **File > Save SQL**, comme demandé dans le brief. Conserve cet export dans ton dépôt. Le fichier fourni contient déjà les requêtes, mais n’est pas un export fait par toi depuis cette interface.

Si l’interface diffère, cherche les fonctions Import et Save SQL ; ne modifie pas les données pour faire correspondre artificiellement un résultat.

### Décomposer la requête par produit

```sql
SELECT produit, SUM(qte) AS quantite_vendue,
       SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires DESC;
```

- `SELECT` choisit ce que la requête retourne.
- `FROM ventes` indique la table source.
- `SUM(qte)` additionne les unités, contrairement à `COUNT(*)`, qui compte les lignes.
- `SUM(prix * qte)` calcule chaque montant puis les additionne.
- `AS` donne un nom lisible au résultat.
- `GROUP BY produit` rassemble les lignes de chaque produit avant de les additionner.
- `ORDER BY ... DESC` trie du plus grand montant au plus petit.

Évite `SUM(prix) * SUM(qte)` : cette expression multiplie des totaux qui ne correspondent plus aux ventes individuelles. Pour obtenir les ventes par région, remplace la clé de regroupement `produit` par `region`.

## 3. Comprendre le programme Python

Lis `app.py` dans l’ordre, puis exécute-le.

1. `Path(__file__).resolve().parent` retrouve le dossier du programme. Ainsi, le CSV reste accessible même si le terminal est ouvert ailleurs.
2. `pd.read_csv(...)` charge le CSV dans un **DataFrame**, un tableau pandas.
3. Les contrôles arrêtent le programme si une donnée essentielle manque ou si une quantité est incorrecte. Un doublon exact est signalé, pas automatiquement supprimé : il peut parfois correspondre à une vente réelle répétée.
4. `pd.to_datetime` vérifie les dates ; `pd.to_numeric` vérifie les nombres.
5. `ventes['chiffre_affaires'] = ventes['prix'] * ventes['qte']` ajoute une colonne calculée ligne par ligne.
6. `groupby(...).agg(...)` regroupe par produit ou région et calcule deux sommes. C’est l’équivalent de `GROUP BY` avec `SUM` en SQL.
7. `sqlite3.connect(':memory:')` crée une base temporaire pour comparer les calculs SQL et pandas. Cela ne remplace pas l’exercice sur SQLiteOnline demandé par Simplon.
8. `px.pie` crée le diagramme régional fourni dans l’esprit du modèle. `px.bar` crée les deux histogrammes demandés. `x`, `y` et `text` désignent les colonnes utilisées.
9. `write_html` enregistre un graphique interactif. Le JavaScript est inclus afin de pouvoir le lire hors ligne ; cela explique la taille des fichiers.
10. `to_csv(..., index=False)` exporte les tableaux sans ajouter de colonne d’index inutile.

Le petit bloc de vérification SQL/pandas est un complément pour contrôler la cohérence. Si une assertion échoue, il faut comprendre l’écart avant de modifier ou retirer le contrôle.

### Exercices pour t’approprier le code

- Explique pourquoi A domine en quantité, mais pèse moins dans le CA que dans les volumes.
- Ajoute temporairement `print(ventes.head())`, exécute et observe les premières lignes.
- Change un titre de graphique puis relance : constate que le HTML est régénéré.
- Explique à voix haute le passage d’une ligne brute à un total par produit.

## 4. Préparer ton dépôt GitHub

Dans le dépôt modèle Simplon, crée ton propre dépôt avec **Use this template / Utiliser ce modèle**. Conserve ses fichiers de configuration (notamment ceux de Codespaces). Ouvre ensuite ton Codespace si tu utilises cette méthode.

Décompresse ce dossier, puis copie son contenu à la racine de ton dépôt : `app.py` remplace le programme initial, le README est actualisé, les autres fichiers sont ajoutés. Ne téléverse pas seulement l’archive ZIP : le jury doit pouvoir consulter les fichiers.

Exécute les commandes de démarrage du README. Après avoir relu et compris le contenu, réalise un commit via le panneau de contrôle de source. Si tu utilises le terminal :

```bash
git status
git add app.py requirements.txt ventes.csv requetes.sql README.md SYNTHESE.md GUIDE.md resultats
git commit -m "Ajouter l'analyse des ventes et les graphiques"
git push
```

Ajoute également ton export SQLiteOnline s’il porte un autre nom. Vérifie le dépôt sur GitHub après publication. Le lien doit être accessible au jury : vérifie en navigation privée s’il est public, ou organise l’accès si tu choisis un dépôt privé.

## 5. Préparer une présentation de 3 à 5 minutes

- **Contexte** : expliquer une analyse exploratoire de 20 jours de ventes.
- **Données** : présenter les cinq colonnes et les contrôles de qualité.
- **Méthode** : montrer une requête SQL et expliquer prix × quantité.
- **Résultats** : donner le CA total, le produit dominant et la comparaison régionale.
- **Limites** : distinguer CA et bénéfice ; rappeler le faible historique et l’absence de coûts.

Entraîne-toi à répondre sans lire : pourquoi SUM et pas COUNT ? Pourquoi des histogrammes ? Pourquoi ne pas annoncer une rentabilité supérieure au Sud ? Comment vérifier qu’un graphique correspond aux données ? Quelle aide as-tu utilisée et qu’as-tu personnellement exécuté ou modifié ?

## 6. Finaliser l’envoi

Le mail reçu demande un lien Git envoyé à **lfiacre@simplon.co** et **lplinet@simplon.co**. Il ne donne pas de date limite explicite ; « dans les prochains jours » décrit leur retour, pas une échéance de remise.

Avant d’envoyer : exécuter le projet, ouvrir les trois HTML, relire la synthèse, réaliser l’import/export SQL, vérifier l’accès au dépôt et compléter les exercices d’auto-apprentissage demandés. Aucune de ces étapes personnelles n’est présumée réalisée par la préparation du dossier.

Brouillon à adapter après publication :

Objet : Mini-projet de candidature Développeur IA — Reda Abida

Bonjour,

À la suite de votre message, je vous transmets le lien vers mon dépôt GitHub pour le mini-projet « Analyser les ventes d’une PME » :

[INSÉRER LE LIEN DE TON DÉPÔT]

Le dépôt contient les requêtes SQL, la synthèse des résultats et le programme Python avec les graphiques demandés.

Je reste disponible pour présenter ma démarche et répondre à vos questions.

Bien cordialement,
Reda Abida
