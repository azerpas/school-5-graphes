# Documentation

## Sommaire
- [Pré-requis](#pré-requis)
- [Éxecuter le code](#éxecuter-le-code)
- [Structure du projet](#structure-du-projet)
- [Structure d'un graphe](#structure-dun-graphe)
- [Ajouter un graphe](#ajouter-un-graphe)
- [Logs](#logs)
- [Tests unitaires](#tests-unitaires)
- [Compiler](#compiler)
- [Documentation interne](#documentation-interne)

## Pré-requis
#### Requis
- Python 3.8 (Typings)
- PIP pour Python 3.8
#### Étapes
- Installez Python 3.8:
    - [Sous Windows](https://www.python.org/downloads/release/python-380/)
    - [Sous Mac, privilégiez brew](https://formulae.brew.sh/formula/python@3.8)
    - [Sous Unix](https://docs.python-guide.org/starting/install3/linux/)
- [Installez pip3](https://pip.pypa.io/en/stable/installing/)
    - Pensez à utiliser `python3 get-pip.py`
- Cloner le projet depuis Github
Après avoir cloné le projet:     
- `git clone https://github.com/azerpas/school-5-graphes.git projet && cd projet`
- Aller dans `setup.py`, changer `name='projet'` par le nom du dossier parent (pas nécessaire si fait sur l'étape précédente)    
- `python3 -m pip install -e .`
- `python3 -m pip install -r requirements.txt`
- Ajouter un graphe dans `./data` sous [la bonne forme](#structure-dun-graphe)

## Éxecuter le code

- Vérifier que l'installation est bien complète
- Vérifier qu'on est bien dans le répertoire parent (qui contient `setup.py`, `LICENSE`...)
- `cd traitement`
- `python3 I10-runner.py`

## Structure du projet
```
/
│
├── bin/ # Executable
│
├── docs/ # Documentation
│   └── ... 
│
├── traitement/ # Code
│   ├── __init__.py
│   └── I10-runner.py # Notre fichier principal
│
├── data/ # Données
│   ├── 1.txt # Graphe 1
│   ├── 2.txt # Graphe 2
│   ├── graphe_9-log12.03.13.txt # Log du graphe 9 à 12h03
│   └── ...
│
├── tests/ # Tests unitaires
│   └── runner_tests.py
│
├── .gitignore # fichiers ignorés dans git
├── LICENSE
├── setup.py # Le fichier setup
├── requirements.txt # Tous les packages nécessaires à l'exécution du code
└── README.md
```

## Structure d'un graphe
### Structure
```
[Nombre de sommets]
[Nombre d'arcs]
[Extrémité initiale] [Extrémité finale] [Poids de l'arc]
[Extrémité initiale] [Extrémité finale] [Poids de l'arc]
[Extrémité initiale] [Extrémité finale] [Poids de l'arc]
...
```

### Exemple
```
4
5
3 1 25
1 0 12
2 0 -5
0 1 0
2 1 7
```

## Ajouter un graphe
- Créez un nouveau fichier .txt
- Respectez la structure précédente
- Enregistrez le dans `./data/` avec son numéro exclusif, ex: `12.txt`, `1.txt`, `1201.txt`

## Logs
Tous les logs se situent dans `./data/` avec pour format `graphe_[numero]-log[heure].[min].[sec]`

## Tests unitaires
- `python3 -m unittest tests/runner_tests.py`

## Compiler
- [Référence python.org](https://docs.python.org/fr/3/distutils/builtdist.html)
- Placez vous dans le dossier parent
- Sous zip:
    - `python3 setup.py bdist --format=zip`
- Sous Windows
    - `python3 setup.py build --plat-name=win-amd64`
- Le résultat sera stocké dans `./build` et dans `./dist`

## Documentation interne
Toute la documentation du code est faite grâce à Docstring pour Python3.8 sous la forme:
- Description
- @Author: auteur
- @Args: arguments
- @Returns: retour