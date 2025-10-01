# -*- coding: utf-8 -*-
x = 10
y = 3.14
nom = "Alice"

ma_variable = 10
_prenom = "Bruno"
maVariable = 15.5


#prix (float)
prix_pomme = 0.5
prix_banane = 0.3
prix_orange = 0.7

# Quantité
qte_pomme = 4
qte_banane = 6
qte_orange = 3

# Nom du client (str)
nom_client = "Alice"

total = (prix_pomme * qte_pomme) + (prix_banane * qte_banane) + (prix_orange * qte_orange)

# Affichage
print("Ticket de caisse pour :", nom_client)
print("Pommes :", qte_pomme, "x", prix_pomme, "€")
print("Bananes :", qte_banane, "x", prix_banane, "€")
print("Oranges :", qte_orange, "x", prix_orange, "€")
print("TOTAL :", total, "€")

# Profil utilisateur (dict)
utilisateur = {
"nom": "Jonathan",
"age": 25,
"email": "jonathan@example.com",
"abonne": True,
"amis": ["Alice", "Bob", "Charlie"],
}
print("=== Profil Utilisateur ===")
print("Nom :", utilisateur["nom"])
print("Âge :", utilisateur["age"])
print("Email :", utilisateur["email"])
print("Abonné :", "Oui" if utilisateur["abonne"] else "Non")
print("\nListe des amis :")
for ami in utilisateur["amis"]:
    print("-", ami)