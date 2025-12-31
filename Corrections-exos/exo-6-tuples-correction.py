# Importation de namedtuple depuis le module collections
from collections import namedtuple

# Définition du namedtuple Rectangle avec les champs longueur et largeur
Rectangle = namedtuple('Rectangle', ['longueur', 'largeur'])

# Création d'un rectangle avec une longueur de 10 et une largeur de 5
mon_rectangle = Rectangle(longueur=10, largeur=5)

# Affichage des valeurs de longueur et largeur en utilisant les noms des champs
print("Longueur du rectangle :", mon_rectangle.longueur)
print("Largeur du rectangle :", mon_rectangle.largeur)