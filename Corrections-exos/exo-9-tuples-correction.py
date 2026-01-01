# -*- coding: utf-8 -*-
import time

liste = list(range(1, 1000000001))

tuple_ = tuple(range(1, 1000000001))

milieu = len(liste) // 2

debut_liste = time.time()
element_liste = liste[milieu]
fin_liste = time.time()

debut_tuple = time.time()
element_tuple = liste[milieu]
fin_tuple = time.time()

temps_liste = fin_liste - debut_liste

temps_tuple = fin_tuple - debut_tuple

print(f"Temps d'accès à l'élément du milieu de la liste : {temps_liste}")

print(f"Temps d'accès à l'élément du milieu du tuple : {temps_tuple}")