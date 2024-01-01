import presidents as les_presidents
import string_manager as sm
import TF_IDF as tf_idf
import tkinter as tk
from gui_manager import *
from tkinter import *

def creer_ui():

    window_width = 800
    window_height = 400

    window = creer_fenetre("ChatBot", window_width, window_height)
    window.config(background="peachpuff")

    ####################################################################
    # creation du_menu
    ####################################################################
    # creation du menu
    menuBar = Menu(window)

    # Création du menu principal 'Programme'
    menuFichier = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Programme", menu=menuFichier)

    # Création des sous menus :
    menuFichier.add_command(label="Commandes diverses", command="")
    menuFichier.add_command(label="Poser votre question")
    menuFichier.add_command(label="Quitter")
    # Configuration de la barre des menus
    window.config(menu=menuBar)
    ####################################################################
    # Fin de la création du menu
    ####################################################################

    ####################################################################
    # Création du label de présentation des questions
    ####################################################################
    var = StringVar()
    label = Label(window) # relief=RAISED
    label.config(text="Cliquez sur une des entrées disponibles ci-dessous :", anchor="w")
    label.config(width=window_width)
    label.config(height=2)
    label.config(font=36)
    label.config(font=36)
    label.config(background="firebrick")
    label.config(foreground="peachpuff")
    label.pack(padx=4, pady=4)
    ####################################################################
    # Fin de la création du label de présentation des questions
    ####################################################################

    ####################################################################
    # Création de la liste des questions pré-établies
    ####################################################################

    # conteneur de la listbox
    frame_list_box = Frame(window)
    frame_list_box.pack()

    police = ("Arial", 12)

    listbox_questions_preetablies = Listbox(frame_list_box, font=police)
    listbox_questions_preetablies.config(width=85, height=6)
    listbox_questions_preetablies.config(background="peachpuff")
    listbox_questions_preetablies.config(foreground="firebrick")
    listbox_questions_preetablies.insert(1, "Afficher la liste des mots les moins importants dans le corpus")
    listbox_questions_preetablies.insert(2, "Question 2")
    listbox_questions_preetablies.insert(3, "Question 3")
    listbox_questions_preetablies.insert(4, "Question 4")
    listbox_questions_preetablies.insert(5, "Question 5")
    listbox_questions_preetablies.insert(6, "Question 6")
    listbox_questions_preetablies.insert(7, "Question 7")
    listbox_questions_preetablies.insert(8, "Question 8")

    # Création de la barre de défilement de la listbox
    scrollbar = Scrollbar(frame_list_box, command=listbox_questions_preetablies.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurer la Listbox pour utiliser la barre de défilement
    listbox_questions_preetablies.config(yscrollcommand=scrollbar.set)
    listbox_questions_preetablies.pack(padx=4)

    ####################################################################
    # Fin de la création de la listbox de questions pré-établies
    ####################################################################

    # label "Réponse:"
    var = StringVar()
    label = Label(window)  # relief=RAISED
    label.config(text="Réponse :", anchor="w")
    label.config(width=window_width)
    label.config(height=2)
    label.config(font=36)
    label.config(font=36)
    label.config(background="firebrick")
    label.config(foreground="peachpuff")
    label.pack(padx=4, pady=2)

    # textbox permettant la saisie d'une question par user
    def getText():
        # recuperer la question posée par user
        res = textbox_reponse.get("1.0", "end")
        print(res)

    textbox_reponse = Text(window, width=window_width, height=10, font=30, background="peachpuff", foreground="firebrick")
    textbox_reponse.pack(padx=4, pady=2)

    #NewY = textbox_reponse.winfo_y() + 172
    #textbox_reponse.place(y=NewY)

    # bouton pour poser la question
    # button_poser_question = Button(window, font=24, height=2, width=30, text="Poser la question !", command=getText)
    # button_poser_question.pack(pady=20)

    window.mainloop()

    return
def main():

    # obtenir les fichiers des discours des presidents
    les_presidents.fichiers_discours_presidents = les_presidents.obtenir_fichiers_discours_presidents(les_presidents.dossier_discours_presidents)

    # obtenir le nom et le prénom des présidents
    prenom_nom_des_presidents = les_presidents.obtenir_liste_prenom_nom_des_presidents(les_presidents.fichiers_discours_presidents)

    # Convertir les fichiers des discours des présidents en minuscules et les stocker dans le dossier "cleaned"
    sm.convertir_texte_en_minuscules(les_presidents.fichiers_discours_presidents, les_presidents.dossier_discours_presidents_nettoyes)
    sm.nettoyer_texte(les_presidents.dossier_discours_presidents_nettoyes)

    # Obtenir les dicos d'occurrences de mots des discours des présidents
    tf_idf.les_dicos_occurrences_mots = tf_idf.creer_tous_les_dicos_occurrences_mots(les_presidents.dossier_discours_presidents_nettoyes)

    # créer matrice TF d'après les dicos créés précedemment
    tf_idf.matrice_tf_discours_presidents = tf_idf.creer_matrice_tf(tf_idf.les_dicos_occurrences_mots)

    # créer matrice IDF des mots des discours des présidents
    tf_idf.matrice_idf_discours_presidents = tf_idf.creer_matrice_idf(les_presidents.dossier_discours_presidents_nettoyes)

    # Creation de la matrice tf-idf des mots des discours des présidents
    # Lignes = mots (unique) du corpus
    # Colonnes = docs de 1 à n
    tf_idf.matrice_tf_idf_discours_presidents = tf_idf.creer_matrice_tf_idf(les_presidents.dossier_discours_presidents_nettoyes, tf_idf.les_dicos_occurrences_mots, tf_idf.matrice_tf_discours_presidents, tf_idf.matrice_idf_discours_presidents)

    # Transposition de la matrice tf-idf des mots des discours des présidents
    # Lignes = docs de 1 à n
    # Colonnes = mots (unique) du corpus
    tf_idf.matrice_transposee_tf_idf_discours_presidents = tf_idf.transpose_matrice(tf_idf.matrice_tf_idf_discours_presidents)

    # TEST SEULEMENT:

    # utile ?
    matrice_transforméé_idf_discours_presidents = tf_idf.transpose_matrice(tf_idf.matrice_idf_discours_presidents)

    question = "Quel président l'année en cours qu'aurait pu être et qu'on a vu concerné par le climat parle le plus du climat dans son discours"
    question = sm.nettoyer_texte(question)
    tf_idf.creer_vecteur_tf_idf_question(question, tf_idf.matrice_idf_discours_presidents)

    # FIN TEST SEULEMENT

    creer_ui()

main()