# Class avec 2 methodes appelées dans le code

class Student:
    name = 'Thierry' # attribut de classe
    age = '25 ans' # attribut de classe

 
    @classmethod
    def displayName(cls):
        print("Le nom de l'etudiant est:" , cls.name)
    
    @classmethod
    def displayAge(cls):
        print("Il a:", cls.age)

# une méthode de classe est accessible directement en utilisant le nom de la classe        
print(Student.displayName())# affiche: Le nom de l'etudiant est: Thierry
print(Student.displayAge())# affiche l'âge de l'étudiant : 25 ans

# Pour réduire à nouveau le code et permettre une lecture et une écriture simplifiée nous aurions pu écrire ça de la manière suivante :

class Student:
    name = 'Thierry'
    age = '25 ans'

    @classmethod
    def display(cls):
        print("Le nom de l'étudiant est :", cls.name)
        print("Il a:", cls.age)

print(Student.display())

# On incite donc un regroupement d'informations dans une seule fonction au lieu de 2

    
 