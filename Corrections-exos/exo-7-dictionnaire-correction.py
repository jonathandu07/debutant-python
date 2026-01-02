# -*- coding: utf-8 -*-
# Création du dictionnaire classe
classe = {
    "Alice": {"math": 85, "physique": 90, "informatique": 95},
    "Bob": {"math": 78, "physique": 82, "informatique": 88},
    "Charlie": {"math": 92, "physique": 87, "informatique": 91}
}

# Accès à la note de "math" pour un élève spécifique, par exemple "Bob"
note_math_bob = classe["Bob"]["math"]

# Affichage de la note de math pour Bob
print(f"La note de math pour Bob est : {note_math_bob}")