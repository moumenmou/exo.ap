# Demander les informations nécessaires
total = float(input("Veuillez entrer le montant total de l'achat : "))
nb_articles = int(input("Veuillez entrer le nombre d'articles : "))
jour_semaine = input("Veuillez entrer le jour de la semaine (ex: lundi, mardi, ...): ").lower()

# Appliquer la réduction en fonction du jour de la semaine
if jour_semaine in ['samedi', 'dimanche']:
    remise = 0.20  # 20% de réduction le week-end
else:
    remise = 0.10  # 10% de réduction en semaine

# Appliquer une réduction supplémentaire si le nombre d'articles est supérieur à 5
if nb_articles > 5:
    remise += 0.05  # Ajout de 5% de réduction supplémentaire

# Calculer le prix final
prix_final = total * (1 - remise)

# Afficher le prix total après application de la remise
print(f"Le prix total après remise est : {prix_final:.2f} €")
