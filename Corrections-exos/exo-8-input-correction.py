# Demande à l'utilisateur d'entrer deux nombres
try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
except ValueError:
    print("Erreur : Vous devez entrer des nombres valides.")
    exit()

# Demande à l'utilisateur d'entrer une opération
operation = input("Entrez une opération (+, -, *, /) : ")

# Calcul et affichage du résultat
if operation == "+":
    resultat = nombre1 + nombre2
    print(f"Le résultat de {nombre1} + {nombre2} est : {resultat}")
elif operation == "-":
    resultat = nombre1 - nombre2
    print(f"Le résultat de {nombre1} - {nombre2} est : {resultat}")
elif operation == "*":
    resultat = nombre1 * nombre2
    print(f"Le résultat de {nombre1} * {nombre2} est : {resultat}")
elif operation == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        print(f"Le résultat de {nombre1} / {nombre2} est : {resultat}")
    else:
        print("Erreur : Division par zéro impossible.")
else:
    print("Erreur : Opération non valide.")