import sqlite3
import pandas as pd
import os

# Chemin vers votre fichier CSV
csv_file_path = "/home/yanis/Téléchargements/Projet chef d'oeuvre/bank-additional-full.csv"

# Lire votre fichier CSV avec pandas
# Spécifier le séparateur et ignorer les espaces initiaux après le séparateur
df = pd.read_csv(csv_file_path, sep=';', quotechar='"', skipinitialspace=True)
#print(df.head())

# Chemin vers votre fichier de base de données SQLite
sqlite_db_path = "/home/yanis/Téléchargements/Projet chef d'oeuvre/bdd/base_de_donnees.db"

# S'assurer que le répertoire existe
directory = os.path.dirname(sqlite_db_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Créer une connexion à la base de données SQLite
conn = sqlite3.connect(sqlite_db_path)

# Nom de la table dans la base de données SQLite
table_name = "customer_data"

# Écrire les données dans la base de données SQLite
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Fermer la connexion
conn.close()


