import os
import math
import string_manager as sm

matrice_TF_num_col_mot = 0

def creer_dico_occurences_mots(texte):

    dico_nombre_occurences_mots = {}

    nombre_occurences_mot: int

    liste_mots_texte = []

    liste_mots_uniques = []

    # transformer le texte en liste
    liste_mots_texte = sm.transformer_texte_en_liste(texte)

    # parcourir cette liste de mots et comptabiliser le nombre d'occurences de chacun d'entre eux
    for mot in liste_mots_texte:

        if mot not in liste_mots_uniques:

            # se souvenir du mot afin de ne le traiter qu'une seule et unique fois
            liste_mots_uniques.append(mot)

            # chercher le nombre d'occurences de ce mots dans la liste contenant le texte entier
            nombre_occurences_mot = liste_mots_texte.count(mot)

            # stocker le nombre d'occurences de ce mots
            dico_nombre_occurences_mots[mot] = nombre_occurences_mot

    return  dico_nombre_occurences_mots

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
