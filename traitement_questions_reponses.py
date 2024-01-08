import main
import files_manager as fm
import string_manager as sm
import TF_IDF as tf_idf
import math_vecteurs as math_vect
import presidents as les_presidents

#region "traitement question prédéfinies sur stats discours des presidents"
def obtenir_les_mots_les_moins_importants_des_discours_des_presidents():
    # "Afficher les mots les MOINS importants dans les discours des présidents"
    # le mot est non important si son TF-IDF = 0 pour chaque fichiers
    liste_mots_moins_importants = []
    mot_courant = ""
    reponse = ""
    nb_lignes_fichiers = les_presidents.nombre_docs_fichiers_discours_presidents + 1

    for num_mot in range(len(tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot])):

        mot_courant = tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot][num_mot]

        # examiner le score TF-IDF de ce mot pour chaque fichier
        for num_fichier in range(1, nb_lignes_fichiers):

            # score > 0 pour ce mot, il ne fait pas partie des moins importants, passer au mot suivant
            if tf_idf.matrice_tf_idf_corpus_transposee[num_fichier][num_mot] != 0.0:
                break
            # pas de score pour ce mot, il est tjrs à 0 ds ts les docs, il fait partie des moins importants
            if num_fichier == (nb_lignes_fichiers - 1):
                liste_mots_moins_importants.append(mot_courant)

    if len(liste_mots_moins_importants) == 0:
        reponse = "Aucun mots d'importance moindre n'a été trouvé"
        return reponse

    # concatener tous les mots dans la chaine en les séparant par une virgule
    string_mots_moins_importants = ', '.join(liste_mots_moins_importants) # présentation en ligne
    # string_mots_moins_importants = ', \n'.join(liste_mots_moins_importants) # presentation en colonne

    string_mots_moins_importants += "."

    reponse = "Voici la liste des " + str(len(liste_mots_moins_importants)) + " mots les moins importants dans les discours des présidents : " + '\n\n' + string_mots_moins_importants

    return reponse
def obtenir_les_mots_avec_TF_IDF_les_plus_eleves_des_discours_des_presidents():

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
    nb_lignes_fichiers = les_presidents.nombre_docs_fichiers_discours_presidents + 1

    for num_mot in range(len(tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot])):

        mot_courant = tf_idf.matrice_tf_idf_corpus_transposee[tf_idf.matrice_tf_idf_corpus_transposee_num_ligne_mot][num_mot]

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
        reponse = "Aucun mots avec un score TF-IDF positif n'a été trouvé"
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

    reponse = "Voici la liste des " + str(nombre_mots_max_a_afficher) + " premiers mots des discours des présidents avec les scores TF-IDF les plus élevés et classés par ordre décroissants : " + '\n' + chaine_resultat

    return reponse
def obtenir_les_mots_significatifs_les_plus_repetes_par_president(nom_president, les_dicos_occurrences_mots_corpus):

    # trouver les dicos propres  president passé en param
    dicos_dicos_occurrences_mots_president = les_presidents.obtenir_dicos_occurrences_mots_du_president(nom_president)

    return dicos_dicos_occurrences_mots_president
def trouver_presidents_ayant_prononce_x_fois_un_terme(terme, les_dicos_occurrences_mots_corpus):

    # parcourir tous les dicos de tous les présidents et, pour chacun, noter le nombre de fois que le terme
    # passé en param apparait



    return

def obtenir_reponse_question_sur_stats_mots_corpus(num_question):

    reponse = ""

    if num_question == 1:
        reponse = obtenir_les_mots_les_moins_importants_des_discours_des_presidents()
    elif num_question == 2:
        reponse = obtenir_les_mots_avec_TF_IDF_les_plus_eleves_des_discours_des_presidents()
    elif num_question == 3:
        # Trouver les mots significatifs les plus répétés par J. Chirac
        reponse = obtenir_les_mots_significatifs_les_plus_repetes_par_president("chirac", tf_idf.les_dicos_occurrences_mots_corpus)

    return reponse
#endregion "traitement question prédéfinies sur stats discours des presidents"


#region "traitement question utilisateur"
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
def traitement_question_utilisateur(question):

    # 1) Nettoyer la question
    question = sm.nettoyer_texte(question)

    # 2) creer et initialiser le score à 0 du le vecteur tf_idf_question par copie de la matrice_tf_idf_corpus_transposee.
    # Elle contient uniquement 2 lignes (mots du corpus et score tf-idf de ces mots)
    # et M colonnes (nbre total de mots)
    tf_idf.vecteur_tf_idf_question = tf_idf.ini_matrice_tf_idf_question(tf_idf.matrice_tf_idf_corpus_transposee)
    # remplir les scores du vecteur_tf_idf_question en fonction des data dispos dans matrice_tf_idf_corpus_transposee
    tf_idf.vecteur_tf_idf_question = tf_idf.creer_vecteur_tf_idf_question(question, tf_idf.vecteur_tf_idf_question, tf_idf.matrice_tf_idf_corpus_transposee)

    # 3) trouver le doc le plus pertinent à la question posée
    num_doc_pertinent = 0
    num_doc_pertinent = trouver_doc_le_plus_pertinent_a_question(tf_idf.vecteur_tf_idf_question, tf_idf.matrice_tf_idf_corpus_transposee, les_presidents.dico_fichiers_discours_presidents)

    if num_doc_pertinent == 0:
        return "Il n'y a aucun document capable de répondre à votre question."

    # obtenir le nom du doc pertinent capable de répondre à la question
    nom_doc_pertinent = les_presidents.dico_fichiers_discours_presidents[num_doc_pertinent]

    # trouver le mot clé avec score tf-idf le plus élevé afin de répondre à la question
    mot_vecteur_question_avec_score_le_plus_eleve = tf_idf.obtenir_mot_avec_score_tf_idf_le_plus_eleve(tf_idf.vecteur_tf_idf_question)

    if mot_vecteur_question_avec_score_le_plus_eleve == "":
        return "Il n'y a aucun document capable de répondre à votre question."

    # rechercher la phrase contenant le mot clé dans le doc pertinent: Elle sera la réponse à la question
    reponse = generation_reponse_utilisateur(mot_vecteur_question_avec_score_le_plus_eleve, nom_doc_pertinent)

    if reponse == "":
        return "Aucun document susceptible de répondre à votre question n'a été trouvé."

    return reponse

def generation_reponse_utilisateur(mot_avec_score_tf_idf_le_plus_eleve, nom_doc_pertinent):

    reponse = ""

    # ouvrir le doc susceptible de contenir la réponse
    doc = fm.lire_contenu_fichier(les_presidents.dossier_discours_presidents, nom_doc_pertinent)

    # reperer la phrase contenant le mot-clé dans le fichier


    # selectionner cette phrase et la renvoyer en tant que réponse


    return reponse

#endregion "traitement question utilisateur"