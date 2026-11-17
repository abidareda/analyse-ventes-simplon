# Analyse des ventes d’une PME

## Périmètre et méthode

L’extrait fourni contient 39 lignes de ventes du 1er au 20 janvier 2022, trois produits et deux régions. Une ligne contient une date, un produit, un prix unitaire, une quantité et une région. Elle ne permet pas d’identifier une commande ou un client : 39 lignes ne signifie donc pas nécessairement 39 commandes.

Contrôles réalisés : colonnes attendues, absence de valeurs manquantes, dates valides, prix et quantités numériques non négatifs, quantités entières, absence de doublons exacts. Les données ont été agrégées avec SQL et pandas ; les résultats concordent.

Le chiffre d’affaires d’une ligne est `prix × qte`. Le chiffre d’affaires total est la somme de ces montants. La devise et le traitement des taxes ne sont pas indiqués : les montants sont exprimés en unités monétaires, sans hypothèse HT/TTC.

## Résultats

**Chiffre d’affaires total : 44 825 unités monétaires. Quantité totale : 3 380 unités.**

| Produit | Quantité vendue | Chiffre d’affaires | Part du CA |
|---|---:|---:|---:|
| Produit A | 1 750 | 17 500 | 39,04 % |
| Produit B | 1 055 | 15 825 | 35,30 % |
| Produit C | 575 | 11 500 | 25,66 % |
| **Total** | **3 380** | **44 825** | **100 %** |

| Région | Quantité vendue | Chiffre d’affaires | Part du CA |
|---|---:|---:|---:|
| Nord | 1 605 | 20 725 | 46,24 % |
| Sud | 1 775 | 24 100 | 53,76 % |
| **Total** | **3 380** | **44 825** | **100 %** |

## Interprétation

- Le produit A arrive en tête en volume et en chiffre d’affaires. Il représente 51,78 % des unités, mais 39,04 % du chiffre d’affaires, car son prix unitaire (10) est plus faible que celui de B (15) et C (20).
- Le produit C représente 17,01 % des unités et 25,66 % du chiffre d’affaires. Un faible volume ne signifie donc pas une faible contribution monétaire proportionnelle.
- Le Sud génère 3 375 unités monétaires de plus que le Nord, soit 16,28 % de plus par rapport au Nord. Cet écart décrit l’extrait ; il ne prouve pas une meilleure efficacité commerciale.

## Pistes de décision et limites

Vérifier les stocks et ruptures du produit A pourrait aider à préserver les ventes du produit le plus demandé dans cet extrait. Examiner les marges par produit est nécessaire avant de privilégier A, B ou C : chiffre d’affaires et bénéfice sont différents. Pour comprendre l’écart régional, il faudrait connaître les clients, points de vente, promotions et stocks disponibles.

L’historique de 20 jours est trop court pour conclure à une saisonnalité ou à une tendance durable. Les coûts, remises, retours, taxes et données clients ne sont pas renseignés. Aucune conclusion de rentabilité ni prévision annuelle n’est donc formulée.

## Graphiques

- `resultats/ventes-par-region.html` : répartition des quantités par région, reprise de l’objectif du modèle.
- `resultats/ventes-par-produit.html` : comparaison des quantités par produit.
- `resultats/chiffre-affaires-par-produit.html` : comparaison des montants par produit.

Les histogrammes facilitent la comparaison des trois produits ; l’origine de l’axe vertical est zéro. Les fichiers HTML sont consultables hors ligne après téléchargement.
