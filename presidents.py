from files_manager import *

# constantes
dossier_discours_presidents = "./speeches"
dossier_discours_presidents_nettoyes = "./cleaned"
liste_noms_fichiers_discours_presidents = []
dico_fichiers_discours_presidents = {} # clé = num fichier, valeur = nom du fichier
nombre_docs_fichiers_discours_presidents = 0
noms_des_presidents = []
dico_des_questions_sur_stats_mots_corpus = {}

def creer_liste_prenom_nom_formates(noms_des_presidents):
    # DE: A corriger !
    prenoms = {
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"
    }

    liste_prenom_nom_formates = []

    # Utilisons la fonction items() pour parcourir à la fois le nom de famille et le prénom
    for nom_famille, prenom in prenoms.items():
        nom_formatte = f"{prenom} {nom_famille}"
        liste_prenom_nom_formates.append(nom_formatte)

    return liste_prenom_nom_formates
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
def obtenir_nom_fichiers_discours_presidents(dossier_discours_presidents):
    fichiers_discours_presidents = list_of_files(dossier_discours_presidents, ".txt")
    return fichiers_discours_presidents
def remplir_dico_fichiers_discours_presidents_depuis_la_liste(liste_noms_fichiers_discours_presidents):

    for i in range(len(liste_noms_fichiers_discours_presidents)):

        nom_fichier_discours_president = liste_noms_fichiers_discours_presidents[i]

        dico_fichiers_discours_presidents[i+1] = nom_fichier_discours_president

    return dico_fichiers_discours_presidents
def obtenir_liste_prenom_nom_des_presidents(fichiers_discours_presidents):

    # A deplacer dans le fichier "Presidents"
    for fichier in fichiers_discours_presidents:
        nom_president = extraire_nom_president(fichier)
        if nom_president not in noms_des_presidents:
            noms_des_presidents.append(nom_president)

    # Créer la liste des prénoms et noms formatés des présidents
    prenom_nom_des_presidents = creer_liste_prenom_nom_formates(noms_des_presidents)

    return prenom_nom_des_presidents
def obtenir_dicos_occurrences_mots_du_president(nom_president, les_dicos_occurrences_mots_corpus):

    dicos_occurrences_mots_president = []

    # parcourir le dico des fichiers des discours des présidents
    #for num_fichier, nom_fichier_discours_presidents in les_dicos_occurrences_mots_corpus.items():

        #nom_fichier_discours_presidents_lower = nom_fichier_discours_presidents
        #nom_fichier_discours_presidents_lower = nom_fichier_discours_presidents_lower.lower()

        #if nom_president in nom_fichier_discours_presidents_lower:
        #    num_des_discours_du_president.append(num_fichier)

    return dicos_occurrences_mots_president
