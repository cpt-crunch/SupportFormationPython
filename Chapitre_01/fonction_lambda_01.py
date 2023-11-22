# Démonstration d'un fonction lambda

my_list = [1, 2, 3, 4, 5]
list(filter(lambda x: x > 2, my_list))
print(my_list)

def second_list(x):
    return x > 2
my_list = [1, 2, 3, 4, 5]
list(filter(second_list, my_list))
print(my_list)

# La création d'une fonction lanbda va permettre de simplifié l'écriturre ainsi que la leecture du code. Comme nous pouvons le constater la fonction lambda regroupera la liste en 1 seule ligne contraiement à une fonction simple
# Pas besoin de chercher une 'définition' quelquonque. On consstate doncc que les deux fonction retournerons exactement le même résultat