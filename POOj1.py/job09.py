#Créer une classe nommée “Student” qui a comme attributs privés un nom, un prénom,
#un numéro d’étudiants et un nombre de crédits par défaut à zéro.


class Student:
    def __init__(self,nom,prenom,numero_etudiant,nb_credit=0):
        self.__nom=nom
        self.__prenom=prenom
        self.__numero_etudiant=numero_etudiant
        self.__nb_credit=nb_credit
        self.__level=self.__studentEval()

#La méthode “add_credits” permet d’ajouter un nombre de crédits au total de celui de l’étudiant. Ce
#mutateur doit s’assurer que la valeur passée en argument est supérieure à zéro pour garantir l’intégrité de la valeur.


    def set_nb_credit(self,nouv_credit):
        self.__nb_credit=nouv_credit

    def add_credit(self,nouv_credit):
        if (nouv_credit)>0:
            self.__nb_credit=self.__nb_credit+nouv_credit
            print("le nombre de crédit de ",self.__nom , "est de ",nouv_credit)

    


    def studentInfo(self):
        print("Nom: ",self.__nom)
        print("Prenom: ",self.__prenom)
        print('Numéro Etudiant: ',self.__numero_etudiant)
        print("Nombre de credit: ",self.__nb_credit)
        print("Niveau: ",self.__studentEval())

    def __studentEval(self,):
        if (self.__nb_credit)>=90:
            return "Excellent"
        elif (self.__nb_credit)>=80:
            return "Trés Bien"
        elif (self.__nb_credit)>=70:
            return "Bien"
        elif (self.__nb_credit)>=60:
            return "Passable"
        elif (self.__nb_credit)<60:
            return "Insuffisant"
        

        
#Instancier un objet représentant l’étudiant John Doe qui possède le numéro d’étudiant 145. 
# Ajoutez-lui des crédits à trois reprises et imprimer son total de crédits en console.

    

stud1=Student("Doe","John",145,0)
stud1.studentInfo()
stud1.add_credit(10)
stud1.add_credit(10)
stud1.add_credit(10)

stud1.studentInfo()




