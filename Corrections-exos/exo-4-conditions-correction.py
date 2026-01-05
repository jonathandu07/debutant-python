# Demande à l'utilisateur d'entrer un nombre
nombre = int(input("Entrez un nombre : "))

# Vérification de la parité du nombre
if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")