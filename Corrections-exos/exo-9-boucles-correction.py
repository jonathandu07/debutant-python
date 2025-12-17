# Boucle for pour les lignes
for i in range(1, 4):  # i représente les lignes, de 1 à 3
    # Boucle for pour les colonnes
    for j in range(1, 4):  # j représente les colonnes, de 1 à 3
        print(f"({i}, {j})", end=" ")  # Affiche les coordonnées, reste sur la même ligne
    print()  # Saute à la ligne suivante après avoir affiché une ligne complète
