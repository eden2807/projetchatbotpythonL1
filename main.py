
from functions import *

# 1. Extraire les noms des présidents à partir des noms des fichiers texte fournis
directory = "./speeches"
files_list = list_of_files(directory, ".txt")
print("Liste des fichiers :", files_list)
print()

# 2. Associer à chaque président un prénom
fichiers = [
    "Nomination_Chirac1.txt",
    "Nomination_Chirac2.txt",
    "Nomination_Giscard dEstaing.txt",
    "Nomination_Hollande.txt",
    "Nomination_Macron.txt",
    "Nomination_Mitterrand1.txt",
    "Nomination_Mitterrand2.txt",
    "Nomination_Sarkozy.txt"
]

for fichier in fichiers:
    nom_president = extraire_nom_president(fichier)
    print(f"Nom du président dans '{fichier}': {nom_president}")

# 3. Afficher la liste des noms des présidents (attention aux doublons)
noms_presidents = [
    "Chirac",
    "Giscard dEstaing",
    "Hollande",
    "Macron",
    "Mitterrand",
    "Sarkozy"
]

# Créer la liste des prénoms et noms de famille formatés
liste_prenom_nom_presidents = creer_liste_prenom_nom_formattee(noms_presidents)

# Afficher la liste résultante
print("Liste des noms des présidents (formatée) :")
for nom_formatte in liste_prenom_nom_presidents:
    print(nom_formatte)

# 4. Convertir les fichiers en minuscules et les stocker dans le dossier "cleaned"
convertir_textes_en_minuscules(fichiers, "cleaned")
