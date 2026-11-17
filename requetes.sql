-- 1. Afficher toutes les ventes.
SELECT * FROM ventes;

-- 2. Vérifier le nombre de lignes et la période.
SELECT
    COUNT(*) AS nombre_lignes,
    MIN(date) AS date_debut,
    MAX(date) AS date_fin
FROM ventes;

-- 3. Calculer le chiffre d'affaires total.
SELECT
    SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;

-- 4. Calculer les quantités et le chiffre d'affaires par produit.
SELECT
    produit,
    SUM(qte) AS quantite_vendue,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires DESC;

-- 5. Calculer les quantités et le chiffre d'affaires par région.
SELECT
    region,
    SUM(qte) AS quantite_vendue,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY region
ORDER BY chiffre_affaires DESC;