# -*- coding: utf-8 -*-
"""
Les chaînes de caractères
"""

chaine1 = 'Bonjour'
chaine2 = "L'oiseau"
chaine3 = """Texte
Multi-ligne"""

texte = "Bonjour \nComment ça va ?"
print(texte)
print("Hello" + " " + "wolrd")
print("abc" * 3)
s = "Python"
print(s[0])
print(s[-1])
print(s[1:4])

chaine = "Python"
nouvelle_chaine = "J" + chaine[1:]
print(nouvelle_chaine)

print("Bonjour".upper())
print("BONJOUR".lower())
print("    Bonjour             ".strip())
print("Bonjour tout le monde".replace("Bonjour", "Salut"))
print("un,deux,trois".split(","))
liste = ["un", "deux", "trois"]
print(", ".join(liste))



