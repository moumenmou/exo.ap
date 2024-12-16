# Demander à l'utilisateur d'entrer un prix en dinars
prix = float(input("Veuillez entrer un prix en dinars (ex: 12.45) : "))

# Séparer la partie entière (dinars) et la partie décimale (centimes)
dinars = int(prix)
centimes = int(round((prix - dinars) * 100))

# Afficher les résultats
print(f"Partie en dinars : {dinars}")
print(f"Partie en centimes : {centimes}")
