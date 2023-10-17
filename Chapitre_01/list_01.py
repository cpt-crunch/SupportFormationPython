 # Création de liste
liste = [[1, 2], [1, 3], [1, 4]]
print(liste[0])#Ecriture de la liste 0 (1, 2)
print(liste[1])#Ecriture de la liste 1 (1, 3)
print(liste[2])#Ecriture de la liste 2 (1, 4)

# La sélection des listes s'effectuent en ajoutant une valeur, on sélectionne la valeur que l'ont souhaite affiché en partant de 0 la première parenthèse et ainsi de suite.

# On peux ajouter des valeurs après la création de la liste avec la méthode 'append'

#Ajout de valeurs
liste = []
ptint(liste)#Ici aucune valeur n'a été ajoutée, nous n'avons donc pas besoin de sélectionner une valeur afin de l'afficher
liste.append(1)
print(liste)#On obtiendra par cette commande la valeur ajoutée '1', vu qu'elle est seule elle s'affichera sous la même commande simple
liste.append(2)
print(liste)#Il n'y a toujours qu'une seule valeur présente dans la liste, donc pas obligé de sélectionner la valeur qu'on souhaite afficher