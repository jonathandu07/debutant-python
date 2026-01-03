# Demande à l'utilisateur d'entrer un nombre
nombre = float(input("Entrez un nombre : "))

# Vérification du signe du nombre et affichage du message correspondant
if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est nul.")