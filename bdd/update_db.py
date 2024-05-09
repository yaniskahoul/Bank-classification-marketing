import sqlite3

# Chemin vers votre fichier de base de données SQLite
sqlite_db_path = "/home/yanis/Téléchargements/Projet chef d'oeuvre/bdd/base_de_donnees.db"

# Créer une connexion à la base de données SQLite
conn = sqlite3.connect(sqlite_db_path)

# Créer une connexion à la base de données SQLite
cur = conn.cursor()

# Supprimer les enregistrements où 'y' est NULL (équivalent de NaN en Pandas)
cur.execute("DELETE FROM customer_data WHERE y IS NULL")

# Supprimer les enregistrements où 'marital' est 'unknown'
cur.execute("DELETE FROM customer_data WHERE marital = 'unknown'")

# Remplacer les valeurs dans 'education'
cur.execute("""
UPDATE customer_data
SET education = 'basic.education'
WHERE education IN ('basic.4y', 'basic.6y', 'basic.9y')
""")

cur.execute("ALTER TABLE customer_data ADD COLUMN age_group TEXT")

cur.execute("""
UPDATE customer_data
SET age_group = CASE
    WHEN age BETWEEN 17 AND 33 THEN 'Group 1'
    WHEN age BETWEEN 34 AND 50 THEN 'Group 2'
    WHEN age BETWEEN 51 AND 67 THEN 'Group 3'
    WHEN age BETWEEN 68 AND 84 THEN 'Group 4'
    WHEN age BETWEEN 85 AND 101 THEN 'Group 5'
    ELSE 'Other'
END
""")

cur.execute("""
CREATE TABLE filtered_data AS
SELECT 
    y, marital, education, defaut, housing, loan, age_group, 
    duration, campaign, pdays, previous, cons_price_idx, cons_conf_idx
FROM customer_data
""")

# Valider les changements
conn.commit()

# Fermer la connexion
conn.close()