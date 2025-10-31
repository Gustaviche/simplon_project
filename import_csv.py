import sqlite3
import pandas as pd
import requests
from io import StringIO

# Connexion à la base SQLite
conn = sqlite3.connect('/data/db.sqlite3')

# Dictionnaire : table → URL CSV
csv_files = {
    "produits": "https://raw.githubusercontent.com/Gustaviche/simplon_project/refs/heads/main/produits.csv",
    "magasins": "https://raw.githubusercontent.com/Gustaviche/simplon_project/refs/heads/main/magasins.csv",
    "ventes": "https://raw.githubusercontent.com/Gustaviche/simplon_project/refs/heads/main/ventes.csv"
}

def clean_columns(df):
    """Clean column names in place and return the DataFrame"""
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.normalize('NFKD')
                  .str.encode('ascii', errors='ignore')
                  .str.decode('utf-8')
    )
    return df

for table, url in csv_files.items():
    print(f"Import du fichier CSV dans la table {table} ...")
    
    # Télécharger le CSV
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    
    # Clean columns
    df = clean_columns(df)
    
    print(f"Colonnes: {df.columns.tolist()}")
    
    # Insérer dans la table (replace pour éviter les conflits)
    df.to_sql(table, conn, if_exists='replace', index=False)
    print(f"{len(df)} lignes ajoutées à {table} ✅\n")

# Fermer la connexion
conn.close()
print("Import terminé pour tous les fichiers ! 🎉")