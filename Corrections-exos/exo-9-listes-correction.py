# Création de la liste nombres_pairs contenant les nombres pairs de 2 à 20
nombres_pairs = list(range(2, 21, 2))

# Vérification si 4 est présent dans la liste
est_present_4 = 4 in nombres_pairs
print("4 est dans la liste:", est_present_4)

# Vérification si 15 est présent dans la liste
est_present_15 = 15 in nombres_pairs
print("15 est dans la liste:", est_present_15)

# Calcul de la somme des éléments de la liste
somme_nombres_pairs = sum(nombres_pairs)
print("La somme des éléments de la liste est :", somme_nombres_pairs)