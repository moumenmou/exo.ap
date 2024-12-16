# Initialiser une liste pour stocker les villes et leurs populations
villes = []

# Boucle pour demander les noms des villes à l'utilisateur
while True:
    ville = input("Veuillez entrer le nom d'une ville (ou tapez 'stop' pour terminer) : ")
    
    # Vérifier si l'utilisateur a tapé "stop" pour arrêter la saisie
    if ville.lower() == "stop":
        break
    
    # Calculer la population en fonction du nombre de lettres dans le nom de la ville
    population = len(ville) * 1000000
    
    # Ajouter la ville et sa population à la liste
    villes.append((ville, population))

# Trier les villes par population décroissante
villes.sort(key=lambda x: x[1], reverse=True)

# Afficher les villes et leurs populations
print("\nVilles et leurs populations (triées par ordre décroissant de population) :")
for ville, population in villes:
    print(f"{ville}: {population:,} citoyens")
