# Création de la chaîne texte
texte = "Les roses sont rouges, les violettes sont bleues"

# Trouver l'indice de la première occurrence du mot "sont"
indice_sont = texte.find("sont")

# Compter le nombre de fois que "sont" apparaît dans la chaîne
nombre_sont = texte.count("sont")

# Affichage des résultats
print(f"L'indice de la première occurrence de 'sont' est : {indice_sont}")
print(f"Le mot 'sont' apparaît {nombre_sont} fois dans la chaîne.")