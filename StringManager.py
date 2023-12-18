import  os
import string

# A implémenter eventuellement:
# SupprimerPonctuation
# CompterOccurencesMot
# DiviserTexteEnMots
# RechercherString
# RemplacerChar
# ConvertirTexteEnMajuscule
def ConvertirTextesEnMinuscules(fichiers_sources, dossier_destination):

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
def NettoyerTextes(dossier_fichiers):
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