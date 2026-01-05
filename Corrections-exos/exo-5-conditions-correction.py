# Demande à l'utilisateur d'entrer sa note
note = float(input("Entrez votre note (entre 0 et 100) : "))

# Vérification de la note et affichage de l'appréciation correspondante
if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
else:
    print("Peut mieux faire")