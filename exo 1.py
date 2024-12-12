import math

# Demander à l'utilisateur le nombre de personnes
personnes = int(input("Combien de personnes ont besoin d'un trajet ? "))
capacite_taxi = int(input("Combien de personnes peuvent entrer dans un taxi ? "))

# Calculer le nombre de taxis nécessaires
taxis_necessaires = math.ceil(personnes / capacite_taxi)

# Afficher le résultat
print(f"Il vous faudra {taxis_necessaires} taxis pour transporter {personnes} personnes.")