# -*- coding: utf-8 -*-
"""
Les conditions avancées
"""

age = 20
citoyennete = True

if age >= 18:
    if citoyennete:
        print("Vous pouvez voter.")
    else :
        print("Vous ne pouvez pas voter.")
else:
    print("Vous ne pouvez pas voter.")
    

age = 18
message = "Majeur" if age >= 18 else "Mineur"
print(message)