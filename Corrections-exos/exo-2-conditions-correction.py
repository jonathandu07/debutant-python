# Demande à l'utilisateur d'entrer son âge
age = int(input("Entrez votre âge : "))

# Vérification si l'utilisateur est majeur ou mineur
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")