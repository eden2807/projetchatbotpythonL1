from tkinter import *

def creer_fenetre(Titre, Largeur, Hauteur):

    # creer la fenetre
    window = Tk()

    # attribuer un titre
    window.title(Titre)

    # dimensionner la fenetre
    WindowWidth = Largeur
    WindowHeight = Hauteur

    # recuperer la largeur et la hauteur de l'écran
    ScreenWidth = window.winfo_screenwidth()
    ScreenHeight = window.winfo_screenheight()

    # calculer les espaces servant à centrer la fenetre à l'écran
    XWindow = (ScreenWidth / 2) - (WindowWidth / 2)
    YWindow = (ScreenHeight / 2) - (WindowHeight / 2)

    # creer la fenetre et appliquer les espaces afin de la centrer
    window.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, XWindow, YWindow))

    return window

def creer_menu(window):

    menuBar = Menu(window)

    # Création du menu principal 'Programme'
    menuFichier = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Programme", menu=menuFichier)

    # Création des sous menus :
    menuFichier.add_command(label="Tester") # command=tmp.test_for_ui()
    menuFichier.add_command(label="Nouvelle question")
    menuFichier.add_command(label="Quitter")

    # Configuration de la barre des menus
    window.config(menu=menuBar)