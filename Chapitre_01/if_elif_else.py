# Démonstration des attributs if, elif et else

#Condition if else
a = 20 #Variable ou 'a' est égal à '20'
if a > 5: #Si 'a' est supérieur à '5'
	a = a + 1 #Alors la variable 'a' sera égal à 'a + 1'
else: #Mais si 'a' est inférieur à '5'
	a = a - 1 #Alors 'a' sera égal à 'a - 1'
#Dans le cas contraire si 'a' s'avère inférieur à '5' alors la condition else s'appliquera

#Condition elif
a = 5 #Variable
if a > 5:
	a = a + 1
elif a == 5: #Si 'a' est égal à '5'
	a = a + 1000 #Alors on ajoute '1000'
else:
	a = a - 1
#Il est possible d'ajouter autant de conditions précises que l'on souhaite en ajoutant le mot clé elif , contraction de "else" et "if", qu'on pourrait traduire par "sinon" 