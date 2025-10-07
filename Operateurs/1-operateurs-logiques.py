# -*- coding: utf-8 -*-
"""
Les opérateurs logiques
"""

age = 20
abonne = True

# Condition : L'utilisateur doit être majeur ET abonné pour se connecter !
if age >= 18 and abonne:
    print("Accès autorisé !")
else:
    print("Accès refusé :-(")
    
# ######################################

# Le OR

if age < 18 or age > 65:
    print("Tarif réduit !")
else :
    print("Plein tarif !")
    
# ########################################

# Not

connecte = False

if not connecte :
    print("Veuillez vous connecter d'abord !")

