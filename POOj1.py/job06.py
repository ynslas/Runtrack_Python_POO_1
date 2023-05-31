#Créer une classe “Rectangle” avec des attributs privés, “longueur” et “largeur” initialisé dans le constructeur.


class Rectangle:
    def __init__(self,longueur,largeur):
        self._largeur=largeur
        self._longueur=longueur


#Créer des assesseurs et mutateurs afin de pouvoir afficher et modifier les attributs de la classe.

    @property
    def longeur(self):
        return self._longueur
    
    @longeur.setter
    def longeur(self,valeur):
        self._longueur=valeur

    
    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    def largeur(self,valeur):
        self._largeur=valeur

#Créer un rectangle avec les valeurs suivantes : longueur 10 et largeur 5. Changer la valeur de la longueur et de la largeur et vérifier que les modifications soient bien prises en compte.

RECT=Rectangle(10,5)
print(RECT.longeur)
print(RECT.largeur)
