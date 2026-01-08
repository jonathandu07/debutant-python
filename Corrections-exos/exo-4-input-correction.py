# Demande à l'utilisateur d'entrer les trois notes
note1 = float(input("Entrez la première note sur 20 : "))
note2 = float(input("Entrez la deuxième note sur 20 : "))
note3 = float(input("Entrez la troisième note sur 20 : "))

# Calcul de la moyenne des trois notes
moyenne = (note1 + note2 + note3) / 3

# Affichage du résultat
print(f"La moyenne des trois notes est : {moyenne:.2f}/20")