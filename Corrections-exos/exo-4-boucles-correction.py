# Création de la liste de nombres
nombres = [3, 7, 10, 15, 18, 21, 25, 30]

# Nombre à rechercher
nombre_recherche = 15

# Initialisation de l'indice pour la boucle while
index = 0

# Variable pour suivre si le nombre a été trouvé
trouve = False

# Boucle while pour rechercher le nombre
while index < len(nombres):
    if nombres[index] == nombre_recherche:
        trouve = True
        break
    index += 1

# Affichage du résultat
if trouve:
    print(f"Le nombre {nombre_recherche} a été trouvé dans la liste.")
else:
    print(f"Le nombre {nombre_recherche} n'a pas été trouvé dans la liste.")