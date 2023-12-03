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

def creer_liste_prenom_nom_formattee(noms_presidents):
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

    # Utilisons la fonction items() pour parcourir à la fois le nom de famille et le prénom
    for nom_famille, prenom in prenoms.items():
        nom_formatte = f"{prenom} {nom_famille}"
        liste_prenom_nom_formattee.append(nom_formatte)

    return liste_prenom_nom_formattee

def convertir_textes_en_minuscules(fichiers_sources, dossier_destination):
    """
    Convertit les textes des fichiers sources en minuscules et les stocke dans des nouveaux fichiers dans le dossier de destination.

    Args:
        fichiers_sources: Liste des noms des fichiers sources.
        dossier_destination: Nom du dossier de destination.

    Returns:
        None.
    """

    # Créer le dossier de destination s'il n'existe pas
    if not os.path.exists(dossier_destination):
        os.mkdir(dossier_destination)

    # Parcourir les fichiers sources
    for fichier_source in fichiers_sources:
        # Lire le contenu du fichier
        with open(fichier_source, "r", encoding="utf-8") as f:
            text = f.read()

        # Convertir le texte en minuscules
        text_minuscule = text.lower()

        # Créer le nom du fichier de destination
        fichier_destination = os.path.join(dossier_destination, os.path.basename(fichier_source))

        # Écrire le texte en minuscules dans le fichier de destination
        with open(fichier_destination, "w", encoding="utf-8") as f:
            f.write(text_minuscule)

    print("Les textes ont été convertis en minuscules et stockés dans le dossier 'cleaned'.")