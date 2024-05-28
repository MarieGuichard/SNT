# La Carte MicroBit

## I. Qu'est ce que c'est? 

La carte micro:bit éditée par la BBC est un nano-ordinateur qui peut équiper un systéme informatique embarqué. Elle est munie d'un processeur ARM et de plusieurs capteurs et interfaces de connexion. 

Le guide de présentation en ligne est disponible sur https://microbit.org/fr/guide/

![](/ObjetsConnectés/IMG/image_carte_micro_bit.jpg)

La carte micro:bit dispose des spécificités techniques suivantes :

- 25 LEDs programmables individuellement
-  2 boutons programmables
-  Broches de connexion
-  Capteurs de lumière et de température  
- Capteurs de mouvements (accéléromètre et boussole)
-  Communication sans fil, via Radio et Bluetooth  
- Interface USB  

Nous utiliserons la carte en la connectant à un ordinateur avec le câble USB fourni qui assure la liaison de communication et l’alimentation. 

Si on veut intégrer la carte dans un système embarqué, il est possible de la connecter à une alimentation externe par piles. 

Lorsque la communication entre l’ordinateur et la carte échoue, on peut essayer de la redémarrer avec le bouton reset situé au verso. 

## II. L'éditeur en ligne. 

1. En utilisant un navigateur (chrome de préférence), rendez vous sur le site https://python.microbit.org/v/beta. 

2. Connecter votre microbit à l'aide du cable qui vous est fourni, puis cliquer sur le bouton Send to Microbit. 

   Si cela ne fonctionne pas, enregistrer le programme dans les téléchargements, puis copier le sur la microbit. 

3. Observer ce qui se passe sur votre microbit (il est parfois nécessaire de débrancher puis de rebrancher la microbit). 

4. Modifier le code pour qu'il affiche une autre image qu'un coeur. 

   Vous pouvez utiliser une des images intégrées : 

   Image.HEART Image.HEART_SMALL Image.HAPPY Image.SMILE Image.SAD 	Image.CONFUSED Image.ANGRY Image.ASLEEP Image.SURPRISED Image.SILLY 	Image.FABULOUS Image.MEH Image.YES Image.NO Image.CLOCK12, 	Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, 	Image.CLOCK1 Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E

5. Modifier le code pour qu'il affiche votre prénom. 

Appeler votre enseignante. 

## III. Créer sa propre image. 

Chaque pixel LED sur l’affichage physique peut prendre une parmi dix valeurs. Si un pixel 	prend la valeur 0 c’est qu’il est éteint. Littéralement, il a une luminosité de zéro. 

En revanche, s’il prend la valeur 9 il est à la luminosité maximale. Les valeurs de 1 à 8 représentent des niveaux de luminosité entre éteint (0) et « au maximum » (9). 

1. Recopier et exécuter le code suivant :

```python
from microbit import *
bateau = Image("05050:"
				"05050:"
              	"05050:"
                "99999:"
              "09990")
display.show(bateau)
```

​	 Chaque ligne de l’affichage physique est représentée par une ligne de nombres se terminant 	par : et entourée de guillemets doubles " . 

​	Chaque nombre indique une luminosité. 

​	Il y a cinq lignes de cinq nombres donc il est possible de spécifier la luminosité individuelle 	 	de chacune des cinq LED sur chacune des cinq lignes sur l’affichage physique. 

​	C’est ainsi que l'on crée une image. 

2.  Modifier le code précédent afin d'afficher un bateau avec un seul mât. 

3. Rédiger le programme qui affiche l'image suivante :

4. . Rédiger le programme qui affiche l'image suivante :

   ![](/ObjetsConnectés/IMG/image_canard.jpg)



5. Afficher un pixel. 

   Vous pouvez régler la luminosité des pixels de l'affichage individuellement de 0 (désactivé) à 9 (luminosité maximale). Pour des informations sur les coordonnées de l'affichage, voir le guide pour matrice à LED (https://microbit.org/guide/hardware/leds/) .  

   ​	a. Exécuter le programme suivant :  

   ​	

   ```python
   from microbit import *
   display.set_pixel(1,4,9)
   ```

   ​	b. Écrire le programme permettant d'allumer le pixel du centre de la matrice. 

### IV. Boucle While. 

1. Executer le code suivant:

   ```python
   from microbit import *
   while True:
   	display.set_pixel(2,2,9)
   	sleep(500)
        display.clear()
        sleep(500)
   ```

   

​	a. A votre avis, à quoi sert la deuxième ligne `while True`? 

​	b.  A votre avis, à quoi sert la quatrième ligne `sleep(500)`? 

​	c.  A votre avis, à quoi sert la sixième ligne `sleep(500)`? 

​	d. Modifier le programme pour que le pixel clignote plus rapidement.

2. Écrire un programme qui fait clignoter un cœur indéfiniment.

   Vous utiliserez image.HEART

3. Il est possible de combiner plusieurs images pour créer une animation. 

   ​	Écrire un programme permettant d'afficher l'animation suivante :

   ​	https://makecode.microbit.org/---run?id=_4xi7Ct2DzWXK

Remarque : il est évidement possible d'utiliser une boucle for ou un structure conditionnelle (avec il, elif, else). 

### V. La programmation événementielle: utilisons les boutons. 

La carte micro:bit possède deux boutons servant d'actionneur. C'est à dire qu'il est possible de modifier l'aspect de la carte en appuyant sur l'un des boutons et en programmant correctement la carte. 

1. charger le code suivant sur votre carte. 

   ```python
   from microbit import *
   while True:
       display.scroll("SNT")
       sleep(200)
       if button_a.was_pressed():
           break
   ```

   

 2 .Exécuter le code sans appuyer sur le bouton A, puis en appuyant sur le bouton A. Que se passe-t-il ?

​	Exemples de méthodes avec le bouton A: 

​	`button_a.is_pressed()` : renvoie `True` si le bouton spécifié est actuellement enfoncé et `False` 		sinon. 

​	`button_a.was_pressed()` : renvoie `True` ou `False` pour indiquer si le bouton a été appuyé depuis le 	démarrage de l'appareil ou la dernière fois que cette méthode a été appelée. 

3. Écrire le programme permettant d'afficher l'image HAPPY si le bouton A est pressé, l'image SAD si le bouton est pressé, et l'image HEART sinon. 



### VI. Capteur de luminosité. 

En inversant les LEDs d'un écran pour devenir un point d'entrée, l'écran LED devient un capteur de lumière basique, permettant de détecter la luminosité ambiante. 

La commande `display.read_light_level()` retourne un entier compris entre 0 et 255 représentant le niveau de lumière. 

1.  Compléter le programme ci-dessous qui affiche une image de lune si on baisse la luminosité (en recouvrant la carte avec sa main par exemple) et un soleil sinon.

​	

```python
from microbit import *
soleil = Image("90909:"
              "09990:"
              "99999:"
              "09990:"
              "90909:")
lune = Image("00999:"
            "09990:"
            "09900:"
            "09990:"
            "00999:")
while True: 
    if display.read_light_level()> # compléter ici :
    	display.show(soleil)
        sleep(500)
    else:
        display.show("compléter ici")
        sleep(500)
```



2. Créer un programme qui plus la luminosité sera élevée, plus il y aura de LEDs affichées sur la matrice. 

