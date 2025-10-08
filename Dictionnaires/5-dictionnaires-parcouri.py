# -*- coding: utf-8 -*-
"""
Parcourir un dictionnaire
"""

personne = {"nom" : "Alice", "âge" : 25, "ville" : "Paris"}

for clef in personne.keys():
    print(clef)

print("-----------------------------")

for valeur in personne.values():
    print(valeur)

print("-----------------------------")

for cle, valeur in personne.items():
    print(cle, valeur)
    
print("-----------------------------")    
    
personne = {"nom": "Alice", "âge": 25}    
print(personne.get("ville", "Non spécifié"))

print("-----------------------------")

personne.setdefault("Pays", "France")
print(personne)

print("-----------------------------")

personne.update({"ville" : "Paris", "Région" :"ile-de-France"})
print(personne)











