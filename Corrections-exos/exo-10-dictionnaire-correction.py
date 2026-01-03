# Création de la liste de clés
cles = ["nom", "âge", "ville"]

# Utilisation de fromkeys() pour créer un dictionnaire où chaque clé a la valeur "Inconnu"
inconnu = dict.fromkeys(cles, "Inconnu")

# Affichage du dictionnaire initial
print("Dictionnaire initial :", inconnu)

# Utilisation de update() pour modifier le dictionnaire avec des informations réelles
inconnu.update({"nom": "Alice", "âge": 30, "ville": "Paris"})

# Affichage du dictionnaire final
print("Dictionnaire final après update :", inconnu)