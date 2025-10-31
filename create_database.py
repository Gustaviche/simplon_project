#!/usr/bin/env python3
import sqlite3

# Connexion à la base (sera créée si absente)
conn = sqlite3.connect("./data/db.sqlite3")
cur = conn.cursor()

# Activer les clés étrangères
cur.execute("PRAGMA foreign_keys = ON;")

# Création des tables adaptées aux CSV actuels
cur.executescript("""
CREATE TABLE IF NOT EXISTS produits (
    id_reference_produit TEXT PRIMARY KEY,
    nom TEXT NOT NULL,
    prix REAL,
    stock INTEGER
);

CREATE TABLE IF NOT EXISTS magasins (
    id_magasin TEXT PRIMARY KEY,
    ville TEXT,
    nombre_de_salaries INTEGER
);

CREATE TABLE IF NOT EXISTS ventes (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    id_reference_produit TEXT NOT NULL,
    quantite INTEGER NOT NULL,
    id_magasin TEXT NOT NULL,
    FOREIGN KEY (id_reference_produit) REFERENCES produits(id_reference_produit),
    FOREIGN KEY (id_magasin) REFERENCES magasins(id_magasin)
);
""")

conn.commit()
conn.close()

print("✅ Base SQLite créée : /data/sales.db")
print("📦 Tables : produits (id_reference_produit, nom, prix, stock), magasins (id_magasin, ville, nombre_de_salaries), ventes (date, id_reference_produit, quantite, id_magasin)")
