"""À l’aide de la classe “Operation” crée au-dessus, imprimer en console la valeur des
attributs “nombre1” et “nombre2”."""

class operation:
    def __init__(self,nombre1=0,nombre2=0):
        self.nombre1=nombre1
        self.nombre2=nombre2
        
operation=operation(13,5)
print("le nombre 1 est ",operation.nombre1)
print("le nombre 2 est ",operation.nombre2)
