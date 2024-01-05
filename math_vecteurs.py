import math
import math as mod_math

def calculer_produit_scalaire_vecteurs(vecteur_A, vecteur_B):

    if len(vecteur_A) != len(vecteur_B):
        return "Erreur, les deux vecteurs doivent de dimensions égales"

    total_vecteur_AB = 0.0

    for i in range(len(vecteur_A)):
        # multiplier VecteurA(i) x VecteurB(i)
        vecteurs_AB_courant = vecteur_A[i] * vecteur_B[i]
        total_vecteur_AB += vecteurs_AB_courant

    return total_vecteur_AB
def calculer_norme_vecteur(vecteur):

    total = 0

    for i in range(len(vecteur)):
        valeur_courante = vecteur[i]
        valeur_courante_carree = valeur_courante ** 2
        total += valeur_courante_carree

    total = math.sqrt(total)

    return total
def calcul_similarite_vecteurs(vecteur_A, vecteur_B):

    # produit scalaire A.B / Norme vecteur A x Norme vecteur B
    produite_scalaire_vecteur_AB = 0
    produite_scalaire_vecteur_AB = calculer_produit_scalaire_vecteurs(vecteur_A, vecteur_B)

    norme_vecteur_A = 0
    norme_vecteur_B = 0
    norme_vecteur_AB = 0

    norme_vecteur_A = calculer_norme_vecteur(vecteur_A)
    norme_vecteur_B = calculer_norme_vecteur(vecteur_B)

    norme_vecteur_AB = norme_vecteur_A * norme_vecteur_B

    similarite_vecteurs = 0
    similarite_vecteurs = produite_scalaire_vecteur_AB / norme_vecteur_AB

    return similarite_vecteurs