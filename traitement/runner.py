import os.path
from typing import TextIO
from collections.abc import Iterable
import numpy as np
import pandas as pd
from enum import Enum
from datetime import datetime

def log(string: any):
    """Remplace la fonction print en permettant l'ajout du print dans un fichier .txt

    Author: @azerpas

    Args:
        string (any): n'importe quel type d'objet

    Raises:
        Exception: Impossible de sauvegarder dans le fichier
    """
    print(string)
    print()
    try:
        b = enregistrer_dans_fichier(str(string))
        if not b:
            raise Exception()
    except Exception:
        print("Erreur lors de la sauvegarde des logs dans le fichier .txt")
    

def ask() -> int:
    """Permet de demander le numéro d'un graphe

    Returns:
        int: Le numéro du graphe
    """
    try:
        return int(input("Entrez le numéro du graphe: "))
    except ValueError as error:
        log("Entrez un nombre entier valide.")
        log(error)
        ask()

def lire_fichier(graphe: int) -> TextIO:
    """Lecture d'un fichier contenu dans le dossier "data"

    Author: @azerpas

    Args:
        graphe (int): Le numéro du graphe

    Returns:
        TextIO: Un flux I/O (In/Out) permettant de lire un fichier par byte
    """
    try:
        file = open(os.path.dirname(__file__)+"/../data/"+str(graphe)+".txt", "r")
        return file
    except FileNotFoundError as error:
        log("Vérifiez que "+str(graphe)+".txt existe bien dans le dossier ~/data/")
        log(error)
        raise(error)

def enregistrer_dans_fichier(string: str) -> bool:
    """Permet d'enregistrer un string dans un fichier

    Author: @azerpas

    Args:
        string (str): la chaîne de caractères à enregistrer 

    Returns:
        bool: True si succès, False si erreur
    """
    try:
        heure_minute_secondes = datetime.now().strftime("%H.%M.%S")
        file = open(os.path.dirname(__file__)+"/../data/log"+str(heure_minute_secondes)+".txt", "a")
        file.write(string+"\n\n")
        file.close()
        return True
    except FileNotFoundError as error:
        log("Vérifiez que le dossier ~/data/ existe")
        log(error)
        return False

def creer_structure(file: TextIO) -> {"nb_sommets": int, "nb_arcs": int, "arcs": any}: # il faudra remplacer any par: typing.TypedDict
    """Création de la structure de données du graphe

    Returns:
        {"nb_sommets": int, "nb_arcs": int, "arcs": any}: La structure de données du graphe
    """
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
            log("Pas assez de termes ligne: "+str(arc+1))
            continue
        structure["arcs"].append({"init": int(termes[0]), "terminale": int(termes[1]), "valeur": int(termes[2])})
    file.close()
    return structure

def creer_matrice_adja(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    """Crée la matrice adjacente du graphe à partir de sa structure de données

    Author: @azerpas

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données du graphe

    Returns:
        numpy.array: La matrice sous la forme d'une numpy array
    """
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
    """Crée la matrice de valeurs du graphe à partir de sa structure de données

    Author: @azerpas

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données du graphe

    Returns:
        numpy.array: La matrice sous la forme d'une numpy array
    """
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

    Author: @azerpas

    Args:
        Enum (enum.Enum): Classe Enum du package enum
    """
    CROISSANT = "1"
    DECROISSANT = "2"
    SIMPLE = "3"

def get_sommets(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}, ordre: Ordre = Ordre.SIMPLE) -> [any]:
    """Récupérer les sommets de la structure

    Author: @azerpas

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données du graphe
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

def creer_P(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    """Permet la création de la matrice P qui sert à l'algorithme de Floyd Warshall

    Author: @azerpas

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données du graphe

    Returns:
        matrice (4x4): Matrice P du graphe
    """
    sommets = get_sommets(structure)
    nb_sommets = len(sommets)
    a = np.zeros((nb_sommets, nb_sommets), dtype=int)
    for i in range(nb_sommets):
        for j in range(nb_sommets):
            a[i][j] = sommets[i]
    return a

def creer_L(matrice):
    """Permet la création de la matrice L qui sert à l'algorithme de Floyd Warshall

    Author: @azerpas

    Args:
        matrice (4x4): Matrice 4x4 du graphe

    Returns:
        matrice (4x4): Matrice L du graphe
    """
    r,c = matrice.shape
    for i in range(r):
        for j in range(r):
            if(i == j):
                matrice[i][j] = 0
    return matrice

def has_circuit_absorbant(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}) -> bool:
    """Retourne si la structure contient un circuit absorbant

    Author: @azerpas

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données du graphe

    Returns:
        bool: Contient ou non un circuit absorbant
    """
    for i in structure["arcs"]:
        if int(i["valeur"]) < 0:
            return True
    return False

def floyd_warshall(structure: {"nb_sommets": int, "nb_arcs": int, "arcs": any}):
    """Applique l'algorithme de Floyd Warshall

    Author: @azerpas

    Args:
        structure ({"nb_sommets": int, "nb_arcs": int, "arcs": any}): La structure de données du graphe
    """
    sommets = get_sommets(structure)
    nb_sommets = len(sommets)
    mat_valeurs = creer_matrice_valeurs(structure)
    L = creer_L(mat_valeurs)
    P = creer_P(structure)
    for k in range(nb_sommets):
        for i in range(nb_sommets):
            for j in range(nb_sommets):
                if (L[i][k] + L[k][j]) < L[i][j]:
                    L[i][j] = L[i][k] + L[k][j]
                    P[i][j] = P[k][j]
    log(L)
    log(P)

def main():
    choice = ask()
    log("Vous avez choisi le graphe: "+str(choice))
    log("Lecture du fichier "+str(choice)+".txt")
    try:
        file = lire_fichier(choice)
    except Exception as e:
        log("Erreur fichier: ")
        log(e)
        return main()
    log("Création de la structure")
    structure = creer_structure(file)
    log("Création des matrices")
    a = creer_matrice_adja(structure)
    b = creer_matrice_valeurs(structure)
    log(a)
    log(b)
    log("Exécution de Floyd Marshall...")
    f = floyd_warshall(structure)
    absorbant = has_circuit_absorbant(structure)
    if(absorbant):
        log("Présence d'un circuit absorbant, merci de choisir un autre graphe.")
        return main()
    

if __name__ == '__main__':
    main()