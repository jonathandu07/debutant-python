# On demande à l'utilisateur de saisir une chaîne de caractères au clavier.
# input(...) renvoie toujours une chaîne (str).
chaine = input("Entrez une chaîne de caractères : ")

# On prépare une chaîne vide qui va recevoir, petit à petit,
# les caractères de 'chaine' dans l'ordre inverse.
inverse = ""

# len(chaine) donne le nombre de caractères dans la chaîne.
# Les indices d'une chaîne vont de 0 à len(chaine) - 1.
# Donc on démarre à l'index du dernier caractère.
i = len(chaine) - 1

# Tant que i est valide (>= 0), on continue à parcourir la chaîne à l'envers.
while i >= 0:
    # chaine[i] récupère le caractère à la position i.
    # On l'ajoute à la fin de 'inverse' (concaténation).
    # Exemple : si inverse vaut "c" et chaine[i] vaut "b", inverse devient "cb".
    inverse += chaine[i]

    # On décrémente i pour passer au caractère précédent (on recule dans la chaîne).
    i -= 1

# On affiche le résultat final : la chaîne initiale renversée.
print("Chaîne inversée :", inverse)
