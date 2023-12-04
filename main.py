
from functions import *

# Extraire les noms des présidents à partir des noms des fichiers texte fournis
noms_presidents = []
directory = "./Speeches"
fichiers = list_of_files(directory, ".txt")
# Debug uniquement, penser à supprimer
print("Liste des fichiers :", fichiers)
print()

# Extraire le nom de chaque président
for fichier in fichiers:
    nom_president = extraire_nom_president(fichier)
    noms_presidents.append(nom_president)
    print(f"Nom du président dans '{fichier}': {nom_president}")

# Créer la liste des prénoms et noms de famille formatés
liste_prenom_nom_presidents = creer_liste_prenom_nom_formates(noms_presidents)

# 4. Convertir les fichiers en minuscules et les stocker dans le dossier "cleaned"
dossier_cleaned = "cleaned"
convertir_textes_en_minuscules(fichiers, "cleaned")
nettoyer_textes(dossier_cleaned, dossier_cleaned)
