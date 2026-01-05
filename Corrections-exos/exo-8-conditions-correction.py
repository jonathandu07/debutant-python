# Demande à l'utilisateur d'entrer son âge
age = int(input("Entrez votre âge : "))

# Demande à l'utilisateur s'il possède un permis de conduire (oui ou non)
permis = input("Avez-vous un permis de conduire ? (oui/non) : ").strip().lower()

# Vérification des conditions pour l'autorisation de conduire
if age >= 18:
    if permis == "oui":
        print("Vous êtes autorisé à conduire.")
    else:
        print("Vous devez avoir un permis de conduire pour être autorisé à conduire.")
else:
    print("Vous devez avoir 18 ans ou plus pour conduire.")