#Créer une classe “Voiture” qui a pour attributs privés une marque, un modèle , une année, un kilométrage et un attribut nommé “en_marche” initialisé à défaut sur False.
#Cette classe doit posséder des mutateurs et assesseur pour chaque attribut.



class Voiture:
    def __init__(self,marque,modele,année,kilometrage):
        self.__marque=marque
        self.__modele=modele
        self.__année=année
        self.__kilometrage=kilometrage
        self.__en_marche=False
        self.__reservoir=50



    def get_marque(self):
        return self.__marque
    
    def set_marque(self,nouvellemarque):
        self.__marque=nouvellemarque

    
    def get_modele(self):
        return self.__modele
    
    def set_modele(self,nouveaumodele):
        self.__modele=nouveaumodele


   
    def get_année(self):
        return self.__année
    
    def set_année(self,nouvelleannée):
        self.__année=nouvelleannée


    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def set_kilometrage(self,kilometrage):
        self.__kilometrage=kilometrage


    
#Créer une méthode “demarrer” qui change la valeur de l’attribut “en_marche” en True, une méthode “arreter” qui change la valeur de l’attribut “en_marche” en False.


        
    def demarrer(self,):
       if self.__verifier_plein():
        self.__en_marche=True
        print(self.__en_marche , ",La voiture est demmarée")
       else :
           print("la voiture ne peut pas demarrer, reservoir presque vide")

        
            


    def arreter(self):
        self.__en_marche=False
        print(self.__en_marche,",La voiture est arretée")


#Créer une méthode privée “verifier_plein” qui retourne la valeur de l’attribut “reservoir”. Cette méthode est appelée dans la méthode “demarrer” . Si la
#valeur du reservoir est supérieur à 5 la voiture peut demarrer.

    def __verifier_plein(self,):
        return self.__reservoir>5
    
    

    def Afficher(self):
        print("Marque: ",self.__marque)
        print("Modéle: ",self.__modele)
        print("Année: ",self.__année)
        print("kilometrage: ",self.__kilometrage)
        print("Statut vehicule: ",self.__en_marche)
        print("Niveau reservoir: ",self.__reservoir)


        


voiture1=Voiture("audi","A3","2023",35000)
voiture1.Afficher()

voiture1.demarrer()
voiture1.arreter()
