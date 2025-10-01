# -*- coding: utf-8 -*-

nb_articles = 5
print("Le panier contient", nb_articles, "articles.")

prix_ht = 19.90
tva = 0.20
prix_ttc = prix_ht * (1 + tva)

print("Prix TTC :", prix_ttc)

a = 2 + 3j # Nombre complexe

print(a)

nom = "Alice"
print (f"Bonjour {nom}, bienvenue dans la formation !")

est_connecte = False

if est_connecte:
    print (f"{nom} est connectée !")
else:
    print (f"{nom} n'est pas connectée !")
    
notes = [15, 12, 18, 10]
moyenne = sum(notes)/len(notes)
# print("Moyenne :", moyenne)

notes = [8, 12, 18, 10]
moyenne = sum(notes)/len(notes)
print("Moyenne :", moyenne)

position = (45.7640, 4.8357)
print("Latitude :", position[0], "longitude :", position[1])


mon_set = {1, 2, 3, 3}
print(mon_set)

mon_set = {1, 2, 3, 3}
print(mon_set)

utilisateur = {"nom" : "Alice", "âge" : 25, "email" : "alice@exemple.com"}
print(utilisateur["nom"])

def trouver_utilisateur (id):
    if id != 1:
        return None
    return {'nom' : "Alice"}

print(trouver_utilisateur(2))

data = b'Bonjour'
print(data[0])

ba = bytearray(b'hello')
ba[0] = 72
print(ba)





















