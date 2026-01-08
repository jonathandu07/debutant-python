# Initialisation de la liste pour stocker les lignes de la biographie
biographie = []

print("Entrez votre biographie. Tapez 'fin' pour terminer la saisie.")

# Boucle pour recueillir les lignes de la biographie
while True:
    ligne = input()
    if ligne.lower() == "fin":
        break
    biographie.append(ligne)

# Affichage de la biographie complète
print("\nVotre biographie complète est :")
print("\n".join(biographie))