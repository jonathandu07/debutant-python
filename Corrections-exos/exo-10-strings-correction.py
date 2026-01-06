import re

# Fonction pour valider une adresse email
def valider_email(email):
    # Expression régulière pour valider une adresse email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Utilisation de re.match() pour vérifier si l'email correspond au pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test de la fonction avec des exemples
email1 = "test@example.com"
email2 = "invalid-email@"

print(f"'{email1}' est valide : {valider_email(email1)}")
print(f"'{email2}' est valide : {valider_email(email2)}")