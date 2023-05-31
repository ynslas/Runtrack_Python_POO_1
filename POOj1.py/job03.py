"""Modifier votre classe “Operation” afin d’y ajouter la méthode addition. Cette méthode
additionne “nombre1” et “nombre2” et affiche en console le résultat."""


class Operation:
    def __init__(self,nombre1=0,nombre2=0):
        self.nombre1=nombre1
        self.nombre2=nombre2
    def add(self):
        print("la somme des 2 nombres est :",Operation.nombre1+Operation.nombre2)


Operation=Operation(15,3)
print("le nombre 1 est ",Operation.nombre1)
print("le nombre 2 est ",Operation.nombre2)
Operation.add()