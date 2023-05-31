"""Créer une classe “Operation” avec un constructeur (méthode qui sera appelée lors de
l’instance de la classe). Ajouter les attributs “nombre1” et “nombre2” initialisés avec des
valeurs par défaut. Instancier votre première classe et imprimer l’objet en console."""

class Operation:
    def _init(self,nombre1=0,nombre2=0):
        self.nombre1=nombre1
        self.nombre2=nombre2
        
op=Operation()
print(op)
