# -*- coding: utf-8 -*-
"""
Les Boucles
"""

fruits = ["pomme", "banane", "cerise"]
for fruit in fruits :
    print(fruit)
    
for caractere in "Python":
    print(caractere)
    
for i in range(1,10, 2):
    print(i)


print("=================== WHILE ===================")
i = 0    
while i < 5:
    print(i)
    i += 1
    
    
commande = "Stop"
while commande != "Stop":
    commande = input("Entrez une commande :\n")
    
    
print("=================== break ===================")
for i in range(10):
    if i == 9:
        break
    print(i)

print("=================== continue ===================")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("=================== continue ===================")
for i in range (8):
    print(i)
else :
    print("La boucle est terminée !")