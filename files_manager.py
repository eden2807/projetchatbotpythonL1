import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def lire_contenu_fichier(dossier_fichier, nom_fichier):

    if nom_fichier.endswith(".txt"):

        # assembler le chemin complet du fichier (path dossiers + nom fichier)
        chemin_fichier = os.path.join(dossier_fichier, nom_fichier)

        # Lire le contenu du fichier
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            texte = f.read()

        return  texte