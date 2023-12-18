from FilesManager import *
from Presidents import *
from StringManager import *
from TF_IDF import obtenir_dico_occurences_mots

###############################################################################
# Zone de debug temp
#
###############################################################################

Texte = "Bonjour je suis un exemple je vais servir exemple à proprement parler"
dico_occurences_mots = {}
dico_occurences_mots = obtenir_dico_occurences_mots(Texte)

################################################################################

# Extraire les noms des présidents à partir des noms des fichiers texte fournis
noms_des_presidents = [] # = FilesManager.GetListOfFiles(filesPath, filesExtension)
dossier_discours_presidents = "./speeches"

fichiers_discours_presidents = list_of_files(dossier_discours_presidents, ".txt")

# A deplacer dans le fichier "Presidents"
# To Do de DE:
for fichier in fichiers_discours_presidents:
    nom_president = extraire_nom_president(fichier)
    noms_des_presidents.append(nom_president)

# Créer la liste des prénoms et noms de famille formatés
prenom_nom_des_presidents = creer_liste_prenom_nom_formates(noms_des_presidents)

# 4. Convertir les fichiers en minuscules et les stocker dans le dossier "cleaned"
# To Do de DE:
#Declarer en tant que constante
dossier_cleaned = "cleaned"
# To Do de DE:
# changer code en dur ci-dessous. A quoi sert de déclarer une constante si on utilise un code en dur ?!?
ConvertirTextesEnMinuscules(fichiers_discours_presidents, dossier_cleaned)
NettoyerTextes(dossier_cleaned)


