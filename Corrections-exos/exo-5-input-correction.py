# Affichage du menu
print("Menu :")
print("1. Ajouter")
print("2. Supprimer")
print("3. Quitter")

# Demande à l'utilisateur de faire un choix
choix = input("Faites un choix (1, 2, ou 3) : ")

# Vérification du choix et affichage du message correspondant
if choix == "1":
    print("Vous avez choisi d'ajouter un élément.")
elif choix == "2":
    print("Vous avez choisi de supprimer un élément.")
elif choix == "3":
    print("Vous avez choisi de quitter le programme.")
else:
    print("Choix invalide. Veuillez entrer 1, 2, ou 3.")