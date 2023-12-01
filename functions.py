import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraire_nom_president(nom_fichier):
    nom_fichier = nom_fichier.replace("Nomination_", "").replace(".txt", "")

    elements = nom_fichier.rsplit("(", 1)

    nom_president = elements[0].strip()

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

    for nom_president in noms_presidents:
        mots = nom_president.split(" ")
        nom_famille = mots[-1]
        prenom = prenoms.get(nom_famille, "Prénom non trouvé")

        # Formater le prénom et le nom de famille
        nom_formatte = f"{prenom} {nom_famille}"

        # Ajouter à la liste
        liste_prenom_nom_formattee.append(nom_formatte)

    return liste_prenom_nom_formattee