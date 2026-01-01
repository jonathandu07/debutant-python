# Création du dictionnaire stock
stock = {
    "pomme": 50,
    "banane": 30,
    "orange": 20
}

# Vérification de l'existence de la clé "cerise"
if "cerise" not in stock:
    # Ajout de "cerise" avec une quantité de 100
    stock["cerise"] = 100

# Affichage du dictionnaire mis à jour
print("Dictionnaire stock mis à jour :", stock)
