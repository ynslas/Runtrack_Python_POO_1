class Animal:
    def __init__(self,age=0,prenom=""):
        self.age=age
        self.prenom= prenom
    
    def vieillir(self):
        x=self.age+1
        print("l'age de l'animal ",x)

    
    def nommer(self):
        print("l'animal se nomme ",self.prenom)

anim=Animal(0,"luna")
print("l'age de l'animal ",anim.age)

#apres appel de la methode veillir

anim.vieillir()
anim.nommer()


        