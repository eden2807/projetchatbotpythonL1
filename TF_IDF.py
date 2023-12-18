# To Do de DE:
# A deplacer dans StringManager !

def obtenir_dico_occurences_mots(Texte):

    liste_mots = Texte.split()

    nombre_occurence_mot = 0

    dico_liste_mots = {}

    for mot in liste_mots:
        nombre_occurence_mot = 2 #compter_occurence_mot(mot, Texte)
        dico_liste_mots[mot] = nombre_occurence_mot

    return dico_liste_mots

'''
ATTENTION : compter_occurence_mot est à implémenter dans StringManager
def compter_occurence_mot(Mot, Texte):
#Extraire de la chaine de caracteres le nombre de fois que le mot a été trouvé
'''