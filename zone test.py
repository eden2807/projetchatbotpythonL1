import os
import main as m
import TF_IDF as tf_idf
def main():

    # Détails des étapes de création de la matrice TF:

    # 1) creer tous les dicos occurrences mots et les stocker dans un "dico de dicos"
    les_dicos_occurrences_mots = tf_idf.creer_tous_les_dicos_occurrences_mots(m.nom_dossier_cleaned)

    if len(les_dicos_occurrences_mots) == 0:
        return "Erreur, aucuns dictionnaires d'occurrences de mots n'a été trouvés !"

    # 2) creer matrice TF d'après les dicos créés précedemment
    #matrice_TF = creer_matrice_tf(les_dicos_occurrences_mots)

    return


    return

main()