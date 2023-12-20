from files_manager import *
from presidents import *
import string_manager as sm

###############################################################################
# Zone de debug temp


# Fin zone de debug temp
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
dossier_cleaned = "cleaned"

sm.convertir_texte_en_minuscules(fichiers_discours_presidents, dossier_cleaned)
sm.nettoyer_texte(dossier_cleaned)
