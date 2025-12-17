# Demande de la chaîne de caractères à l'utilisateur
chaine = input("Entrez une chaîne de caractères : ").lower()

# Déclaration des voyelles
voyelles = "aeiouy"

# Initialisation du compteur de voyelles
compteur_voyelles = 0

# Boucle for pour parcourir chaque caractère de la chaîne
for caractere in chaine:
    if caractere in voyelles:
        compteur_voyelles += 1

# Affichage du résultat
print(f"Le nombre de voyelles dans la chaîne est : {compteur_voyelles}")