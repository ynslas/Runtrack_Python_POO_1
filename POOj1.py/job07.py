#Créer la classe 'Livre’ qui prend en attributs privés un titre, un auteur et un nombre de pages.


class Livre:
    def __init__(self,titre,auteur,nbpages):
        self._titre=titre
        self._auteur=auteur
        self._nbpages=nbpages


#Créer les assesseurs et mutateurs nécessaires afin de pouvoir modifier et afficher les attributs.

    @property
    def titre(self):
        return self._titre
    
    @titre.setter
    def titre(self,nouv_titre):
        self._titre=nouv_titre

    @property
    def auteur(self):
        return self._auteur
    
    @auteur.setter
    def auteur(self,nouv_auteur):
        self._auteur=nouv_auteur

    @property
    def nbpages(self):
        return self._nbpages
    
    @nbpages.setter
    def nbpages(self,nouv_page):
        self._nbpages=nouv_page

    
    #Pour changer le nombre de pages, le nombre doit être un nombre entier positif sinon la valeur n’est pas changée et un message d’erreur est affiché.
    
    def changementpages(self,nouvellepage):
        if type (nouvellepage)==int and nouvellepage > 0:
            self._nbpages=nouvellepage
            print("la page est: ",nouvellepage)
        else:
            print("Erreur la page est incorrect ,le nombre doit etre un entier positif")


    def afficher(self):
        print("Auteur du livre: ",self._auteur)
        print("Titre du livre: ",self._titre)
        print("Nombre de page du livre: ",self._nbpages)


    
livre1=Livre("Dragon ball Z","Akira Toriyama",500)
livre1.afficher()
livre1.changementpages(334.5)

livre1._titre="Dragon ball GT"
livre1.afficher()







    
        
        