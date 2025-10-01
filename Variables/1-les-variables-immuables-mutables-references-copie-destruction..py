# -*- coding: utf-8 -*-
"""
Variables immuables vs mutables
"""

# Type Immuables :
a = 10
a = 20

# Types mutables
liste = [1, 2, 3]
#liste[0] = 10

b = liste

#b[0] = 10

import copy

b = copy.deepcopy(liste)
b[0] = 10

x = 10
del x
print(x)