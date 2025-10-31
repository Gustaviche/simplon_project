import sqlite3
import pandas as pd

# Connexion à la base SQLite
conn = sqlite3.connect('/data/db.sqlite3')

# Chiffre d'affaires total
query_total_ca = """
SELECT SUM(v.quantite * p.prix) AS chiffre_affaires_total
FROM ventes v
JOIN produits p ON v.id_reference_produit = p.id_reference_produit
"""
total_ca = pd.read_sql(query_total_ca, conn)
print("💰 Chiffre d'affaires total :")
print(total_ca, "\n")

# Ventes par produit
query_ventes_produit = """
SELECT p.nom AS produit, SUM(v.quantite) AS total_ventes,
       SUM(v.quantite * p.prix) AS ca_produit
FROM ventes v
JOIN produits p ON v.id_reference_produit = p.id_reference_produit
GROUP BY p.nom
ORDER BY ca_produit DESC
"""
ventes_produit = pd.read_sql(query_ventes_produit, conn)
print("📦 Ventes par produit :")
print(ventes_produit, "\n")

# Ventes par ville
query_ventes_ville = """
SELECT m.ville AS ville, SUM(v.quantite) AS total_ventes,
       SUM(v.quantite * p.prix) AS ca_region
FROM ventes v
JOIN produits p ON v.id_reference_produit = p.id_reference_produit
JOIN magasins m ON v.id_magasin = m.id_magasin
GROUP BY m.ville
ORDER BY ca_region DESC
"""
ventes_region = pd.read_sql(query_ventes_ville, conn)
print("🌍 Ventes par ville :")
print(ventes_region, "\n")

# Fermer la connexion
conn.close()
