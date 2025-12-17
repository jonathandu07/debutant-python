# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 10:57:41 2025

@author: alpha
"""

while True:
    nombre = int(input("Entrez un nombre (entrez un nombre négatif pour arréter) : \n"))
    
    if nombre < 0:
        print("Nombre négatif détecté. Fin de la boucle.")
        break
    
    else :
        print(f"Vous avez rentré : {nombre}")