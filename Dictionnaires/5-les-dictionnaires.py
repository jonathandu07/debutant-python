# -*- coding: utf-8 -*-
"""
Les dictionnaires
"""

mon_dict = {}

mon_dict = {"nom" : "Alice", "âge" : 25, "ville" : "Paris"}

mon_dict = dict(nom = "Alice", âge = 25, ville = "Paris")
print(mon_dict["nom"])

personne = {"nom" : "Alice", "âge" : 25}

personne["âge"] = 26

personne["pays"] = "France"
print(personne)

personne["ville"] = "Paris"
print(personne)
del personne["ville"]
print(personne)
age = personne.pop("âge")
print(personne)
personne.clear()
print(personne)
personne["nom"] = "Phillipe"
print("nom" in personne)
print("pays" in personne)






