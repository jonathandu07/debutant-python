# Affichage du menu
print("Menu :")
print("1. Ajouter")
print("2. Supprimer")
print("3. Quitter")

# Demande à l'utilisateur de choisir une option
choix = input("Choisissez une option (1, 2, 3) : ")

# Utilisation de l'instruction match pour exécuter l'action correspondante
match choix:
    case "1":
        print("Vous avez choisi d'ajouter un élément.")
    case "2":
        print("Vous avez choisi de supprimer un élément.")
    case "3":
        print("Vous avez choisi de quitter le programme.")
    case _:
        print("Option non valide, veuillez choisir 1, 2 ou 3.")