def chercher_valeur_dans_liste_2D(liste, valeur, num_colonne_de_recherche=-1):

    for i in range(len(liste)):
        if liste[i][num_colonne_de_recherche] == valeur:
            return i
    return -1
