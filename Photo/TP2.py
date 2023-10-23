from PIL import Image
def FiltreRouge(NomFichier):
    img = Image.open(NomFichier) #chargement de l'image
    Largeur, Hauteur = img.size # récupération de ses dimensions
    
    #double boucle pour parcourir tous les pixels de l'image
    for x in range(Largeur): # boucle sur les colonnes de l'image
        for y in range(Hauteur): #boucle sur les lignes de l'image
            r,v,b, = img.getpixel((x,y))
            img.putpixel((x,y),(r,0,0))
    img.show() # affiche l'image modifiée
    
def FiltreVert(NomFichier):
    pass
