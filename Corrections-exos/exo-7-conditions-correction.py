# Demande à l'utilisateur d'entrer le montant de ses achats
montant_achats = float(input("Entrez le montant de vos achats en euros : "))

# Vérification si le montant dépasse 100 euros pour appliquer la réduction
if montant_achats > 100:
    reduction = montant_achats * 0.10  # Calcul de la réduction de 10 %
    montant_final = montant_achats - reduction
    print(f"Une réduction de 10 % est appliquée. Montant final à payer : {montant_final:.2f} euros.")
else:
    montant_final = montant_achats
    print(f"Pas de réduction appliquée. Montant final à payer : {montant_final:.2f} euros.")