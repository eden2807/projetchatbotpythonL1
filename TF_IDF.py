import os
import math as ma
import lists_manager as lm
import copy

les_dicos_occurrences_mots_corpus = {}
matrice_tf_corpus = []
matrice_idf_corpus = []
matrice_idf_corpus_num_col_mot = 0
matrice_tf_idf_corpus = []
matrice_tf_idf_corpus_num_ligne_mot = 0
matrice_tf_idf_corpus_num_ligne_score = 1
matrice_tf_idf_corpus_transposee = []
matrice_tf_idf_corpus_transposee_num_ligne_mot = 0
matrice_tf_discours_presidents_num_col_mot = 0
matrice_idf_discours_presidents_num_col_mot = 0
matrice_tf_num_col_score_idf = 1
matrice_transposée_idf_discours_presidents_num_ligne_mot = 0
vecteur_tf_idf_question = []
vecteur_tf_idf_question_num_ligne_mot = 0
vecteur_tf_idf_question_num_ligne_score_tf_idf = 1
mot_existant = 1

###############################################################################################"
# ADAM:
def dico_chaine_de_caractere(mot):
    def calculer_tf(chaine):
        mots = chaine.split()  # Divise la chaîne en une liste de mots
        compteur_mots = {}

        for mot in mots:
            mot = mot.lower()  # Convertit le mot en minuscules pour éviter la distinction entre majuscules et minuscules
            mot = mot.strip('.,!?()[]{}\'"')  # Supprime la ponctuation autour des mots
            if mot:
                compteur_mots[mot] = compteur_mots.get(mot, 0) + 1

        # Calculer la fréquence du terme (TF) pour chaque mot
        total_mots = len(mots)
        tf = {mot: occurences / total_mots for mot, occurences in compteur_mots.items()}

        return tf
# ADAM:
def calculer_idf(corpus_directory):

    mots_par_document = {}  # Dictionnaire pour stocker les mots présents dans chaque document
    total_documents = 0  # Compteur du nombre total de documents dans le corpus

    # Parcours de tous les fichiers dans le répertoire du corpus
    for filename in os.listdir(corpus_directory):
        if filename.endswith(".txt"):
            with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
                document = file.read()
                mots = set(document.split())  # Utilisation d'un  ensemble pour obtenir les mots uniques dans le document
                mots_par_document[filename] = mots
                total_documents += 1

    # Calcul de l'IDF pour chaque mot
    idf = {}
    for document, mots in mots_par_document.items():
        for mot in mots:
            idf[mot] = idf.get(mot, 0) + 1

    for mot, occurrences in idf.items():
        idf[mot] = ma.log(total_documents / (1 + occurrences))  # Ajout de 1 pour éviter la division par zéro

    return idf
###############################################################################################"

def creer_dico_occurences_mots(texte):

    dico_nombre_occurences_mots = {}

    # transformer le texte en liste
    liste_mots_texte = texte.split()

    # parcourir cette liste de mots et comptabiliser le nombre d'occurences pour chacun d'entre eux
    for mot in liste_mots_texte:

        if mot not in dico_nombre_occurences_mots.keys():

            # chercher le nombre d'occurences de ce mots dans la liste contenant le texte entier
            nombre_occurences_mot = liste_mots_texte.count(mot)

            # stocker le nombre d'occurences de ce mots
            dico_nombre_occurences_mots[mot] = nombre_occurences_mot

    return  dico_nombre_occurences_mots
def creer_tous_les_dicos_occurrences_mots(dossier_fichiers, extension_fichiers = ".txt"):

    les_dicos_occurrences_mots = {}
    dico_occurences_mots = {}

    # parcourir tous les fichiers dispos dans dossier_fichiers
    for nom_fichier in os.listdir(dossier_fichiers):

        if nom_fichier.endswith(extension_fichiers):

            # assembler le chemin complet du fichier (path dossiers + nom fichier)
            chemin_fichier = os.path.join(dossier_fichiers, nom_fichier)

            # Lire le contenu du fichier
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                texte = f.read()

            # créer le dico d'occurrences de mots
            dico_occurences_mots = creer_dico_occurences_mots(texte)

            # le stocker dans le dico des dicos d'occurrences de mots
            les_dicos_occurrences_mots[nom_fichier] = dico_occurences_mots

    return les_dicos_occurrences_mots
def creer_matrice_tf(les_dicos_occurrences_mots):

    # def d'une ligne composant la matrice TF
    # La ligne 0 de la matrice est une ligne particulière: col 0 = vide, cols suivantes:
    # Elle contient le nom des docs dans l'ordre des dicos placés dans le dico "les_dicos_occurrences_mots"
    # Détails des lignes suivantes: col 0 = mot, col suivantes = nbre occurrences mot dans les différents docs
    # existants, suivant leur colonnes propres.
    # Note: Il doit donc y avoir autant de colonnes que de docs, chaque doc possedant son propre
    # dictionnaire d'occurrences de mots.

    # La matrice tf est une liste 2D
    matrice_tf = []

    # Connaitre le nombre de colonnes nécessaires pour la matrice
    nombre_docs_occurrences_mots = len(les_dicos_occurrences_mots)

    # def d'une ligne de la matrice: col mot + n * col avec n = nbre docs occurences mots
    ligne_matrice_tf = [""] + [0] * nombre_docs_occurrences_mots

    # Adresse_valeur nombre occurrences d'un mot pour un doc donné
    ligne_mot = -1
    num_col_doc_courant = 0
    dico_correspondance_nom_doc_corpus_et_num_col = {}
    i = 0

    # contruction de la première ligne de la matrice qui est spéciale car elle contient
    # le titre de tous les fichiers cleaned du corpus (= toutes les clés des dicos nommé "les_dicos_occurrences_mots")
    for nom_dico_occurrences_mots_courant, dico_occurrences_mots in les_dicos_occurrences_mots.items():
        i += 1
        dico_correspondance_nom_doc_corpus_et_num_col[i] = nom_dico_occurrences_mots_courant
        # ligne_matrice_tf[i] = nom_dico_occurrences_mots_courant

    # ajouter dans la matrice tf cette première ligne spéciale contenant le nom des fichiers
    # matrice_tf.append(ligne_matrice_tf)

    # remplissage de la matrice
    for dico_courant_occurrences_mots in les_dicos_occurrences_mots.values():

        num_col_doc_courant += 1

        for mot, nombre_occurrences_mot in dico_courant_occurrences_mots.items():

            # ini data ligne matrice tf
            ligne_matrice_tf = [""] + [0] * nombre_docs_occurrences_mots

            # mot existant dans la matrice tf ?
            if num_col_doc_courant > 1:
                ligne_mot = lm.chercher_valeur_dans_liste_2D(matrice_tf, mot, matrice_tf_discours_presidents_num_col_mot)

            # le mot n'existe pas, l'ajouter dans la matrice tf
            if ligne_mot == -1:

                # ajouter une ligne dans matrice TF pour le nouveau mot;
                # mettre mot dans col matrice_tf_num_col_mot (0) et nombre_occurrences_mot dans col = num_doc en cours"

                # ajouter le mot dans la ligne de la matrice tf
                ligne_matrice_tf[matrice_tf_discours_presidents_num_col_mot] = mot

                # stockage nombre occurrences mot; col = num doc concerné (num_col_doc_courant)
                ligne_matrice_tf[num_col_doc_courant] = nombre_occurrences_mot

                # ajouter la nouvelle ligne dans la matrice tf
                matrice_tf.append(ligne_matrice_tf)

            # le mot existe, on ajoute le nombre d'occurrences trouvés pour ce mot dans ce doc
            else:
                matrice_tf[ligne_mot][num_col_doc_courant] = nombre_occurrences_mot

    return matrice_tf
def creer_matrice_idf(nom_dossier_cleaned):

    # 1) créer tous les dicos occurrences mots et les stocker dans un "dico de dicos"
    les_dicos_mots_docs = creer_tous_les_dicos_occurrences_mots(nom_dossier_cleaned)

    # 2) pour chaque dico, donc chaque fichier du corpus, savoir dans quel fichier il est présent
    matrice_presence_mots_dans_docs = []

    # Connaitre le nombre de colonnes nécessaires
    nombre_docs = len(les_dicos_mots_docs)

    # def d'une ligne de la matrice: col mot + n * col avec n = nbre docs occurences mots
    ligne_matrice_presence_mots_dans_doc = [""] + [0] * nombre_docs

    ligne_mot = -1
    num_col_doc_courant = 0
    i = 0

    # contruction de la première ligne de la matrice qui est spéciale car elle contient
    # le titre de tous les fichiers cleaned du corpus (= toutes les clés des dicos nommé "les_dicos_occurrences_mots")
    # for nom_dico_mots_doc_courant, dico_mots_doc_courant in les_dicos_mots_docs.items():
    #    i += 1
    #    ligne_matrice_presence_mots_dans_doc[i] = nom_dico_mots_doc_courant

    # ajouter dans la matrice cette première ligne spéciale contenant le nom des fichiers
    # matrice_presence_mots_dans_docs.append(ligne_matrice_presence_mots_dans_doc)

    # ini data ligne matrice idf
    ligne_matrice_presence_mots_dans_doc = [""] + [0] * nombre_docs

    # remplissage de la matrice
    for dico_mots_doc_courant in les_dicos_mots_docs.values():

        num_col_doc_courant += 1

        for mot in dico_mots_doc_courant.keys():

            # mot existant dans la matrice ?
            if num_col_doc_courant > 1:
                ligne_mot = lm.chercher_valeur_dans_liste_2D(matrice_presence_mots_dans_docs, mot, matrice_idf_discours_presidents_num_col_mot)

            # le mot n'existe pas, l'ajouter dans la matrice
            if ligne_mot == -1:

                # ajouter le mot dans la ligne de la matrice
                ligne_matrice_presence_mots_dans_doc[0] = mot

                # conserver l'info concernant l'existence de ce mot pour ce doc
                ligne_matrice_presence_mots_dans_doc[num_col_doc_courant] = mot_existant

                # ajouter la nouvelle ligne dans la matrice
                matrice_presence_mots_dans_docs.append(ligne_matrice_presence_mots_dans_doc)

            # le mot existe, on ajoute le nombre d'occurrences trouvés pour ce mot dans ce doc
            else:
                matrice_presence_mots_dans_docs[ligne_mot][num_col_doc_courant] = mot_existant

            # ini data ligne matrice idf
            ligne_matrice_presence_mots_dans_doc = [""] + [0] * nombre_docs

    # creation de la matrice idf (2 cols: mot et score idf)
    matrice_idf = []
    ligne_matrice_idf = [""] + [0]

    # pour chaque mot existant dans la matrice_presence_mots_dans_docs
    # trouver le nombre de fois ou ce mot est présent dans les docs et en faire le total
    nombre_total_de_docs_contenant_ce_mot = 0

    for i in range(len(matrice_presence_mots_dans_docs)):  # parcourir tous les mots
        for j in range(1, len(matrice_presence_mots_dans_docs[i])):  # parcourir chaque colonne
            # calcul du nombre total de docs dans lesquels figurent ce mot
            nombre_total_de_docs_contenant_ce_mot += matrice_presence_mots_dans_docs[i][j]

        mot = matrice_presence_mots_dans_docs[i][0]

        #  calculer le score idf et le stocker dans la matrice idf
        score_idf_mot = ma.log10(nombre_docs / nombre_total_de_docs_contenant_ce_mot)
        score_idf_mot = round(score_idf_mot, 2)

        ligne_matrice_idf = [mot] + [score_idf_mot]

        matrice_idf.append(ligne_matrice_idf)

        ligne_matrice_idf = [""] + [0]
        nombre_total_de_docs_contenant_ce_mot = 0

    return matrice_idf
def creer_matrice_tf_idf(nom_dossier_cleaned, les_dicos_occurrences_mots, matrice_tf, matrice_idf):

    if len(les_dicos_occurrences_mots) == 0:
        return

    # créer matrice TF d'après les dicos créés précedemment
    # matrice_tf = creer_matrice_tf(les_dicos_occurrences_mots)

    # créer matrice IDF
    # matrice_idf = creer_matrice_idf(nom_dossier_cleaned)

    # 4) créer effectivement la matrice tf_idf en fonction des matrices créées précedemment
    matrice_tf_idf = []
    ligne_matrice_tf_idf = []

    # parcourir la ligne de la matrice tf ET de la matrice idf.
    # rappel: les 2 matrices ont le même nombre de lignes (donc le même nombre de mots qui sont uniques)
    for i in range(len(matrice_tf)):

        ligne_matrice_tf_idf = []
        val_tf = 0
        val_idf = 0
        score_tf_idf = 0

        # stocker le mot courant
        ligne_matrice_tf_idf = [matrice_tf[i][matrice_tf_discours_presidents_num_col_mot]]

        # stocker le score idf de ce mot
        val_idf = matrice_idf[i][matrice_tf_num_col_score_idf]

        # parcourir toutes les valeurs ( de tous les docs) de la matrice tf et * par
        # le score idf afin d'obtenir le score tf-idf du mot (on le fait pour chaque doc,
        # donc pr chaque colonnes de la matrice tf)
        for j in range(1, len(matrice_tf[i])):

            # stocker le score tf-idf pour ce mot, pour le doc courant X
            val_tf = matrice_tf[i][j]
            score_tf_idf = val_tf * val_idf
            score_tf_idf = round(score_tf_idf, 2)
            ligne_matrice_tf_idf += [score_tf_idf]

        matrice_tf_idf.append(ligne_matrice_tf_idf)

    return matrice_tf_idf
def transpose_matrice(matrice):

    # DE: Deplacer cette fonction dans un fichier matrices_manager.py ?

    matrice_transposee = []
    ligne_matrice = []
    ligne_matrice_transposee = []
    cur_col = 0
    cur_ligne = 0

    ##########################################################################################
    # ici: creer les ligne docs de la matrice transposee d'apres les docs présents dans le dico
    #
    # Les lignes de la matrice transposee contiennent les docs 1 à N
    #
    # Les colonnes de la matrice reversed contiennent les mots du corpus
    ##########################################################################################

    # a ce stade, nous avons une matrice transposee contenant le nombre de lignes voulues
    # leur nombre correspondant au nombre de docs existants

    # ajouter toutes les colonnes (mots) dans la matrice transposee
    for ligne in range(len(matrice)):
         mot = matrice[ligne][0]
         ligne_matrice_transposee += [mot]

    # ajouter la première ligne à la matrice transposée (tous les mots)
    matrice_transposee.append(ligne_matrice_transposee)

    # ajout le nombre de lignes requis à la matrice transposée (= nombre de colonnes de la matrice d'origine)
    ligne_matrice_transposee = []
    for ligne in range(1, len(matrice[0])):
        ligne_matrice_transposee = [0] * len(matrice)
        matrice_transposee.append(ligne_matrice_transposee)
        ligne_matrice_transposee = []

    # a ce stade, on a la matrice reversed "formée" avec lignes et colonnes,
    # et avec les mots dans chaque colonne de la ligne 0.
    # Il n'y a pas de valeurs pour le moment. on va donc chercher ces valeurs pour les remplir

    # (pour une colonne (un mot donné), trouver les valeurs col 1 à col n (doc 1 à doc n)
    for ligne in range(len(matrice)):
        for colonne in range(1, len(matrice[ligne])):
            ligne_matrice += [matrice[ligne][colonne]]

        # a ce stade on a une ligne renseignée avec val ayant cette forme
        # mot x | doc 1 | doc 2 | doc x
        # mettre ces valeurs dans la matrice transposée. les lignes contiennent les docs et les col contiennent les mots
        cur_ligne = 1

        for i in range(len(ligne_matrice)):
            cur_val = ligne_matrice[i]
            matrice_transposee[cur_ligne][cur_col] = cur_val
            cur_ligne += 1

        ligne_matrice = []
        cur_col += 1

    return matrice_transposee
def ini_matrice_tf_idf_question(matrice_tf_idf_corpus_transposee):

    matrice_tf_idf_question = []

    matrice_tf_idf_question.append(copy.deepcopy(matrice_tf_idf_corpus_transposee[matrice_tf_idf_corpus_transposee_num_ligne_mot]))

    # ajouter la ligne qui contiendra les score tf-idf pour les mots de la question (ini à "0" pour le moment)
    ligne_vierge = [0] * len(matrice_tf_idf_corpus_transposee[0])
    matrice_tf_idf_question.append(ligne_vierge)

    return matrice_tf_idf_question
def creer_vecteur_tf_idf_question(question, vecteur_tf_idf_question, matrice_idf_corpus):

    liste_mots_question = question.split(" ")
    score_idf = 0

    # pour chaque mot de la question,
    for i in range(len(liste_mots_question)):
        mot = liste_mots_question[i]
        # ...verifier si ce mot est inclus dans le corpus, donc dans une des col de matrice_tf_idf_question
        if mot in vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_mot]:
            # le mot existe, le localiser
            for j in range(len(vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_mot])):
                # incrémenter le tf du mot dans le vecteur de la question
                if (vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_mot][j] == mot):
                    vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_score_tf_idf][j] += 1
                    j = 0
                    break

    # calcul du vecteur TF-IDF de la question: Celui-ci s'obtient en multipliant le tf de la question
    # par le score IDF des mots du corpus
    i = 0
    for i in range(len(liste_mots_question)):
        mot = liste_mots_question[i]
        x = 0
        n = 0
        score_idf = -1
        # chercher ce mot dans la matrice_idf_corpus pour trouver son score IDF
        for x in range(len(matrice_idf_corpus)):
            if score_idf != -1: break
            if matrice_idf_corpus[x][matrice_tf_idf_corpus_num_ligne_mot] == mot:
                # score idf du mot localisé
                score_idf = matrice_idf_corpus[x][matrice_tf_idf_corpus_num_ligne_score]
                # calculer le tf-idf du mot en multipliant son tf par le score idf trouvé
                for n in range(len(vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_mot])):
                    # DE: A corriger ! : Remplacer par matrices_manager.trouver_num_col(matrice, num_ligne, val_a_chercher)
                    if vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_mot][n] == mot:
                        vecteur_tf_idf_question[vecteur_tf_idf_question_num_ligne_score_tf_idf][n] *= score_idf
                        n = 0
                        x = 0
                        break

    return vecteur_tf_idf_question
def obtenir_mot_avec_score_tf_idf_le_plus_eleve(vecteur_question):

    mot_significatif = ""
    score_mot_significatif = 0

    num_ligne_mots = vecteur_tf_idf_question_num_ligne_mot
    num_ligne_valeur = vecteur_tf_idf_question_num_ligne_score_tf_idf

    for num_col in range(len(vecteur_question[num_ligne_valeur])):
        if vecteur_question[num_ligne_valeur][num_col] > score_mot_significatif:
            score_mot_significatif = vecteur_question[num_ligne_valeur][num_col]
            mot_significatif = vecteur_question[num_ligne_mots][num_col]

    return mot_significatif
