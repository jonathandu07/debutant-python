# Création du dictionnaire personne
personne = {
    "nom": "Alice",
    "âge": 30,
    "ville": "Paris",
    "profession": "Ingénieur"
}

# Suppression de la clé "profession" en utilisant del
del personne["profession"]

# Suppression de la clé "ville" en utilisant pop()
personne.pop("ville")

# Affichage du dictionnaire restant
print("Dictionnaire après suppression :", personne)