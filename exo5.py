# Demander les noms et les temps des deux coureurs
nom_coureur1 = input("Veuillez entrer le nom du premier coureur : ")
temps_coureur1 = float(input(f"Veuillez entrer le temps de {nom_coureur1} en secondes : "))

nom_coureur2 = input("Veuillez entrer le nom du deuxième coureur : ")
temps_coureur2 = float(input(f"Veuillez entrer le temps de {nom_coureur2} en secondes : "))

# Comparer les temps et afficher le résultat
if temps_coureur1 < temps_coureur2:
    print(f"{nom_coureur1} est plus rapide.")
elif temps_coureur1 > temps_coureur2:
    print(f"{nom_coureur2} est plus rapide.")
else:
    print("Les deux coureurs ont le même temps.")
