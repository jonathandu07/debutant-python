# -*- coding: utf-8 -*-
"""
Copie et méthodes avancées des dictionnaires
"""

personne = {"nom" : "Alice", "âge" : 25}

copie_personne = personne.copy()

autre_copie = dict(personne)

copie_personne["âge"] += 1

carres = {x: x**2 for x in range(1, 6)}
print(carres)

cles = ["nom", "âge", "ville"]
mon_dict = dict.fromkeys(cles, "inconnu")
print(mon_dict)