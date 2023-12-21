import  os
import string
def convertir_texte_en_minuscules(fichiers_sources, dossier_destination):

    # Convertit les textes des fichiers sources en minuscules et les stocke dans des nouveaux fichiers dans le dossier de destination.

    # Récupérer le chemin absolu du dossier "speeches"
    speeches_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "speeches")

    # Créer le dossier de destination s'il n'existe pas
    chemin_dossier_destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), dossier_destination)
    if not os.path.exists(chemin_dossier_destination):
        os.mkdir(chemin_dossier_destination)

    # Parcourir les fichiers sources
    for fichier_source in fichiers_sources:

        # Construire le chemin complet du fichier source
        chemin_complet_source = os.path.join(speeches_directory, fichier_source)


        #TO DO:
        # Remplacer ci dessous par une fonction nommée "OpenAndGetFileContent(FilePath)"
        # placée dans files_manager et qui renverra une string contenant l'intégralité du fichier
        # Lire le contenu du fichier
        with open(chemin_complet_source, "r", encoding="utf-8") as f:
            text = f.read()

        # Convertir le texte en minuscules
        text_minuscule = text.lower()

        # Construire le chemin complet du fichier de destination
        chemin_complet_destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), dossier_destination, fichier_source)

        # Écrire le texte en minuscules dans le fichier de destination
        with open(chemin_complet_destination, "w", encoding="utf-8") as f:
            f.write(text_minuscule)

        print("Les textes ont été convertis en minuscules et stockés dans le dossier 'cleaned'.")
def nettoyer_texte(dossier_fichiers):
    #Nettoie les textes des fichiers dans le dossier source en supprimant la ponctuation.
    #Les fichiers modifiés sont stockés dans le dossier de destination.

    # Récupérer le chemin absolu du dossier source
    chemin_dossier_source = os.path.join(os.path.dirname(os.path.abspath(__file__)), dossier_fichiers)

    # Créer le dossier de destination s'il n'existe pas
    chemin_dossier_destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), dossier_fichiers)
    if not os.path.exists(chemin_dossier_destination):
        os.mkdir(chemin_dossier_destination)

    # Liste des caractères spéciaux à traiter
    caracteres_speciaux = {"'": " ", "-": " "}

    # Parcourir les fichiers dans le dossier source
    for fichier in os.listdir(chemin_dossier_source):
        chemin_complet_source = os.path.join(chemin_dossier_source, fichier)

        # Lire le contenu du fichier
        with open(chemin_complet_source, "r", encoding="utf-8") as f:
            texte = f.read()

        # Supprimer la ponctuation tout en conservant les espaces
        texte_nettoye = "".join(c if c not in string.punctuation else " " for c in texte)

        # Traiter les caractères spéciaux
        for caractere, remplacement in caracteres_speciaux.items():
            texte_nettoye = texte_nettoye.replace(caractere, remplacement)

        # Construire le chemin complet du fichier de destination
        chemin_complet_destination = os.path.join(chemin_dossier_destination, fichier)

        # Écrire le texte nettoyé dans le fichier de destination
        with open(chemin_complet_destination, "w", encoding="utf-8") as f:
            f.write(texte_nettoye)

    print("Les textes ont été nettoyés et stockés dans le dossier 'cleaned'.")
def transformer_texte_en_liste(texte):
    liste_mots = texte.split()
    return  liste_mots
def compter_occurrences_mot(mot, texte):
    count = texte.count(mot)
    return count
def convertir_texte_en_liste_de_mots():
    # to do...
    return

def charger_contenu_fichier(chemin_fichier, extension = ".txt"):
    with open(os.path.join(chemin_fichier, extension), 'r', encoding='utf-8') as file:
        texte = file.read()
        return texte

#def ouvrir_et_charger_contenu_des_fichiers_du_dossier(chemin_dossier_fichiers, extension = ".txt"):
#    for filename in os.listdir(chemin_dossier_fichiers):
#        if filename.endswith(extension):
#            with open(os.path.join(chemin_dossier_fichiers, filename), 'r', encoding='utf-8') as file:
#                texte = file.read()






