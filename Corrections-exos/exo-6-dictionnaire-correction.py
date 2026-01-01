# Création du dictionnaire personne
personne = {
    "nom": "Alice",
    "âge": 30
}

# Utilisation de get() pour accéder à la clé "ville" avec une valeur par défaut
ville = personne.get("ville", "Non spécifié")
print(f"Ville avant setdefault : {ville}")

# Utilisation de setdefault() pour ajouter la clé "ville" avec la valeur "Paris" si elle n'existe pas
personne.setdefault("ville", "Paris")

# Affichage du dictionnaire mis à jour
print("Dictionnaire personne mis à jour :", personne)