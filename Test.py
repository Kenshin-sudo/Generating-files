import os
import pandas as pd

# Chemin du Test contenant les fichiers Excel
Test = "C:\\Users\HP\\Downloads\\Excel"

# Récupérez la liste des fichiers Excel dans le Test
fichiers_excel = [fichier for fichier in os.listdir(Test) if fichier.endswith(".xlsx")]

# Créez un DataFrame vide pour stocker les données fusionnées
donnees_fusionnees = pd.DataFrame()

# Parcourez chaque fichier Excel du Test et ajoutez ses données au DataFrame fusionné
for fichier in fichiers_excel:
    try:
        chemin_fichier = os.path.join(Test, fichier)
        df = pd.read_excel(chemin_fichier)
        donnees_fusionnees = donnees_fusionnees.append(df, ignore_index=True)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier}: {e}")

# Nom du fichier de sortie fusionné
fichier_fusionne = "fichier_fusionne.xlsx"

# Écrivez le DataFrame fusionné dans un nouveau fichier Excel
donnees_fusionnees.to_excel(fichier_fusionne, index=False)

print(f"Les fichiers Excel du Test ont été fusionnés avec succès dans {fichier_fusionne}")
