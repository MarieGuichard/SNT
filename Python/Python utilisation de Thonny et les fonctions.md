# Python: utilisation de Thonny et les fonctions. 



## I. IDE (environnement de développement). 

Un environnement de développement est un logiciel qui facilite l’écriture d’un programme. Il en existe des dizaines pour Python. Vous disposez au lycée  Thonny. 

Ouvrir Thonny. 

![](E:\lycee\SNT\Python\iconeThonny.jpg){width = 100 ; height = 100}

Une fenêtre de ce type devrait s'ouvrir (si cela n'est pas le cas, appeler votre enseignante). 

![](E:\lycee\SNT\Python\thonny.jpg)

Nous distinguerons deux fenêtres:

- la fenêtre du haut: elle permet d'écrire un programme, des fonctions et de les sauvegarder. 
- la fenêtre du bas: c'est le shell. Elle permet exécuter le programme écrit dans la fenêtre du haut et d'effectuer des tests. 

Testons tout cela:

Dans la fenêtre du haut, recopiez soigneusement le code ci-dessous. 

```python
print("Bonjour")
Nom = input("Comment vous appelez vous ? ")
print("Comment allez vous Monsieur ou Madame ", Nom )
```

Ensuite, sauvegardez votre programme que vous appellerez test dans votre espace personnel. 

Exécutez votre programme en cliquant sur la petite flèche verte située juste au-dessus ou en appuyant sur la touche F5 de votre clavier. 

Observez alors ce qui se passe dans le Shell. Répondez à la question posée et appuyez sur entrée. 

#### Exercice 1:

Ecrire un programme qui demande l'âge à l'utilisateur et qui calcule l'âge que l'utilisateur aura en 2050. 

Exécutez le programme et testez le avec votre âge, puis avec 30. 



Rappel: pour demander à l'utilisateur un nombre, il faut utiliser la fonction input(), ainsi que la fonction int(), puisque par défaut, input() donne une chaine de caractères. 

Exemple: `note = int(input('quelle note avec vous eu en SNT? '))`



## II. Les fonctions. 

En travaillant sur py-rates, vous avez rencontré de nombreuses fonctions qui ne se comportaient pas toutes de la même manière. 

Nous pouvons en distinguer deux types: 

- les fonctions sans paramètre:

  Par exemple, la fonction `avancer() `permettait d'avancer d'une case et une seule case. 

- les fonctions avec paramètre:

  Par exemple, la fonction `sauter (hauteur)`permettait de sauter de la hauteur indiquée entre parenthèses. On dit que `hauteur`est un paramètre de la fonction. 

  `sauter(3)`permettait à notre héros de sauter de trois blocs, le paramètre `hauteur`valant ici 3. 

Il existe en python de nombreuses fonctions prédéfinies. Nous avons déjà utilisé `print()`, `input()` par exemple. 

Il est bien sur possible d’écrire ses propres fonctions. Cela permet de simplifier un programme et d’éviter de répéter du code.

### a. Fonctions sans paramètres. 

#### Exercice 2: 

```python
from random import * #importe le module permettant de générer un tirage au sort de nombre au hasard
def de():
    ''' renvoie le tirage au sort d'un dé cubique (valeurs compris entre 1 et 6) '''
    face = randint(1,6) # fonction du module random renvoyant un nombre compris entre 1 et 6
    return face # renvoie la valeur obtenue

```

Nous avons écrit une fonction `de()`. Nous avons utilisé pour cela le mot clé `def`. 

Comme pour les autres instructions vues précédemment, celui ci doit être suivi de `:` et le contenu de la fonction doit être indenté.

1. Recopiez le code dans la partie supérieure et sauvegardez le. (Vous pouvez omettre les commentaires). 

2. Exécutez le code. Que se passe-t-il? 

3. En vous plaçant dans le shell, écrivez `de()`, puis appuyez sur la touche entrée. 

   Recommencez l'opération trois fois. Que constatez vous? 

   Le shell vous a servi à utiliser votre fonction. 

4. Ecrire une fonction qui tire au hasard un nombre compris entre 1 et 100 et renvoie 'pair' si le nombre tiré est pair, et 'impair ' sinon. 



### b. Fonctions avec paramètres. 

#### Exercice 3:

```python
def aire_carre(longueur):
    '''renvoie l'aire d'un carré d'une longueur donnée'''
    aire = longueur*longueur
    return aire
```

1. Recopiez le code dans la partie supérieure et sauvegardez le. (Vous pouvez omettre les commentaires). 

2. Exécutez le code. Que se passe-t-il? 

3. En vous plaçant dans le shell, écrivez `aire_carre(3)`, puis appuyez sur la touche entrée. 

   Que se passe-t-il? 

4. Quelle instruction devez vous écrire afin d'obtenir l'aire d'un carré de côté 5? 

5. Ecrire une fonction `aire_rectangle (longueur,largeur)`qui calcule l'aire d'un rectangle de longueur et largeur données.



#### Exercice 4: 

Ecrire une fonction `coucou(nombre)`qui affiche 'coucou' autant de fois que le nombre entré en paramètres. 



#### Exercice 5:

Ecrire une fonction `température(valeur)`qui affiche `froid` si la valeur est inférieure à 10, `doux`si la valeur est comprise entre 10 et 20 et `chaud`sinon. 



#### Exercice 6: 

Ecrire une fonction `maximum(a,b,c)` qui renvoie le plus grand des trois nombres a,b et c. 

