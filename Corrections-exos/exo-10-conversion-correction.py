# Demande à l'utilisateur d'entrer une chaîne de caractères
chaine = input("Entrez une chaîne de caractères : ")

# Tentative de conversion de la chaîne en entier
try:
    nombre = int(chaine)
    print(f"La chaîne '{chaine}' a été convertie en entier : {nombre}")
except ValueError:
    print(f"Erreur : La chaîne '{chaine}' ne peut pas être convertie en entier.")