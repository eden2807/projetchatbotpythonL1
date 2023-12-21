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

