# Création tuple, mise à jour et affichage

a = (3, 4, 7) #Création du tuple
type(a) #Commande d'affichage de type (qui ressortira que vous venez de créer un tuple)

# Parfois les tuple ne présentent pas de paranthèses

# Notation différente de tuple

b, c = 1, 4 #Création du tuple
b #On appelle le premier chiffre défini par la variable 'b'
c #On appelle le second chiffre défini par la variable 'c'

# Si on reprend la forme de variable contenant les parenthèses cela revindrais à ça 

(b, c) = (1, 4)

# Synthaxe avec plusieurs variables à droite et variable unique à gauche (si celle-ci contient un tuple)

a = (1, 4)
u, v = a
u #On obtient le premier chiffre
v #On obtient le seconde chiffre
