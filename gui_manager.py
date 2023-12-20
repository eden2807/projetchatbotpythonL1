from tkinter import *
import Temp as tp

def creation_fenetre(Titre, Largeur, Hauteur):

    # creer la fenetre
    Window = Tk()

    # attribuer un titre
    Window.title("Projet ChatBot")

    # dimensionner la fenetre
    WindowWidth = Largeur
    WindowHeight = Hauteur

    # recuperer la largeur et la hauteur de l'écran
    ScreenWidth = Window.winfo_screenwidth()
    ScreenHeight = Window.winfo_screenheight()

    # calculer les espaces servant à centrer la fenetre à l'écran
    XWindow = (ScreenWidth / 2) - (WindowWidth / 2)
    YWindow = (ScreenHeight / 2) - (WindowHeight / 2)

    # creer la fenetre et appliquer les espaces afin de la centrer
    Window.geometry('%dx%d+%d+%d' % (WindowWidth, WindowHeight, XWindow, YWindow))

    return Window

def creation_menu(Window):

    menuBar = Menu(Window)

    # Création du menu principal 'Programme'
    menuFichier = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Programme", menu=menuFichier)

    # Création des sous menus :
    menuFichier.add_command(label="Tester", command=tp.test)
    menuFichier.add_command(label="Nouvelle question")
    menuFichier.add_command(label="Quitter")

    # Configuration de la barre des menus
    Window.config(menu=menuBar)