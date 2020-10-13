import unittest
from unittest.mock import patch
from traitement.runner import ask, lire_fichier

class RunnerTest(unittest.TestCase):
    @patch('builtins.input', return_value="1")
    def test_ask(self,input):
        self.assertEqual(ask(), 1)
    
    def test_lire_fichier(self):
        self.assertEqual(lire_fichier("do_not_delete").read(),"testing")

if __name__ == '__main__':
    unittest.main()