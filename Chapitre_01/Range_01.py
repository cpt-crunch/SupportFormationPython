# Démonstration de "range"

# Exemple de 'range' sur une liste
# Un 'range' représente un intervalle entre deux nombres entiers, on peut le voir comme la liste des nombres entre ces deux bornes
# L'intervalle formé entre 1 et 10 se note par exemple 'range(1, 10)'. Il faut savoir que c'est un intervallee fermé à gauche mais ouvert à droite, il contient ainsi 1 mais pas 10 (il s'arrête à 9)

for n in range(1, 10):
    print(n)

# Utiliser la valeur de la variable 'n' dans un exemple de calcul

for n in range(1, 11):
    print('3 x', n, '=', 3 * n)

# Le premier argument donné à 'range' est optionnel

for n in range(5): # Est équivalent à 'range(0, 5)
    print(n) 

# Exemple de 'print' en chiffres pairs

for n in range(0, 10, 2): # Le '2' servira d'afficher les pairs de 1 à 8
    print(n)


