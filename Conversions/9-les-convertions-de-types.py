# -*- coding: utf-8 -*-
"""
Les conversions de type
"""

a  = 3.14
b = int(a)

c = "42"
d = int(c)

e = True
f = int(e)
"""
g = "Hello"
h = int(g)
"""

a = 5
b = float(a)

c = "3.14"
d = float(c)


a = 123
b = str(a)

e = str(d)

f = True
g = str(f)

a = 0
b = bool(a)

d = bool(c)

e = []
f = bool(e)

a = "Hello"
b = list(a)

c = (1, 2, 3)
d = list(c)

c = tuple(b)

e = tuple(d)

a = [("nom", "Alice"), ("âge", 25)]
b = dict(a)

cles = ["nom", "âge"]
valeurs = ["Bob", 30]

c = dict(zip(cles, valeurs))