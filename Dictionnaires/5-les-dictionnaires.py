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
