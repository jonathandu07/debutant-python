# -*- coding: utf-8 -*-
"""
L'instruction input() pour les entrées utilisateur
"""

#variable = input("Message à afficher : \n")

age = int(input("Quel est votre age ? : \n"))
print(age + 5)

try:
    nombre = int(input("Entrez un nombre : \n"))
except:
    print("Erreur : Ce n'est pas un nombre !")