# Création de la liste nombres contenant les nombres de 0 à 9
nombres = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Afficher les éléments de l'indice 2 à 5 (inclus)
elements_2_5 = nombres[2:6]  # Le tranchage s'arrête avant l'indice 6
print("Éléments de l'indice 2 à 5 :", elements_2_5)

# Afficher les 3 derniers éléments
trois_derniers = nombres[-3:]  # Tranchage des trois derniers éléments
print("Les 3 derniers éléments :", trois_derniers)

# Afficher la liste entière à l'envers
liste_inversee = nombres[::-1]  # Tranchage avec un pas de -1 pour inverser la liste
print("Liste entière à l'envers :", liste_inversee)