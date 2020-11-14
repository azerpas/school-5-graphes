# PROJET THÉORIE DES GRAPHES

**Lien du GitHub**    
https://github.com/azerpas/school-5-graphes/ 

## Documentation du projet
[Disponible dans `./docs/README.md` ou en cliquant ici](/docs/README.md)

## Initialiser le projet
[Consulter la documentation](/docs/README.md)

## Tests unitaires
`python3 -m unittest tests/runner_tests.py`

## Illustration du projet
![Process](https://user-images.githubusercontent.com/19282069/95011857-15e00100-0634-11eb-9ca7-564b3127709c.png)

## Étapes (TODO): 
- [X] Fonction "Demander à l'utilisateur quel graphe"    
```python
graphe = input("Entrez le numéro du graphe: "); 
```    
- [X] Fonction "Lire le fichier .txt"    
```python
file = open(graphe+".txt", "r")
print(file.read())
```     
- [X] Enregistrer le graphe dans une structure de données    
* Nombre de sommets      
* Nombre d'arcs     
* Arcs[]      
`Le choix d’une structure de donnée plus efficace fera partie de votre évaluation.`      
- [X] Afficher le graphe sous forme de matrice d'adjacence et matrice de valeurs ou les deux combinées     
[Un lien où il détaille comment bien afficher les matrices](http://math.mad.free.fr/depot/numpy/base.html)      
- [X] Fonction "Appliquer l'algorithme de 'Floyd-Warshall'" avec 'L' et 'P' affichés     
- [X] Fonction "Afficher si graphe contient algo absorbant"     
- [X] Fonction "Afficher les chemins de valeurs minimales"   

## Graphes à prendre en compte     
- [X] Graphes orientés      
- [X] Graphes valués (valeurs dans Z)    
- [X] Sommets (valeurs dans N)    


## À tester     
```    
4
5
3 1 25
1 0 12
2 0 -5
0 1 0
2 1 7
```     

**Ligne 1**: Nombre de sommets = 4         
**Ligne 2**: Nombre d'arcs = 5     
**Ligne 3 à n**: Les arcs     

**Un arc** *(pour la première ligne)*:      
**1er terme**: Extrémité initiale = 3     
**2e terme**: Extrémité terminale = 1       
**3e terme**: Valeur de l'arc = 25      
