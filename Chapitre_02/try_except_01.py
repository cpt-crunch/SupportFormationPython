# Démonstration d'un try-except

while True:
    try: # Création d'une clause try afin de demander d'entrer un nombre
        x = int(input("Merci de rentrer un nombre"))
        break # Permet à l'utilistaeur d'interrompre le programme 
    except ValueError: # Création d'une clause except qui ne rentre en compte que si la clause try n'est pas vraie
        print("Nombre incorret, merci de saisir un autre nombre")


# /!\ Cette d"monstration de code est a appliquer dans un code complet donnant le contexte à la boucle
# Notez que 'ValueError' est utilisé dans cet exemple car l'exception concerne une valeur, d'autres types existent et peuvent être compilés dans un tuple afin d'en vérifié plusieurs

