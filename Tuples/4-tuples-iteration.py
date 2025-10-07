# -*- coding: utf-8 -*-
"""
Itération et utilisation avancée des tuples
"""

mon_tuple = ("pomme", "banane", "cerise")
for fruit in mon_tuple:
    print(fruit)
    
mon_tuple = (1, 2, 3)
a, b, c = mon_tuple
print(a, b, c)

tuples_list = [(1, 'a'), (2, 'b')]
for number, letter in tuples_list:
    print(number, letter)
    
mon_dict = {(1, 2): "point A", (3, 4): "Point B"}
print(mon_dict[1, 2])

ma_liste = [1, 2, 3]
mon_tuple = tuple(ma_liste)
print(mon_tuple)

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)









