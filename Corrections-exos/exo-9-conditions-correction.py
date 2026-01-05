# Demande à l'utilisateur d'entrer un nombre
nombre = float(input("Entrez un nombre : "))

# Utilisation d'un if ternaire pour déterminer si le nombre est positif ou négatif/nul
resultat = "Positif" if nombre > 0 else "Négatif"

# Affichage du résultat
print(resultat)