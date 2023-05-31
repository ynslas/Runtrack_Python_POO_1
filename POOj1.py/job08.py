#Récupérer la classe “Livre”. Ajouter l'attribut privé suivant : - “disponible” initialisé par défaut a True.


class Livre:
    def __init__(self,titre,auteur,nbpages):
        self.__titre=titre
        self.__auteur=auteur
        self.__nbpages=nbpages
        self.__disponible=True

    @property
    def titre(self):
        return self.__titre
    
    @titre.setter
    def titre(self,nouv_titre):
        self.__titre=nouv_titre

    @property
    def auteur(self):
        return self.__auteur
    
    @auteur.setter
    def auteur(self,nouv_auteur):
        self.__auteur=nouv_auteur

    @property
    def nbpages(self):
        return self.__nbpages
    
    @nbpages.setter
    def nbpages(self,nouv_page):
        self.__nbpages=nouv_page

    def changementpages(self,nouvellepage):
        if type (nouvellepage)==int and nouvellepage > 0:
            self.__nbpages=nouvellepage
            print("la page est: ",nouvellepage)
        else:
            print("Erreur la page est incorrect ,le nombre doit etre un entier positif")

    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def disponible(self,nouvelle_dispo):
        self.__disponible=nouvelle_dispo

    #Créer une méthode nommée “vérification” qui vérifie si le livre est disponible, c'est-à-dire que la valeur de son attribut disponible est égale à True. Cette méthode doit retourner True ou False.
    
    def verification(self):
       return self.__disponible
    
     
    def afficher(self):
        print("Auteur du livre: ",self.__auteur)
        print("Titre du livre: ",self.__titre)
        print("Nombre de page du livre: ",self.__nbpages)
        print("disponibilité: ",self.__disponible)


#Ajouter une méthode “emprunter” qui rend le livre indisponible, autrement dit la valeur de “disponible” devient False. Bien sûr, pour pouvoir emprunter un livre, il faut que
#celui-ci soit disponible, vérifier donc que celui-ci soit disponible sans utiliser l’attribut “disponible”.


    def emprunter(self):
        if self.verification():
            self._disponible=False
            print("le livre a eté emprunter")
        else:
            print("le livre n'est pas disponible")


    
#Après avoir emprunté un livre, il faut pouvoir le rendre. Créer une méthode “rendre” qui dans un premier temps vérifie si le livre a bien été emprunter ( sans utiliser l’attribut
#“disponible”), puis change la valeur de l’attribut “disponible”.
    
    
    def rendre(self):
        if not self.verification():
            self._disponible=True
            print("le livre a été rendu")
        else :
            print("le livre n'a pas été emprunter")
    

livre1=Livre("Dragon ball Z","Akira Toriyama",500)
livre1.afficher()
print(livre1.verification())

"""livre1.disponible=False
livre1.verification()
print(livre1.verification())"""

livre1.emprunter()

livre1.rendre()

livre2=Livre("goal","yaya",400)
livre1.rendre()





