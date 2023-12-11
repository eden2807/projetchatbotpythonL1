import string

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
import os
import math

def calculer_idf(corpus_directory):
    mots_par_document = {}  # Dictionnaire pour stocker les mots présents dans chaque document
    total_documents = 0  # Compteur du nombre total de documents dans le corpus

    # Parcours de tous les fichiers dans le répertoire du corpus
    for filename in os.listdir(corpus_directory):
        if filename.endswith(".txt"):
            with open(os.path.join(corpus_directory, filename), 'r', encoding='utf-8') as file:
                document = file.read()
                mots = set(document.split())  # Utilisation d'un ensemble pour obtenir les mots uniques dans le document
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
