import unittest
from unittest.mock import patch
from traitement.runner import ask, lire_fichier, creer_matrice_adja, creer_matrice_valeurs, creer_L, creer_P, floyd_warshall
import numpy as np

class RunnerTest(unittest.TestCase):
    @patch('builtins.input', return_value="1")
    def test_ask(self,input):
        self.assertEqual(ask(), 1)
    
    def test_lire_fichier(self):
        file = lire_fichier("do_not_delete")
        self.assertEqual(file.read(),"testing")
        file.close()
    
    def test_matrice_adjacente(self):
        a = np.array([[0, 1, 0, 0],
                    [0, 0, 0, 1],
                    [0, 1, 0, 1],
                    [0, 1, 0, 0]])
        structure = {'nb_sommets': 4, 'nb_arcs': 5, 'arcs': [{'init': 3, 'terminale': 1, 'valeur': 25}, {'init': 1, 'terminale': 0, 'valeur': 12}, {'init': 2, 'terminale': 0, 'valeur': -5}, {'init': 0, 'terminale': 1, 'valeur': 0}, {'init': 2, 'terminale': 1, 'valeur': 7}]}
        b = creer_matrice_adja(structure)
        self.assertEqual(a.all(),b.all())

    def test_matrice_valeurs(self):
        a = np.array([[1000000, 25, 1000000, 1000000],
                    [1000000, 1000000, 1000000, 12],
                    [1000000, 7, 1000000, -5],
                    [1000000, 0, 1000000, 1000000]])
        structure = {'nb_sommets': 4, 'nb_arcs': 5, 'arcs': [{'init': 3, 'terminale': 1, 'valeur': 25}, {'init': 1, 'terminale': 0, 'valeur': 12}, {'init': 2, 'terminale': 0, 'valeur': -5}, {'init': 0, 'terminale': 1, 'valeur': 0}, {'init': 2, 'terminale': 1, 'valeur': 7}]}
        b = creer_matrice_valeurs(structure)
        self.assertEqual(a.all(),b.all())

    def test_floyd_warshall(self):
        structure = {'nb_sommets': 4, 'nb_arcs': 7, 'arcs': [{'init': 1, 'terminale': 2, 'valeur': 2}, {'init': 2, 'terminale': 3, 'valeur': -2}, {'init': 3, 'terminale': 4, 'valeur': 5}, {'init': 4, 'terminale': 1, 'valeur': -4}, {'init': 1, 'terminale': 4, 'valeur': 6}, {'init': 4, 'terminale': 2, 'valeur': -1}, {'init': 3, 'terminale': 2, 'valeur': 5}]}
        mat_valeurs = creer_matrice_valeurs(structure)
        L = creer_L(mat_valeurs)
        P = creer_P(structure)
        floyd_warshall(structure)
        

if __name__ == '__main__':
    unittest.main()