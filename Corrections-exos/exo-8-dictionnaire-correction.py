# Création des listes noms et ages
noms = ["Alice", "Bob", "Charlie"]
ages = [24, 27, 22]

# Utilisation de zip() pour associer chaque nom à l'âge correspondant et création du dictionnaire
etudiants = dict(zip(noms, ages))

# Affichage du dictionnaire
print("Dictionnaire des étudiants :", etudiants)