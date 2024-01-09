import main
import files_manager as fm
import string_manager as sm
import TF_IDF as tf_idf
import math_vecteurs as math_vect
import presidents as les_presidents
import traitement_questions_reponses as tt_quest_rep
import random
from tkinter import messagebox

dico_intros_avant_reponse_trouvee = {}

# region "traitement question prédéfinies sur stats discours des presidents"
def obtenir_les_mots_les_moins_importants_des_discours_des_presidents():

    reponse = ""
    liste_mots_moins_importants = []
    reponse_complete = ""

    reponse, liste_mots_moins_importants = les_presidents.obtenir_les_mots_les_moins_importants_des_discours_des_presidents()

    if reponse == "":
        reponse = "Aucun mots d'importance moindre n'a été trouvé."
        return reponse

    phrase_intro = tt_quest_rep.obtenir_aleatoirement_phrase_intro_avant_reponse_trouvee()
    reponse_complete += phrase_intro + "\n\n" + reponse

    return reponse_complete


def obtenir_les_mots_les_plus_importants_des_discours_des_presidents():

    reponse = ""
    reponse_complete = ""

    reponse = les_presidents.obtenir_les_mots_les_plus_importants_des_discours_des_presidents()

    if reponse == "":
        reponse = "Aucun mots importants n'a été trouvé."
        return reponse

    phrase_intro = tt_quest_rep.obtenir_aleatoirement_phrase_intro_avant_reponse_trouvee()
    reponse_complete = phrase_intro + "\n\n" + reponse

    return reponse_complete

def obtenir_les_mots_importants_les_plus_employes_par_un_president(nom_president, les_dicos_occurrences_mots_corpus, nombre_mots_a_trouver = 50):

    reponse = ""
    reponse_complete = ""

    reponse = les_presidents.obtenir_les_mots_importants_les_plus_employes_par_un_president(nom_president, les_dicos_occurrences_mots_corpus, 50)

    if reponse == "":
        reponse = "Désolé, il n'y a aucun résultat pour le président " + nom_president
        return reponse

    phrase_intro = tt_quest_rep.obtenir_aleatoirement_phrase_intro_avant_reponse_trouvee()
    reponse_complete = phrase_intro + "\n\n" + reponse

    return reponse_complete

def obtenir_presidents_ayant_prononce_un_terme(liste_termes, les_dicos_occurrences_mots_corpus):
    # parcourir tous les dicos de tous les présidents et, pour chacun, noter le nombre de fois que le terme
    # passé en param apparait
    return

def obtenir_le_president_ayant_le_plus_prononce_un_terme(terme, les_dicos_occurrences_mots_corpus):

    return

def obtenir_reponse_sur_stats_mots_corpus(num_question):

    reponse = ""

    liste_termes = ["climat", "ecologie", "écologie"]

    if num_question == 1:
        reponse = obtenir_les_mots_les_moins_importants_des_discours_des_presidents()
    elif num_question == 2:
        reponse = obtenir_les_mots_les_plus_importants_des_discours_des_presidents()
    elif num_question == 3:
        # Trouver les mots significatifs les plus répétés par J. Chirac
        reponse = obtenir_les_mots_importants_les_plus_employes_par_un_president("chirac", tf_idf.les_dicos_occurrences_mots_corpus, 50)
    elif num_question == 4:
        reponse = obtenir_le_president_ayant_le_plus_prononce_un_terme("nation", tf_idf.les_dicos_occurrences_mots_corpus)
    elif num_question == 5:
        reponse = obtenir_presidents_ayant_prononce_un_terme(liste_termes, tf_idf.les_dicos_occurrences_mots_corpus)
    else:
        messagebox.showinfo("Information","Cette fonctionnalité n'est pas encore implémentée")

    return reponse


# endregion "traitement question prédéfinies sur stats discours des presidents"


# region "traitement question utilisateur"
def trouver_doc_le_plus_pertinent_a_question(vecteur_tf_idf_question, matrice_tf_idf_corpus_transposee,
                                             dico_noms_fichiers_discours_presidents):
    # pour chaque fichiers du corpus dans la matrice
    num_doc_pertinent = 0
    score_similarite = 0.0
    score_similarite_le_plus_eleve = 0.0
    nb_docs = 0

    nb_docs = len(dico_noms_fichiers_discours_presidents) + 1

    for num_doc in range(1, nb_docs):

        # calculer la similarité entre le vecteur de la question et le vecteur du doc n de la matrice transposee
        score_similarite = math_vect.calcul_similarite_vecteurs(
            vecteur_tf_idf_question[tf_idf.vecteur_tf_idf_question_num_ligne_score_tf_idf],
            matrice_tf_idf_corpus_transposee[num_doc])

        if score_similarite > score_similarite_le_plus_eleve:
            score_similarite_le_plus_eleve = score_similarite
            num_doc_pertinent = num_doc

    return num_doc_pertinent


def generation_reponse_utilisateur_depuis_texte(mot_specifique, nom_doc_pertinent):

    mot_specifique_pas_trouve = 0

    # ouvrir le doc susceptible de contenir la réponse
    texte = fm.lire_contenu_fichier(les_presidents.dossier_discours_presidents, nom_doc_pertinent)

    # reperer la phrase contenant le mot-clé et la renvoyer en tant que réponse
    reponse = sm.trouver_phrase_entourant_mot(texte, mot_specifique, nom_doc_pertinent)

    if reponse =="":
        mot_specifique_pas_trouve = 1
        reponse = "Une erreur est survenue: le mot spécifique " + "'" + mot_specifique + "'" + " n'a pas été trouvé dans le texte "
        if nom_doc_pertinent != "":
            reponse += " du fichier " + "'" + nom_doc_pertinent + "'"
        return reponse, mot_specifique_pas_trouve

    return reponse, mot_specifique_pas_trouve


def traitement_question_utilisateur(question):

    # 1) Nettoyer la question
    question = sm.nettoyer_texte(question)

    # supprimer d'eventuels retour à la ligne parasites en fin de chaine
    question = question.rstrip()

    # 2) creer et initialiser le score à 0 du le vecteur tf_idf_question par copie de la matrice_tf_idf_corpus_transposee.
    # Elle contient uniquement 2 lignes (mots du corpus et score tf-idf de ces mots)
    # et M colonnes (nbre total de mots)
    tf_idf.vecteur_tf_idf_question = tf_idf.ini_matrice_tf_idf_question(tf_idf.matrice_tf_idf_corpus_transposee)

    # remplir les scores du vecteur_tf_idf_question en fonction des data dispos dans matrice_tf_idf_corpus_transposee
    tf_idf.vecteur_tf_idf_question = tf_idf.creer_vecteur_tf_idf_question(question, tf_idf.vecteur_tf_idf_question,
                                                                          tf_idf.matrice_tf_idf_corpus_transposee)

    # 3) trouver le num du doc le plus pertinent à la question posée
    num_doc_pertinent = 0
    num_doc_pertinent = trouver_doc_le_plus_pertinent_a_question(tf_idf.vecteur_tf_idf_question,
                                                                 tf_idf.matrice_tf_idf_corpus_transposee,
                                                                 les_presidents.dico_fichiers_discours_presidents)

    if num_doc_pertinent == 0:
        return "Il n'y a aucun document capable de répondre à votre question."

    # obtenir le nom du doc pertinent capable de répondre à la question
    nom_doc_pertinent = les_presidents.dico_fichiers_discours_presidents[num_doc_pertinent]

    # trouver le mot clé avec score tf-idf le plus élevé afin de répondre à la question
    mot_vecteur_question_avec_score_le_plus_eleve = tf_idf.obtenir_mot_avec_score_tf_idf_le_plus_eleve(
        tf_idf.vecteur_tf_idf_question)

    if mot_vecteur_question_avec_score_le_plus_eleve == "":
        return "Il n'y a pas de mot significatif dans votre question, je ne peux pas répondre, désolé."

    # rechercher la phrase contenant le mot clé dans le doc pertinent: Elle sera la réponse à la question
    reponse, mot_specifique_pas_trouve = generation_reponse_utilisateur_depuis_texte(mot_vecteur_question_avec_score_le_plus_eleve, nom_doc_pertinent)

    # ici: mettre un mot ou une phrase de présentation de la réponse
    # phrase_intro = obtenir_phrase_intro_reponse (dico_phrases_intro)
    if mot_specifique_pas_trouve == 1:
        return reponse

    phrase_intro = tt_quest_rep.obtenir_aleatoirement_phrase_intro_avant_reponse_trouvee()

    phrase_intro += "\n\n"

    return phrase_intro + reponse


def remplir_dico_intro_avant_reponse_trouvee():

    # clé = num ID unique, valeurs = phrase d'intro

    dico_intros_avant_reponse_trouvee[1] = "Voici ce que j'ai trouvé: "
    dico_intros_avant_reponse_trouvee[2] = "Bien sur, il y a ceci: "
    dico_intros_avant_reponse_trouvee[3] = "En cherchant bien, voici la réponse que j'ai trouvé: "
    dico_intros_avant_reponse_trouvee[4] = "Voilà ce que l'on peut dire sur le sujet: "
    dico_intros_avant_reponse_trouvee[5] = "Vous trouverez ci-dessous une réponse murement réfléchie: "
    dico_intros_avant_reponse_trouvee[6] = "En faisant un gros effort, j'ai trouvé ça: "
    dico_intros_avant_reponse_trouvee[7] = "J'espère que vous trouverez votre bonheur grâce à cette réponse: "
    dico_intros_avant_reponse_trouvee[8] = "Et voilà pour vous: "
    dico_intros_avant_reponse_trouvee[9] = "Il existe cet élément de réponse possible: "
    dico_intros_avant_reponse_trouvee[10] = "Cela n'a pas été facile, mais j'ai tout de même trouvé ça pour vous: "

    return

def obtenir_aleatoirement_phrase_intro_avant_reponse_trouvee():

    nombre_max = len(dico_intros_avant_reponse_trouvee)

    # Générer un nombre entier aléatoire
    nombre_aleatoire = random.randint(1, nombre_max)

    return dico_intros_avant_reponse_trouvee[nombre_aleatoire]

# endregion "traitement question utilisateur"
