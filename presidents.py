
# constantes
dossier_discours_presidents = "./speeches"
dossier_discours_presidents_nettoyes = "./cleaned"


# To Do de DE:

# Remplacer ce code horrible ! A quoi sert de passer "noms_presidents" si on ne l'utilise jamais ?!?

def creer_liste_prenom_nom_formates(noms_presidents):
    prenoms = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
    }

    liste_prenom_nom_formatee = []

    # Utilisons la fonction items() pour parcourir à la fois le nom de famille et le prénom
    for nom_famille, prenom in prenoms.items():
        nom_formatte = f"{prenom} {nom_famille}"
        liste_prenom_nom_formatee.append(nom_formatte)

    return liste_prenom_nom_formatee

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
    # To do : Remplacer le code "en dur" ci-dessous" par un fichier texte
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