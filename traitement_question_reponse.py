import string_manager as sm
import TF_IDF as tf_idf
import math_vecteurs as math_vect

def trouver_doc_le_plus_pertinent_a_question(vecteur_tf_idf_question, matrice_tf_idf_corpus_transposee,
                                             noms_fichiers_discours_presidents):

    return

    # pour chaque fichiers du corpus dans la matrice
    for num_doc in range(len(noms_fichiers_discours_presidents)):
        math_vect.calcul_similarite_vecteurs(vecteur_tf_idf_question[tf_idf.matrice_tf_idf_question_num_ligne_score_tf_idf],
                                             matrice_tf_idf_corpus_transposee[num_doc])


    return
