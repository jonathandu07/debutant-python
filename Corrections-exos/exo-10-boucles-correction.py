# Demande à l'utilisateur d'entrer un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Initialisation de la variable pour stocker le factoriel
factoriel = 1

# Boucle for pour calculer le factoriel
for i in range(1, n + 1):
    factoriel *= i  # Multiplie factoriel par i à chaque itération

# Affichage du résultat
print(f"Le factoriel de {n} est : {factoriel}")