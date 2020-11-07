import unittest
from unittest.mock import patch
from traitement.runner import ask, lire_fichier, creer_matrice_adja, creer_matrice_valeurs
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

if __name__ == '__main__':
    unittest.main()