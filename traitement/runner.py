import os.path
from typing import TextIO
from collections.abc import Iterable
import numpy as np

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

def creer_structure(file: TextIO) -> {"nb_sommets": int, "nb_arcs": int, "arcs": any}: # il faudra remplacer any par: typing.TypedDict
    structure = {
        "nb_sommets": 0,
        "nb_arcs": 0,
        "arcs": []
    }
    contenu = file.read().splitlines()
    structure["nb_sommets"] = contenu[0]
    structure["nb_arcs"] = contenu[1]
    for arc in range(2, len(contenu)): # on itère dans le reste des lignes du fichier
        termes = contenu[arc].split(" ") # on sépare la ligne par les espaces
        if(len(termes) != 3): # s'il y a moins de 3 entiers, il manque un terme
            print("Pas assez de termes ligne: "+str(arc+1))
            continue
        structure["arcs"].append({"init": int(termes[0]), "terminale": int(termes[1]), "valeur": int(termes[2])})
    return structure

#for x in range(structure["nb_sommets"]): # Pour chaque ligne
    #    for y in range(structure["nb_sommets"]): # Pour chaque colonne

def creer_matrice_adja(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    sommets = [] # toutes les sommets
    for i in structure["arcs"]:
        if not i["init"] in sommets:
            sommets.append(i["init"])
    # sommets = [3,2,1,0]
    #   3 2 1 0
    # 3     1
    # 2 
    # 1
    # 0
    a = np.zeros((4,4), dtype=int)
    for i in structure["arcs"]:
        sommet = i["init"]
        # sommet = 3
        ligne = sommets.index(sommet)
        # ligne = 0
        sommet = i["terminale"]
        # sommet = 1
        colonne = sommets.index(sommet)
        # colonne = 2
        a[ligne][colonne] = 1
        # a[0][2]    

def creer_matrice_valeurs(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    return