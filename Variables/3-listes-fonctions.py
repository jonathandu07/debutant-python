# -*- coding: utf-8 -*-
"""
Fonctions et méthodes utiles pour les listes
"""

# connaitre la longueur d'une liste
fruits = ["pomme", "banane", "cerise"]
print(len(fruits))

nombres = [7, 2, 4, 5, 8, 3 ,1, 9, 6]
print(sorted(nombres))

print(min(nombres))
print(max(nombres))

chaine = "python"
print(list(chaine))

print(fruits.index("cerise"))

nombres = [7, 2, 4, 5, 8, 3 ,1, 9, 6, 5, 4, 7]
print(nombres.count(4))

fruits.reverse()
print(fruits)

nombres.sort()
print(nombres)

noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = zip(noms, ages)
print(list(zipped))

for index, fruit in enumerate(fruits):
    print(index, fruit)
    
doubles = map(lambda x: x * 2, nombres)
print(list(doubles))

pairs = filter(lambda x: x % 2 == 0, nombres)
print(list(pairs))

from functools import reduce

somme = reduce(lambda x, y: x + y, nombres)
print(somme)












