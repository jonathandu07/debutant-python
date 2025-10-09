# -*- coding: utf-8 -*-
"""
Conditions avancées : pass , structures de données et match
"""

age = 20

if age >= 18:
    pass
else:
    print("Vous êtes mineur !")
    
fruits = ["pomme", "banane", "cerise"]

if "pomme" in fruits:
    print("Il y a des pommes")
else:
    print("il n'y a pas de pommes.")
    
    
choix = 1

match choix:
    case 1:
        print("Nouveau fichier")
    case 2:
        print("Ouvrir un fichier")
    case 3:
        print("Sauvegarder")
    case _:
        print("Option inconue")