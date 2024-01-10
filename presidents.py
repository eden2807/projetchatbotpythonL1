
import TF_IDF as tf_idf
from files_manager import *

# constantes
dossier_discours_presidents = "./speeches"
dossier_discours_presidents_nettoyes = "./cleaned"
liste_noms_fichiers_discours_presidents = []
dico_fichiers_discours_presidents = {} # clé = num fichier, valeur = nom du fichier
nombre_docs_fichiers_discours_presidents = 0
noms_des_presidents = []
#dico_des_questions_sur_stats_mots_corpus = {}

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

    for fichier in fichiers_discours_presidents:
        nom_president = extraire_nom_president(fichier)
        if nom_president not in noms_des_presidents:
            noms_des_presidents.append(nom_president)

    # Créer la liste des prénoms et noms formatés des présidents
    prenom_nom_des_presidents = creer_liste_prenom_nom_formates(noms_des_presidents)

    return prenom_nom_des_presidents

def obtenir_liste_nom_des_presidents(fichiers_discours_presidents):

    for fichier in fichiers_discours_presidents:
        nom_president = extraire_nom_president(fichier)
        if nom_president not in noms_des_presidents:
            noms_des_presidents.append(nom_president)

    return noms_des_presidents

def obtenir_les_dicos_occurrences_mots_pour_un_president(nom_president, les_dicos_occurrences_mots_corpus):

    nom_president_lower = ""
    dicos_occurrences_mots_president = {}

    # être indépendant des min/maj en mettant tout en min
    nom_president_lower = nom_president.lower()

    # parcourir le dico des dicos occurrences mots corpus de chaque président
    for nom_fichier_discours_presidents, dico in les_dicos_occurrences_mots_corpus.items():

        # être indépendant des min/maj en mettant tout en min
        nom_fichier_discours_presidents_lower = nom_fichier_discours_presidents
        nom_fichier_discours_presidents_lower = nom_fichier_discours_presidents_lower.lower()

        if nom_president_lower in nom_fichier_discours_presidents_lower:
            dicos_occurrences_mots_president[nom_fichier_discours_presidents] = dico

    return dicos_occurrences_mots_president


def obtenir_les_mots_les_moins_importants_des_discours_des_presidents():

    # "Afficher les mots les MOINS importants dans les discours des présidents"
    # le mot est non important si son TF-IDF = 0 pour chaque fichiers

    liste_mots_moins_importants = []
    mot_courant = ""
    reponse = ""
    nb_lignes_fichiers = nombre_docs_fichiers_discours_presidents + 1

    for num_mot in range(
            len(tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot])):

        mot_courant = tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot][
            num_mot]

        # examiner le score TF-IDF de ce mot pour chaque fichier
        for num_fichier in range(1, nb_lignes_fichiers):

            # score > 0 pour ce mot, il ne fait pas partie des moins importants, passer au mot suivant
            if tf_idf.matrice_tf_idf_corpus_transposee[num_fichier][num_mot] != 0.0:
                break
            # pas de score pour ce mot, il est tjrs à 0 ds ts les docs, il fait partie des moins importants
            if num_fichier == (nb_lignes_fichiers - 1):
                liste_mots_moins_importants.append(mot_courant)

    if len(liste_mots_moins_importants) == 0:
        reponse = ""
        return reponse

    # concatener tous les mots dans la chaine en les séparant par une virgule
    string_mots_moins_importants = ', '.join(liste_mots_moins_importants)  # présentation en ligne
    # string_mots_moins_importants = ', \n'.join(liste_mots_moins_importants) # presentation en colonne

    string_mots_moins_importants += "."

    reponse = "Liste des " + str(
        len(liste_mots_moins_importants)) + " mots les moins importants dans les discours des présidents : " + '\n\n' + string_mots_moins_importants

    return reponse, liste_mots_moins_importants


def obtenir_les_mots_les_plus_importants_des_discours_des_presidents():

    # "Afficher les mots les PLUS importants dans les discours des présidents".
    # Parcourir la matrice et stocker dans un dico tous les mots ayant un TF-IDF > 0.
    # Les clés de ce dico sont les mots (uniques) et leur valeurs sont les scores.
    # Trier ensuite le dico par ordre décroissant puis afficher les n premiers mots les plus importants.

    dico_mots_TF_IDF = {}
    nombre_mots_max_a_afficher = 100
    mot_courant = ""
    score_mot_courant = 0
    chaine_resultat = ""
    reponse = ""

    nb_lignes_fichiers = nombre_docs_fichiers_discours_presidents + 1

    for num_mot in range(
            len(tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot])):

        mot_courant = tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot][
            num_mot]

        score_mot_courant = 0

        # examiner le score TF-IDF de ce mot pour chaque fichier
        for num_fichier in range(1, nb_lignes_fichiers):

            score_mot_courant += tf_idf.matrice_tf_idf_corpus_transposee[num_fichier][num_mot]

            # score > 0 pour ce mot, il fait potentiellement  partie des plus importants
            if num_fichier == (nb_lignes_fichiers - 1) and score_mot_courant > 0:
                # ajouter le mot (clé) et le score du mot (value) dans le dico
                # Note: arrondir à 2 chiffres apres virgule, sinon les calculs en float peuvent avoir cet aspect: 0.6 + 1.2 = 1.7999999 !
                dico_mots_TF_IDF[mot_courant] = round(score_mot_courant, 2)

    if len(dico_mots_TF_IDF) == 0:
        reponse = ""
        return reponse

    # tri dans le dico des mots avec TF-IDF élevés par ordre décroissant (les scores les + élevés sont donc les premiers)

    # Obtenir une liste triée de tuples (clé, valeur) basée sur les valeurs
    items_tries = sorted(dico_mots_TF_IDF.items(), key=lambda x: x[1], reverse=True)

    # limiter à n items
    items_tries_limites = items_tries[:nombre_mots_max_a_afficher]

    chaine_resultat = '\n'
    chaine_resultat = '\n' + "Format:" + '\n'
    chaine_resultat += "mot = score TF-IDF" + '\n\n'
    chaine_resultat += "'"

    # Construire une chaîne à partir de la liste triée
    for cle, valeur in items_tries_limites:
        chaine_resultat += f"{cle} = {valeur}'\n'"

    # Supprimer la virgule, l'espace et le retour à la ligne à la fin de la chaîne
    chaine_resultat = chaine_resultat[:-5]

    reponse = "Liste des " + str(
        nombre_mots_max_a_afficher) + " premiers mots des discours des présidents avec les scores TF-IDF les plus élevés et classés par ordre décroissants : " + '\n' + chaine_resultat

    return reponse

def obtenir_les_mots_importants_les_plus_employes_par_un_president(nom_president, les_dicos_occurrences_mots_corpus, nombre_mots_a_trouver):

    dicos_occurrences_mots_corpus = {}
    dico_mots_les_plus_utilises_par_ce_president = {}
    liste_mots_moins_importants = []

    # obtenir le ou les dico(s) occurrences mots de ce president
    dicos_occurrences_mots_du_president = obtenir_les_dicos_occurrences_mots_pour_un_president(nom_president, les_dicos_occurrences_mots_corpus)

    if len(dicos_occurrences_mots_du_president) == 0:
        return

    # obtenir la liste des mots les moins importants.
    # rappel: un mot est dit non important si son score tf-idf = 0 dans tous les fichiers
    rep, liste_mots_moins_importants = obtenir_les_mots_les_moins_importants_des_discours_des_presidents()

    # pour chaque dico, trier les mots des plus employes aux moins employes
    for nom_fichier_discours_presidents, dico in dicos_occurrences_mots_du_president.items():

        # Obtenir une liste triée de tuples (mot, nb occurrence mot) basée sur le nb occurrences de ce mot de la + élevée à la - élevée
        mots_tries = sorted(dico.items(), key=lambda x: x[1], reverse=True)

        # ici : parcourir les n premiers mots (determiné par 'nombre_mots_a_trouver') de la liste triée et les stocker dans un dico
        for i in range(len(mots_tries)):

            mot_courant = mots_tries[i][0]
            val_courante = mots_tries[i][1]

            # verifier que le mot soit significatif avant de l'ajouter (score tf-idf pr ts les fichiers > 0)
            if mot_courant in liste_mots_moins_importants:
                continue

            # ajouter le mot reconnu comme étant significatif
            if dico_mots_les_plus_utilises_par_ce_president.get(mot_courant):
                dico_mots_les_plus_utilises_par_ce_president[mot_courant] += val_courante
            else:
                dico_mots_les_plus_utilises_par_ce_president[mot_courant] = val_courante

            # nombre de mots à trouver atteint ?
            if i == nombre_mots_a_trouver:
                break

    # aucun mot trouvé, le signaler et sortir
    if len(dico_mots_les_plus_utilises_par_ce_president) == 0:
        reponse = ""

    # A ce stade, des mots on été trouvé. Les trier par ordre décroissant sur le nb de prononciation
    res = ""

    mots_les_plus_utilises_tries = sorted(dico_mots_les_plus_utilises_par_ce_president.items(), key=lambda x: x[1], reverse=True)

    # Construire une chaîne à partir de la liste triée des mots
    for mot, score in mots_les_plus_utilises_tries:
        res += f"{mot} = {score}'\n'"

    # Supprimer la virgule, l'espace et le retour à la ligne à la fin de la chaîne
    res = res[:-5]

    return "Liste des mots importants les plus utilisés par le président " + nom_president + ":" + "\n\n" + res


def obtenir_presidents_ayant_prononce_un_terme(mot, les_dicos_occurrences_mots_corpus):

    # stocker le res. clé = nom du président, valeurs = nb de fois ou le mot a été prononcé
    dico_presidents_et_nb_prononciation_mot = {}

    nom_president = ""

    # parcourir tous les dicos de tous les présidents et, pour chacun d'entre eux, noter le
    # nombre de fois que le terme passé en param apparait
    # parcourir le dico des dicos occurrences mots corpus de chaque président
    for nom_fichier_discours_presidents, dico_occurrences_mot in les_dicos_occurrences_mots_corpus.items():

        # extraire le nom du président du nom du fichier ayant servi à la création du dico d'occurrence de mots
        nom_president = extraire_nom_president(nom_fichier_discours_presidents)

        # le président courant a-t-il déjà prononcé ce mot ? Si oui, connaitre le nombre de fois qu'il l'a fait dans ce discours
        if dico_occurrences_mot.get(mot):

            nb_occurrences_mot = dico_occurrences_mot[mot]

            # ajouter le nb d'occurrences de ce mot pour le président courant
            if dico_presidents_et_nb_prononciation_mot.get(nom_president):
                # si ce président a déjà prononcé ce mot dans un autre discours, additionner au nb existant
                dico_presidents_et_nb_prononciation_mot[nom_president] += nb_occurrences_mot
            else:
                # sinon créer la nouvelle entrée
                dico_presidents_et_nb_prononciation_mot[nom_president] = nb_occurrences_mot

    return dico_presidents_et_nb_prononciation_mot


def creer_dicos_stats_sur_mot_employe_par_les_presidents(mot_a_trouver, les_dicos_occurrences_mots_corpus, liste_nom_des_presidents):

    # pour chaque dico existant et donc pour chaque président,
    liste_nom_des_presidents = obtenir_liste_nom_des_presidents(liste_nom_des_presidents)

    nom_president = ""

    # obtenir le ou les dico(s) occurrences mots de ce president
    dicos_occurrences_mots_du_president = obtenir_les_dicos_occurrences_mots_pour_un_president(nom_president,
                                                                                               les_dicos_occurrences_mots_corpus)

    if len(dicos_occurrences_mots_du_president) == 0:
        return



    # obtenir la liste des mots les moins importants.
    # rappel: un mot est dit non important si son score tf-idf = 0 dans tous les fichiers
    #rep, liste_mots_moins_importants = obtenir_les_mots_les_moins_importants_des_discours_des_presidents()

    # pour chaque dico, trier les mots des plus employes aux moins employes
    #for nom_fichier_discours_presidents, dico in dicos_occurrences_mots_du_president.items():

        # trouver le mot en question si existant et le conserver dans un dico dont la clé
        # est le nom du président et la valeur est le nb occurrences du mot pr ce président


    return


def trouver_presidents_ayant_employe_un_terme():

    return


def trouver_president_ayant_le_plus_employer_un_terme():

    return

