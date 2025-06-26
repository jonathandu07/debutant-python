# -*- coding: utf-8 -*-
import copy
a = [1,2,3]

b = a

b[0] = 10
print(a)

# Exemple de copie

c = [4,5,6]
d = copy.deepcopy(c)

d[0] = 10
print(c)

# Destruction d'un variable
e = 10
del e
# print(e) il se produit une erreur car la variable e n'existe plus.