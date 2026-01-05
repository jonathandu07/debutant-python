# Demande à l'utilisateur d'entrer trois nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

# Comparaison des trois nombres pour trouver le plus grand
if nombre1 >= nombre2 and nombre1 >= nombre3:
    plus_grand = nombre1
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    plus_grand = nombre2
else:
    plus_grand = nombre3

# Affichage du résultat
print(f"Le plus grand des trois nombres est : {plus_grand}")