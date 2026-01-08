# Demande à l'utilisateur d'entrer un nombre
try:
    nombre = float(input("Entrez un nombre : "))
    print(f"Vous avez entré le nombre : {nombre}")
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")