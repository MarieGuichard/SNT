# Dessiner une image numérique. 

Voici comment il est possible de représenter, par exemple, un écran de 64 pixels. 

![](E:\lycee\SNT\photo numériques\tableau_pixel.jpg)

Nous allons dessiner des images numériques à l'aide Python. 

Pour cela, nous utiliserons Thonny. 

1. Ouvrez Thonny, créer un nouveau fichier que vous appellerez image.py. Vous le sauvegarderez dans votre répertoire photos. 

2. Dans la partie supérieure de Thonny, recopiez le code suivant et exécutez le:

   ```python
   from PIL import Image 
   monimage = Image.new("RGB",(8,8))
   monimage.show()
   ```

   

La première ligne permet de charger la librairie que nous utiliserons pour faire des dessins. 

La deuxième ligne permet de créer une image de 64 pixels, qui seront par défaut en noir. 

La troisième ligne permet de d'afficher l'image (il vous sera probablement nécessaire de zoomer afin de la voir correctement ). 

3. Insérez la ligne suivante en troisième position dans votre code puis exécutez à nouveau votre programme. Zoomez afin de regarder ce qui se passe sur votre image. 

   ```python
   monimage.putpixel((0,0),(255,0,0))
   ```

   Que se passe-t-il? 

   Cette instruction permet de colorer le pixel de coordonnées (0,0) en rouge. 

   Rappel: une couleur est codé par un triplet d'entier (R, G, B) dont les valeurs sont comprises entre 0 et 255. R correspond à la quantité de rouge, G à la quantité de vert et B à la quantité de B. 

   Ainsi, (255,0,0) donne la couleur rouge puisque Vert et Bleu sont à zéro. 

4. Modifiez le programme pour colorer en bleu le pixel de coordonnées (0,0). 

5.  les étapes suivantes, à faire valider par votre professeur une par une :

   1. Modifier le programme pour colorer en rouge uniquement le deuxième pixel de la première ligne, puis uniquement le troisième.

6. Modifier le programme pour colorer en rouge uniquement le deuxième pixel de la première ligne, puis uniquement le troisième.

7. Modifier le programme pour colorer en rouge toute la première ligne. 

   Vous utiliserez une boucle pour cela.

8. Modifier à nouveau le programme pour colorer en rouge uniquement la deuxième ligne, puis uniquement la troisième ligne.  

9. Trouver comment colorer en rouge toutes les lignes de l'image, de la façon la plus simple possible.  

10. Afin de pouvoir facilement changer de couleur, créer une fonction `creation_image` utilisant un paramètre nommé couleur qui contiendra le code actuel du programme.

    Une fois votre code exécuté, l'appel en console de `creation_image((255,0,0))` devra afficher une image rouge mais `creation_image((0,255,0))` devra afficher une image verte, ….

11. Ajouter deux paramètres à la fonction, longueur et largeur, pour pouvoir changer le nombre de pixels à la demande.

12. Pour aller plus loin : écrire une fonction permettant la création d'un drapeau

    