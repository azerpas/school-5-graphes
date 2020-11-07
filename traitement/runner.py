import os.path
from typing import TextIO
from collections.abc import Iterable
import numpy as np
from enum import Enum

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
    file.close()
    return structure

def creer_matrice_adja(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    sommets = get_sommets(structure) 
    nb_sommets = len(sommets) # Nombre de sommets
    a = np.zeros((nb_sommets, nb_sommets), dtype=int) # Permet de remplir une matrice de 0 en fonction du nb de sommets

    # Pour tous les arcs du graphe
    for i in structure["arcs"]:
        sommet = i["init"] # On récupère le sommet associé à la valeur initiale
        ligne = sommets.index(sommet) # On récupère son index (sa ligne) dans la liste sommets 
        sommet = i["terminale"] # On récupère le sommet associé à la valeur terminale
        colonne = sommets.index(sommet) # On récupère son index (sa colonne) dans la liste sommets
        a[ligne][colonne] = 1 # On attribue 1 à la valeur de la matrice
    return a

def creer_matrice_valeurs(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    POIDS_INFINI = 1000000 # Qu'on pourrait décrire comme "infini" en théorie des graphes
    sommets = get_sommets(structure)
    nb_sommets = len(sommets)
    a = np.full((nb_sommets, nb_sommets), POIDS_INFINI) # On initialise la matrice de valeurs "infinies"

    # Pour tous les arcs du graphe
    for i in structure["arcs"]:
        sommet = i["init"] # On récupère le sommet associé à la valeur initiale
        ligne = sommets.index(sommet) # On récupère son index (sa ligne) dans la liste sommets
        sommet = i["terminale"] # On récupère le sommet associé à la valeur terminale
        colonne = sommets.index(sommet) # On récupère son index (sa colonne) dans la liste sommets
        poids = i["valeur"]
        a[ligne][colonne] = poids # On attribue "poids" à la valeur de la matrice
    return a

class Ordre(Enum):
    """Permet de créer une énumération des différents ordres de triage

    Args:
        Enum (enum.Enum): Classe Enum du package enum
    """
    CROISSANT = "1"
    DECROISSANT = "2"
    SIMPLE = "3"

def get_sommets(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}, ordre: Ordre = Ordre.SIMPLE) -> [any]:
    """Récupérer les sommets de la structure

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données
        ordre (Ordre, optional): Trier dans un ordre croissant, décroissant ou simple. Se référer à la classe Ordre. Par défaut Ordre.SIMPLE.

    Returns:
        [any]: Une liste des int, string ou autre contenu comme sommets du graphe
    """
    sommets = []
    for i in structure["arcs"]:
        if not i["init"] in sommets:
            sommets.append(i["init"])
    if ordre == Ordre.CROISSANT: sommets.sort()
    if ordre == Ordre.DECROISSANT: sommets.sort(reverse=True)
    return sommets