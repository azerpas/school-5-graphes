import os.path
from typing import TextIO

def ask():
    try:
        return int(input("Entrez le numéro du graphe: "))
    except ValueError as error:
        print("Entrez un nombre entier valide.")
        print(error)
        ask()

def lire_fichier(graphe: int) -> TextIO:
    try:
        file = open(os.path.dirname(__file__)+"/../data/"+str(graphe)+".txt", "r")
        return file
    except FileNotFoundError as error:
        print("Vérifiez que "+str(graphe)+".txt existe bien dans le dossier ~/data/")
        print(error)
        return ""

def creer_structure(file: TextIO) -> {"nb_sommets": int, "nb_arcs": int, "arcs": any}:
    structure = {
        "nb_sommets": 0,
        "nb_arcs": 0,
        "arcs": []
    }
    contenu = file.read().splitlines()
    structure["nb_sommets"] = contenu[0]
    structure["nb_arcs"] = contenu[1]
    for arc in range(2, len(contenu)):
        termes = contenu[arc].split(" ")
        if(len(termes) != 3):
            print("Pas assez de termes ligne: "+str(arc+1))
            continue
        structure["arcs"].append({"init": int(termes[0]), "terminale": int(termes[1]), "valeur": int(termes[2])})
    return structure