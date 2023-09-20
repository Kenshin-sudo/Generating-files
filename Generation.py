import pandas as pd
import random
from openpyxl import Workbook

# Nombre de fichiers Excel à générer
nombre_fichiers = 5

# Nombre de lignes et de colonnes aléatoires pour chaque fichier
nombre_lignes = random.randint(5, 10)
nombre_colonnes = random.randint(2, 5)

# Génération des fichiers Excel
for i in range(nombre_fichiers):
    # Créez un DataFrame de données aléatoires
    donnees = [[random.randint(1, 100) for _ in range(nombre_colonnes)] for _ in range(nombre_lignes)]
    df = pd.DataFrame(donnees, columns=[f"Colonne_{j+1}" for j in range(nombre_colonnes)])

    # Créez un nouveau classeur Excel et ajoutez le DataFrame
    classeur = Workbook()
    feuille = classeur.active
    for row in df.iterrows():
        _, row_data = row
        feuille.append(list(row_data))

    # Enregistrez le classeur Excel dans un fichier
    nom_fichier = f"fichier_{i+1}.xlsx"
    classeur.save(nom_fichier)
    print(f"Fichier Excel {nom_fichier} généré avec succès.")

print(f"{nombre_fichiers} fichiers Excel aléatoires ont été générés.")
