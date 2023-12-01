from functions import *

directory = "./speeches"
files_list = list_of_files(directory, ".txt")
print(files_list)
print()

fichiers = [
    "Nomination_Chirac1.txt",
    "Nomination_Chirac2.txt",
    "Nomination_Giscard dEstaing.txt",
    "Nomination_Hollande.txt",
    "Nomination_Macron(1).txt",
    "Nomination_Mitterrand1.txt",
    "Nomination_Mitterrand2.txt",
    "Nomination_Sarkozy(1).txt"
]

for fichier in fichiers:
    nom_president = extraire_nom_president(fichier)
    print(f"Nom du président dans '{fichier}': {nom_president}")

noms_presidents = [
    "Chirac",
    "Giscard dEstaing",
    "Hollande",
    "Macron",
    "Mitterrand",
    "Sarkozy"
]

for nom_president in noms_presidents:
    prenom = associer_prenom_a_president(nom_president)
    print(f"Prénom associé à {nom_president}: {prenom}")

noms_presidents = [
    "Chirac",
    "Giscard dEstaing",
    "Hollande",
    "Macron",
    "Mitterrand",
    "Sarkozy"
]

liste_prenom_nom_presidents = creer_liste_prenom_nom_presidents(noms_presidents)

# Afficher la liste résultante
for prenom, nom in liste_prenom_nom_presidents:
    print(f"Prénom: {prenom}, Nom: {nom}")

noms_presidents = [
    "Chirac",
    "Giscard dEstaing",
    "Hollande",
    "Macron",
    "Mitterrand",
    "Sarkozy"
]

liste_prenom_nom_formattee = creer_liste_prenom_nom_formattee(noms_presidents)

# Afficher la liste résultante
print(liste_prenom_nom_formattee)