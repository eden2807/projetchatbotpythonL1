import presidents as les_presidents
import string_manager as sm
import TF_IDF as tf_idf
import  traitement_question_reponse as tt_question_reponse
import tkinter as tk
import math_vecteurs as math_vect
from gui_manager import *
from tkinter import *

# region def des elements UI
window_width = 800
window_height = 500
label_height = 2

# fenetre principale
window = creer_fenetre("ChatBot", window_width, window_height)

label_invite_choix_stats_mots_corpus = Label(window) # relief=RAISED

# frame conteneur de la listbox
frame_list_box = Frame(window)

police = ("Arial", 12)

listbox_questions_sur_stats_mots_corpus = tk.Listbox(frame_list_box, font=police)

label_info_ou = Label(window, relief=RAISED)

textbox_question = Text(window, width=window_width, height=4, font=30, background="lightblue",
                        foreground="black")

label_info_reponse = Label(window)  # relief=RAISED

textbox_reponse = Text(window, width=window_width, height=10, font=30, background="peachpuff",
                       foreground="firebrick")

# endregion def des elements UI

#region "Commandes du menu"
def afficher_ui_infos_stats_mots_corpus():

    # preparer l'ui
    #frame_list_box.pack_forget()

    return

def afficher_ui_poser_question():

    # preparer l'ui
    #frame_list_box.pack()

    return

def quitter():

    window.quit()

    return

#endregion "Commandes du menu"

def chercher_infos_stats_mots_corpus(index_requete):

    #les_presidents.dico_questions_stat_mots_corpus

    return

def on_listbox_stat_mots_corpus_click(event):

    # Obtenir l'index de l'élément sélectionné
    selected_index = listbox_questions_sur_stats_mots_corpus.curselection()

    # Obtenir le texte de l'élément sélectionné
    selected_text = listbox_questions_sur_stats_mots_corpus.get(selected_index)

    return
def getText():

    # recuperer la question posée par user
    res = textbox_reponse.get("1.0", "end")

    print(res)

    return
def creer_ui(dico_questions_stat_mots_corpus):

    window.config(background="peachpuff")

    ###############################################################
    # region creation du menu
    menuBar = Menu(window)

    # Création du menu principal 'Programme'
    menuFichier = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Programme", menu=menuFichier)

    # Création des sous menus :
    menuFichier.add_command(label="Infos et stats sur les discours", command=afficher_ui_infos_stats_mots_corpus)
    menuFichier.add_command(label="Poser une question", command=afficher_ui_poser_question)
    menuFichier.add_command(label="Quitter", command=quitter)
    # Configuration de la barre des menus
    window.config(menu=menuBar)

    # endregion création du menu
    ###############################################################

    ####################################################################
    # region label invite choix stats mots corpus
    label_invite_choix_stats_mots_corpus.config(text="Cliquez sur un des choix disponibles :", anchor="w")
    label_invite_choix_stats_mots_corpus.config(width=window_width)
    label_invite_choix_stats_mots_corpus.config(height=2)
    label_invite_choix_stats_mots_corpus.config(font=36)
    label_invite_choix_stats_mots_corpus.config(font=36)
    label_invite_choix_stats_mots_corpus.config(background="firebrick")
    label_invite_choix_stats_mots_corpus.config(foreground="peachpuff")
    label_invite_choix_stats_mots_corpus.pack(padx=4, pady=4)
    # endregion label invite choix stats mots corpus
    ####################################################################

    ####################################################################
    # Création de la liste de de choix de stats des mots des presidents
    ####################################################################
    # conteneur de la listbox
    #frame_list_box = Frame(window)
    frame_list_box.pack()

    # DE: A corriger !
    # Remplacer les choix des stats mot du corpus par un fichier
    # voir le param passé à cette fonction.
    # mettre les fonctions de recherche dans le module "presidents"
    # listbox_stat_mots_corpus = Listbox(frame_list_box, font=police)
    listbox_questions_sur_stats_mots_corpus.config(width=85, height=6)
    listbox_questions_sur_stats_mots_corpus.config(background="peachpuff")
    listbox_questions_sur_stats_mots_corpus.config(foreground="firebrick")
    listbox_questions_sur_stats_mots_corpus.insert(1, "Afficher les mots les MOINS importants dans les discours des présidents")
    listbox_questions_sur_stats_mots_corpus.insert(2, "Afficher les mots les PLUS importants dans les discours des présidents")
    listbox_questions_sur_stats_mots_corpus.insert(3, "Trouver les mots significatifs les plus répétés par J. Chirac")
    listbox_questions_sur_stats_mots_corpus.insert(4, "Indiquer le nom des présidents ayant parlés de la Nation ainsi que celui qui en a le plus parlé")
    listbox_questions_sur_stats_mots_corpus.insert(5, "Montrer qui a parler du climat et/ou de l'écologie")
    listbox_questions_sur_stats_mots_corpus.bind("<ButtonRelease-1>", on_listbox_stat_mots_corpus_click)

    # Création de la barre de défilement de la listbox
    scrollbar = Scrollbar(frame_list_box, command=listbox_questions_sur_stats_mots_corpus.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurer la Listbox pour utiliser la barre de défilement
    listbox_questions_sur_stats_mots_corpus.config(yscrollcommand=scrollbar.set)
    listbox_questions_sur_stats_mots_corpus.pack(padx=4)

    # Fin listbox_questions_sur_stats_mots_corpus
    ####################################################################

    # label info "ou:"
    label_info_ou.config(text="...Ou saisissez votre question ci-dessous et appuyez sur la touche Entrée : ", anchor="w")
    label_info_ou.config(width=window_width)
    label_info_ou.config(height=label_height)
    label_info_ou.config(font=36)
    label_info_ou.config(background="firebrick")
    label_info_ou.config(foreground="peachpuff")
    label_info_ou.pack(padx=4, pady=2)

    textbox_question.pack(padx=4, pady=2)

    # label info "Réponse:"
    label_info_reponse.config(text="Réponse :", anchor="w")
    label_info_reponse.config(width=window_width)
    label_info_reponse.config(height=2)
    label_info_reponse.config(font=36)
    label_info_reponse.config(background="firebrick")
    label_info_reponse.config(foreground="peachpuff")
    label_info_reponse.pack(padx=4, pady=2)

    # textbox permettant la saisie d'une question par user
    #textbox_reponse = Text(window, width=window_width, height=10, font=30, background="peachpuff",
    #                       foreground="firebrick")
    textbox_reponse.pack(padx=4, pady=2)

    window.mainloop()

    return

def main():

    # obtenir les fichiers des discours des presidents
    les_presidents.noms_fichiers_discours_presidents = les_presidents.obtenir_nom_fichiers_discours_presidents(les_presidents.dossier_discours_presidents)

    # obtenir le nom et le prénom des présidents
    prenom_nom_des_presidents = les_presidents.obtenir_liste_prenom_nom_des_presidents(les_presidents.noms_fichiers_discours_presidents)

    # Convertir les fichiers des discours des présidents en minuscules et les stocker dans le dossier "cleaned"
    sm.convertir_texte_en_minuscules(les_presidents.noms_fichiers_discours_presidents, les_presidents.dossier_discours_presidents_nettoyes)
    # Nettoyer les fichiers des discours des présidents
    sm.nettoyer_textes_du_dossier(les_presidents.dossier_discours_presidents_nettoyes)

    # Obtenir les dicos d'occurrences de mots des discours des présidents
    tf_idf.les_dicos_occurrences_mots_corpus = tf_idf.creer_tous_les_dicos_occurrences_mots(les_presidents.dossier_discours_presidents_nettoyes)

    # créer matrice TF d'après les dicos créés précedemment
    tf_idf.matrice_tf_corpus = tf_idf.creer_matrice_tf(tf_idf.les_dicos_occurrences_mots_corpus)

    # créer matrice IDF des mots des discours des présidents
    tf_idf.matrice_idf_corpus = tf_idf.creer_matrice_idf(les_presidents.dossier_discours_presidents_nettoyes)

    # Creation de la matrice tf-idf des mots des discours des présidents
    # Lignes = mots (unique) du corpus
    # Colonnes = docs de 1 à n
    tf_idf.matrice_tf_idf_corpus = tf_idf.creer_matrice_tf_idf(les_presidents.dossier_discours_presidents_nettoyes, tf_idf.les_dicos_occurrences_mots_corpus, tf_idf.matrice_tf_corpus, tf_idf.matrice_idf_corpus)

    # Transposition de la matrice tf-idf des mots des discours des présidents
    # Lignes = docs de 1 à n
    # Colonnes = mots (unique) du corpus
    tf_idf.matrice_tf_idf_corpus_transposee = tf_idf.transpose_matrice(tf_idf.matrice_tf_idf_corpus)

    # TEST SEULEMENT:

    # Une question a été posé par user:

    # 1) Nettoyer la question
    question = "Quel présidents l'année en cours qu'aurait pu être présidents et qu'on a vu concerné par le climat parle le plus du climat dans son discours"
    question = sm.nettoyer_texte(question)

    # 2) creer le vecteur tf_idf_question par copie de la matrice_tf_idf_corpus_transposee.
    # Elle contient uniquement 2 lignes (mots du corpus et score tf-idf de ces mots)
    # et M colonnes (nbre total de mots)
    tf_idf.vecteur_tf_idf_question = tf_idf.ini_matrice_tf_idf_question(tf_idf.matrice_tf_idf_corpus_transposee)

    # 3) créer le vecteur_tf_idf_question
    tf_idf.vecteur_tf_idf_question = tf_idf.creer_vecteur_tf_idf_question(question, tf_idf.vecteur_tf_idf_question, tf_idf.matrice_idf_corpus)

    # 4) calcul du produit scalaire entre matrice_tf_idf_question et matrice_tf_idf_corpus_transposee[ligne]
         # (ici en test, mais il faudra le faire systématiquement pour chaque doc dans matrice_tf_idf_corpus_transposee)
    vecteur_scalaire = 0
    num_doc = 1
    vecteur_scalaire = math_vect.calculer_produit_scalaire_vecteurs(tf_idf.vecteur_tf_idf_question[tf_idf.matrice_tf_idf_question_num_ligne_score_tf_idf], tf_idf.matrice_tf_idf_corpus_transposee[num_doc])

    # 5) calcul de la norme d'un vecteur
    norme_vecteur = 0
    norme_vecteur = math_vect.calculer_norme_vecteur(tf_idf.vecteur_tf_idf_question[tf_idf.matrice_tf_idf_question_num_ligne_score_tf_idf])

    # 6) trouver le doc le plus pertinent à la question posée
    num_doc_pertinent = tt_question_reponse.trouver_doc_le_plus_pertinent_a_question(tf_idf.vecteur_tf_idf_question, tf_idf.matrice_tf_idf_corpus_transposee, les_presidents.noms_fichiers_discours_presidents)

    #nom_doc_pertinent = obtenir_nom_doc(num_doc_pertinent)

    # FIN TEST SEULEMENT

    les_presidents.dico_des_questions_sur_stats_mots_corpus = les_presidents.remplir_dico_avec_questions_stat_mots_corpus()

    # note importante: toujours creer l'ui à la fin du process car des que la boucle de window est créée
    # on sort de celui ci et le reste du code situé après la création de l'ui n'est plus executé
    creer_ui(les_presidents.dico_des_questions_sur_stats_mots_corpus)

main()