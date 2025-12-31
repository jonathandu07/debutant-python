# Création du dictionnaire points avec des tuples comme clés
points = {
    (1, 2): "A",
    (3, 4): "B",
    (5, 6): "C"
}

# Affichage de la valeur associée à une clé spécifique
coord = (3, 4)
print(f"La valeur associée à la clé {coord} est :", points[coord])