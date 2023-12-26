import os
import math
import string_manager as sm
import lists_manager as lm


matrice_TF_num_col_mot = 0

def creer_dico_occurences_mots(texte):

    dico_nombre_occurences_mots = {}

    # transformer le texte en liste
    liste_mots_texte = sm.transformer_texte_en_liste(texte)

    # parcourir cette liste de mots et comptabiliser le nombre d'occurences de chacun d'entre eux
    for mot in liste_mots_texte:

        if mot not in dico_nombre_occurences_mots.keys():

            # chercher le nombre d'occurences de ce mots dans la liste contenant le texte entier
            nombre_occurences_mot = liste_mots_texte.count(mot)

            # stocker le nombre d'occurences de ce mots
            dico_nombre_occurences_mots[mot] = nombre_occurences_mot

    return  dico_nombre_occurences_mots
def creer_tous_les_dicos_occurrences_mots(dossier_fichiers, extension_fichiers = ".txt"):

    les_dicos_occurrences_mots = {}
    dico_nombre_occurences_mots = {}

    # parcourir tous les fichiers dispos dans dossier_fichiers
    for nom_fichier in os.listdir(dossier_fichiers):

        if nom_fichier.endswith(extension_fichiers):

            # assembler le chemin complet du fichier (path dossiers + nom fichier)
            chemin_fichier = os.path.join(dossier_fichiers, nom_fichier)

            # Lire le contenu du fichier
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                texte = f.read()

            # creer le dico d'occurrences de mots
            dico_nombre_occurences_mots = creer_dico_occurences_mots(texte)

            # le stocker dans le dico des dicos d'occurrences de mots
            les_dicos_occurrences_mots[nom_fichier] = dico_nombre_occurences_mots

    return les_dicos_occurrences_mots
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
        idf[mot] = math.log(total_documents / (1 + occurrences))  # Ajout de 1 pour éviter la division par zéro

    return idf
def creer_matrice_tf(les_dicos_occurrences_mots):

    # def d'une ligne composant la matrice TF
    # La ligne 0 de la matrice est une ligne particulière: col 0 = vide, cols suivantes:
    # Elle contient le nom des docs dans l'ordre des dicos placés dans le dico "les_dicos_occurrences_mots"
    # Détails des lignes suivantes: col 0 = mot, col suivantes = nbre occurrences mot dans les différents docs
    # existants, suivant leur colonnes propres.
    # Note: Il doit donc y avoir autant de colonnes que de docs, chaque doc possedant son propre
    # dictionnaire d'occurrences de mots.

    # La matrice TF est une liste 2D
    matrice_TF = []

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
        dico_correspondance_nom_doc_corpus_et_num_col[nom_dico_occurrences_mots_courant] = i
        ligne_matrice_tf[i] = nom_dico_occurrences_mots_courant

    # ajouter dans la matrice TF cette première ligne spéciale contenant le nom des fichiers
    matrice_TF.append(ligne_matrice_tf)

    # remplissage de la matrice
    for dico_courant_occurrences_mots in les_dicos_occurrences_mots.values():

        num_col_doc_courant += 1

        for mot, nombre_occurrences_mot in dico_courant_occurrences_mots.items():

            # ini data ligne matrice TF
            ligne_matrice_tf = [""] + [0] * nombre_docs_occurrences_mots

            # mot existant dans la matrice TF ?
            if num_col_doc_courant > 1:
                ligne_mot = lm.chercher_valeur_dans_liste_2D(matrice_TF, mot, matrice_TF_num_col_mot)

            # le mot n'existe pas, l'ajouter dans la matrice TF
            if ligne_mot == -1:
                # ajouter une ligne dans matrice TF pour le nouveau mot;
                # mettre mot dans col matrice_TF_num_col_mot (0) et nombre_occurrences_mot dans col = num_doc en cours"

                # ajouter le mot dans la ligne de la matrice TF
                ligne_matrice_tf[matrice_TF_num_col_mot] = mot

                # stockage nombre occurrences mot; col = num doc concerné (num_col_doc_courant)
                ligne_matrice_tf[num_col_doc_courant] = nombre_occurrences_mot

                # ajouter la nouvelle ligne dans la matrice TF
                matrice_TF.append(ligne_matrice_tf)

            # le mot existe, on ajoute le nombre d'occurrences trouvés pour ce mot dans ce doc
            else:
                matrice_TF[ligne_mot][num_col_doc_courant] = nombre_occurrences_mot
    return



