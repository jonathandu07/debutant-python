# Création de la liste des jours de la semaine
jours_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
weekend = ["samedi", "dimanche"]

# Demande à l'utilisateur d'entrer un jour
jour = input("Entrez un jour de la semaine : ").strip().lower()

# Vérification si le jour est un jour de semaine ou du week-end
if jour in jours_semaine:
    print(f"{jour.capitalize()} est un jour de semaine.")
elif jour in weekend:
    print(f"{jour.capitalize()} est un jour du week-end.")
else:
    print("Ce n'est pas un jour valide.")