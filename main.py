from FilesManager import *
from Presidents import *
from StringManager import *
from TF_IDF import CompterOccurenceMots

###############################################################################
# Zone de debug temp

# A faire:
# 1) Trouver comment la fonction split trie les mots par défaut (Random ?, autre ?...)
#Réponse : J'ai enlevé set, il n'était pas trés utile. Pour avoir une liste des mots dans l'ordre du texte, il suffit de laisser .split
#set fait cela de manière aléatoire
# 2) Trouver comment specifier son propre ordre (Ordre des mots dans la cgaine, ordre alpha-numérique, etc.)
#Pour pas mal d'ordre voulu, il faut crée soit même sa condition (la codé) mais il existe une autre fonction pour trier rapidement par ordre alphabétique par exemple qui se nomme .sorted
#Pour le moment, .split semble nous suffir



document = "Bonjour je suis un exemple je vais servir d'exemple à proprement parler"

mots = CompterOccurenceMots(document)

################################################################################

# Extraire les noms des présidents à partir des noms des fichiers texte fournis
noms_presidents = []
directory = "./speeches"
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
ConvertirTextesEnMinuscules(fichiers, "cleaned")
NettoyerTextes(dossier_cleaned, dossier_cleaned)