"""Créez une classe “Personne” avec les attributs “nom” et “prenom”.""" 


class Personne:
    def __init__(self,nom,prenom):
        self.nom= nom
        self.prenom= prenom

    
    
    """Ajoutez une méthode “SePresenter()” qui retourne le nom et le prénom de la personne. Ajoutez aussi un constructeur prenant en paramètres de quoi donner des valeurs initiales aux attributs “nom” et “prenom”."""

    
    def SePresenter(self):
        return f"je suis {self.nom}  {self.prenom}"


    """Instanciez plusieurs personnes avec les valeurs de construction de votre choix et faites appel à la méthode “SePresenter()” afin de vérifier que tout fonctionne correctement."""
    
pers1=Personne("John","Doe")
pers2=Personne("Jean", "Dupont")

print(pers1.SePresenter())
print(pers2.SePresenter())





        