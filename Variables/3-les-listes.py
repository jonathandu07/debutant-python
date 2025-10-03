# -*- coding: utf-8 -*-
"""
Les listes
"""

# Création d'une liste

vide = [] # liste vide
nombres = [1 , 2, 3 , 4]
fruits = ['pomme', 'banane']
mixte = [1, 'pomme', 3.14, True]
imbrique = [1, [2, 3], 4]

# Accès aux éléments
print(fruits[0])
print(fruits[1])

print(imbrique[1][1])

# Modifier des éléments
fruits = ['pomme', 'banane', 'cerise']
fruits[1] = "orange"
print(fruits)


# Ajout d'élements
fruits.append("banane")
fruits.insert(1, "mangue")
fruits.extend(["kiwi", "melon"])

# Suppresion d'éléments
fruits.remove("banane")
print(fruits)
dernier = fruits.pop()
print(dernier)
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)










