# Création du dictionnaire notes
notes = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

# Parcourir le dictionnaire pour afficher chaque étudiant avec sa note
for etudiant, note in notes.items():
    print(f"{etudiant} a obtenu la note de {note}.")