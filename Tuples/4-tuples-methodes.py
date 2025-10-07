# -*- coding: utf-8 -*-
"""
Méthodes des tuples
"""

mon_tuple = (1, 2, 3, 2, 2)
print(mon_tuple.count(2))

print(mon_tuple.index(3))

tuple1 = (1, 2, 3)
tuple2 = (4, 5 ,6)
tuple3 = tuple1 + tuple2
print(tuple3)

mon_tuple = mon_tuple*3
print(mon_tuple)

print(2 in mon_tuple)

mon_tuple = (0,1, 2, 3, 4, 5)
print(mon_tuple[2:5])
x = 5
print(mon_tuple[:x])