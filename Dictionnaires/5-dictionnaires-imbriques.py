# -*- coding: utf-8 -*-
"""
Dictionnaires imbriqués et avancés
"""

etudiant = {
    "nom" : "Alice",
    "âge" : 25,
    "cours" : {
        "math" : 85,
        "physique" : 90,
        "informatique" : 95
        }
    }

print(etudiant["cours"]["math"])

liste_tuples = [("nom", "Alice"), ("âge", 25), ("Ville", "Paris")]
mon_dict = dict(liste_tuples)
print(mon_dict)

cles = ["nom", "âge", "ville"]
valeurs = ["Alice", 25, "Paris"]
monDict = dict(zip(cles, valeurs))
print(monDict)