import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


'''def extraire_nom_president(nom_fichier):
    nom_fichier = nom_fichier.replace("Nomination_", "").replace(".txt", "")

    elements = nom_fichier.rsplit("(", 1)

    nom_president = elements[0].strip()

    nom_president = ''.join([char for char in nom_president if not char.isdigit()])

    return nom_president'''

def extraire_nom_president(nom_fichier):
    nom_fichier = nom_fichier.replace("Nomination_", "").replace(".txt", "")

    # Utilisons la fonction rfind pour trouver la dernière occurrence de "("
    index_parenthese = nom_fichier.rfind("(")

    if index_parenthese != -1:
        # Si la parenthèse est trouvée, séparons le nom de famille du prénom
        nom_president = nom_fichier[:index_parenthese].strip()
    else:
        # Si la parenthèse n'est pas trouvée, utilisons le nom de fichier tel quel
        nom_president = nom_fichier.strip()

    # Supprimons les chiffres du nom du président
    nom_president = ''.join([char for char in nom_president if not char.isdigit()])

    return nom_president



def associer_prenom_a_president(nom_president):
    prenoms = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
        # Ajoutez d'autres présidents au besoin
    }

    # Trouver le dernier mot dans le nom du président
    mots = nom_president.split(" ")
    nom_famille = mots[-1]

    # Vérifier si le nom de famille est dans le dictionnaire
    if nom_famille in prenoms:
        prenom = prenoms[nom_famille]
    else:
        prenom = "Prénom non trouvé"

    return prenom

def afficher_liste_presidents(noms_presidents):

    noms_uniques = set(noms_presidents)
    print("Liste des noms des présidents (sans doublons):")
    for nom in noms_uniques:
        print(nom)


'''def creer_liste_prenom_nom_formattee(noms_presidents):
    prenoms = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
        # Ajoutez d'autres présidents au besoin
    }

    liste_prenom_nom_formattee = []

    for nom_president in noms_presidents:
        mots = nom_president.split(" ")
        nom_famille = mots[-1]
        prenom = prenoms.get(nom_famille, "Prénom non trouvé")

        # Formater le prénom et le nom de famille
        nom_formatte = f"{prenom} {nom_famille}"

        # Ajouter à la liste
        liste_prenom_nom_formattee.append(nom_formatte)

    return liste_prenom_nom_formattee'''

def creer_liste_prenom_nom_formates(noms_presidents):
    prenoms = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"

    }

    liste_prenom_nom_formattee = []

    # Utilisons la fonction items() pour parcourir à la fois le nom de famille et le prénom
    for nom_famille, prenom in prenoms.items():
        nom_formatte = f"{prenom} {nom_famille}"
        liste_prenom_nom_formattee.append(nom_formatte)

    return liste_prenom_nom_formattee


import os

# ... (autres fonctions inchangées)

def convertir_textes_en_minuscules(fichiers_sources, dossier_destination):
    """
    Convertit les textes des fichiers sources en minuscules et les stocke dans des nouveaux fichiers dans le dossier de destination.

    Args:
        fichiers_sources: Liste des noms des fichiers sources.
        dossier_destination: Nom du dossier de destination.

    Returns:
        None.
    """

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

import os
import string

# ... (autres fonctions inchangées)

def nettoyer_textes(dossier_source, dossier_destination):
    """
    Nettoie les textes des fichiers dans le dossier source en supprimant la ponctuation.
    Les fichiers modifiés sont stockés dans le dossier de destination.

    Args:
        dossier_source: Nom du dossier source.
        dossier_destination: Nom du dossier de destination.

    Returns:
        None.
    """

    # Récupérer le chemin absolu du dossier source
    chemin_dossier_source = os.path.join(os.path.dirname(os.path.abspath(__file__)), dossier_source)

    # Créer le dossier de destination s'il n'existe pas
    chemin_dossier_destination = os.path.join(os.path.dirname(os.path.abspath(__file__)), dossier_destination)
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
def dico_chaine_de_caractere(mot):
    def compter_mots(chaine):
        mots = chaine.split()  # Divise la chaîne en une liste de mots
        compteur_mots = {}

        for mot in mots:
            mot = mot.lower()  # Convertit le mot en minuscules pour éviter la distinction entre majuscules et minuscules
            mot = mot.strip('.,!?()[]{}\'"')  # Supprime la ponctuation autour des mots
            if mot:
                compteur_mots[mot] = compteur_mots.get(mot, 0) + 1

        return compteur_mots

