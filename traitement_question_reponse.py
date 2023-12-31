import string_manager as sm
import TF_IDF as tf_idf

question = "Quel président l'année en cours qu'aurait pu être et qu'on a vu concerné par le climat parle le plus du climat dans son discours"

matrice_idf_transposee = question.split(" ")
question = sm.nettoyer_texte(question)

matrice_tf_idf_question = tf_idf.score_tf_idf_question(question, matrice_idf_transposee)
