import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# A implémenter eventuellement:
#OuvrirFichier
#EnregistrerFichier

'''def extraire_nom_president(nom_fichier):
    nom_fichier = nom_fichier.replace("Nomination_", "").replace(".txt", "")

    elements = nom_fichier.rsplit("(", 1)

    nom_president = elements[0].strip()

    nom_president = ''.join([char for char in nom_president if not char.isdigit()])

    return nom_president'''