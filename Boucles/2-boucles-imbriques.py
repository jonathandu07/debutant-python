# -*- coding: utf-8 -*-
"""
Boucles imbriquées
"""

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8, 9]
    ]

for ligne in matrice:
    for element in ligne:
        print(element, " ")
    print()