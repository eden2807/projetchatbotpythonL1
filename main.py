import presidents as les_presidents
import string_manager as sm
import TF_IDF as tf_idf
import traitement_question_reponse as tt_q_r
import traitement_questions_reponses as tt_quest_rep
import tkinter as tk
import math_vecteurs as math_vect
from gui_manager import *
from tkinter import *
from tkinter import messagebox

# region def des elements UI
window_width = 800
window_height = 500
label_height = 2

# fenetre principale
window = creer_fenetre("ChatBot", window_width, window_height)

label_invite_choix_stats_mots_corpus = Label(window, relief=RAISED)

# frame conteneur de la listbox
frame_list_box = Frame(window)

police = ("Arial", 12)

listbox_questions_sur_stats_mots_corpus = tk.Listbox(frame_list_box, font=police)

label_info_ou = Label(window, relief=RAISED)

textbox_question = Text(window, width=window_width, height=4, font=30, wrap='word', background="white",
                        foreground="black")

label_info_reponse = Label(window, relief=RAISED)

# frame conteneur de la textbox_reponse
frame_textbox_reponse = Frame(window)

textbox_reponse = Text(window, width=window_width, height=10, font=30, wrap='word', background="peachpuff",
                       foreground="firebrick")

# endregion def des elements UI

#region "Commandes du menu"
def ini_ui_infos_stats_mots_corpus():

    # demander si user est ok pour l'effacer
    reponse = messagebox.showinfo("Information",
                                     "Veuillez selectionner un des choix disponibles dans la liste")

    textbox_question.delete("1.0", tk.END)
    textbox_reponse.delete("1.0", tk.END)

    return
def ini_ui_pour_poser_question():

    contenu = textbox_question.get("1.0", "end-1c")

    # si la textbox question contient quelque chose
    if contenu != "":

        # demander si user est ok pour l'effacer
        reponse = messagebox.askquestion("Question", "Effacer l'ancienne question afin de poser une nouvelle question ?")

        if reponse == 'yes':
            textbox_question.delete("1.0", tk.END)
            textbox_reponse.delete("1.0", tk.END)

    # selectionner la texbox (donner le focus afin d'être prêt à saisir la new question)
    textbox_question.focus_set()

    return
def quitter():
    window.destroy()

#endregion "Commandes du menu"

def traitement_question_sur_stat_mots_corpus(num_question):

    reponse_complete = ""

    # effacer le contenu de la textbox reponse
    textbox_reponse.delete("1.0", tk.END)

    # obtenir la réponse selon la question selectionnée par l'utilisateur
    reponse = tt_quest_rep.obtenir_reponse_sur_stats_mots_corpus(num_question)

    # afficher la réponse progressivement, façon chatGPT, + ou - vite selon le type de question posée
    if num_question == 2 or num_question == 3:
        sm.afficher_texte_progressivement(reponse, textbox_reponse, 0.02, 150)
    else:
        sm.afficher_texte_progressivement(reponse, textbox_reponse)

    return
def on_listbox_questions_sur_stats_mots_corpus_click(event):

    # Obtenir l'index de l'élément sélectionné
    selected_index = listbox_questions_sur_stats_mots_corpus.curselection()

    # Obtenir le texte de l'élément sélectionné
    selected_text = listbox_questions_sur_stats_mots_corpus.get(selected_index)

    # récupération de l'indice dans le tuple et conversion en int afin de pouvoir incrémenter
    num_question = selected_index[0]

    # ne pas considerer une question 0, mais toujours commencer par la question 1
    num_question += 1

    traitement_question_sur_stat_mots_corpus(num_question)

    return
def traitement_question_utilisateur_et_affichage_reponse(question):

    # chercher la réponse à la question de l'utilisateur
    reponse = tt_quest_rep.traitement_question_utilisateur(question)

    # afficher la réponse façon chatGPT:
    sm.afficher_texte_progressivement(reponse, textbox_reponse)

    return
def on_textbox_question_enter_pressed(event):

    question = textbox_question.get("1.0", "end-1c")

    # la question ne contient pas de caracteres alphanumérique, avertir l'utilisateur
    if len(question.strip()) == 0:
        messagebox.showinfo("Information", "La question n'a pas été correctement saisie")
        return

    # effacer la réponse précédente
    textbox_reponse.delete("1.0", tk.END)

    # traiter la question de l'utilisateur et renvoyer la réponse
    traitement_question_utilisateur_et_affichage_reponse(question)

    return


def creer_ui():

    window.config(background="peachpuff")

    ###############################################################
    # region creation du menu
    menuBar = Menu(window)

    # Création du menu principal 'Programme'
    menuFichier = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Programme", menu=menuFichier)

    # Création des sous menus :
    #menuFichier.add_command(label="Infos et stats sur les discours", command=ini_ui_infos_stats_mots_corpus)
    menuFichier.add_command(label="Choisir une question pré-établie", command=ini_ui_infos_stats_mots_corpus)
    menuFichier.add_command(label="Poser une question", command=ini_ui_pour_poser_question)
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

    listbox_questions_sur_stats_mots_corpus.config(width=85, height=6)
    listbox_questions_sur_stats_mots_corpus.config(background="peachpuff")
    listbox_questions_sur_stats_mots_corpus.config(foreground="firebrick")
    listbox_questions_sur_stats_mots_corpus.insert(1, "Afficher les mots les MOINS importants dans les discours des présidents")
    listbox_questions_sur_stats_mots_corpus.insert(2, "Afficher les mots les PLUS importants dans les discours des présidents")
    listbox_questions_sur_stats_mots_corpus.insert(3, "Trouver les mots significatifs les plus répétés par J. Chirac")
    listbox_questions_sur_stats_mots_corpus.insert(4, "Indiquer le nom des présidents ayant parlés de la Nation ainsi que celui qui en a le plus parlé")
    listbox_questions_sur_stats_mots_corpus.insert(5, "Montrer qui a parlé du climat et/ou de l'écologie")
    listbox_questions_sur_stats_mots_corpus.bind("<ButtonRelease-1>", on_listbox_questions_sur_stats_mots_corpus_click)

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
    # appel de la fonction lors de l'appuie sur la touche "Entrée"
    textbox_question.bind('<Return>', on_textbox_question_enter_pressed)

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

    tf_idf.ini += 1

    if tf_idf.ini == 2:
        return

    # obtenir les fichiers des discours des presidents
    les_presidents.liste_noms_fichiers_discours_presidents = les_presidents.obtenir_nom_fichiers_discours_presidents(les_presidents.dossier_discours_presidents)

    les_presidents.nombre_docs_fichiers_discours_presidents = len(les_presidents.liste_noms_fichiers_discours_presidents)

    # remplir le dico avec les noms des fichiers du corpus et les numéroter en s'affranchissant de la base 0
    les_presidents.remplir_dico_fichiers_discours_presidents_depuis_la_liste(les_presidents.liste_noms_fichiers_discours_presidents)

    # obtenir le nom et le prénom des présidents
    prenom_nom_des_presidents = les_presidents.obtenir_liste_prenom_nom_des_presidents(les_presidents.liste_noms_fichiers_discours_presidents)

    # Convertir les fichiers des discours des présidents en minuscules et les stocker dans le dossier "cleaned"
    sm.convertir_texte_en_minuscules(les_presidents.liste_noms_fichiers_discours_presidents, les_presidents.dossier_discours_presidents_nettoyes)
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

    # remplir les phrases d'intro que l'on mettra avant de livrer les réponses aux utilisateurs
    tt_quest_rep.remplir_dico_intro_avant_reponse_trouvee()

    # note importante: toujours creer l'ui à la fin du process car des que la boucle de window est créée
    # on sort de celui-ci et le reste du code situé après la création de l'ui n'est plus executé
    creer_ui()

    return

main()