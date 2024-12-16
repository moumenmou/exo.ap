# Demander à l'utilisateur d'entrer une année
annee = int(input("Veuillez entrer une année : "))

# Vérifier si l'année est bissextile
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(f"{annee} est une année bissextile.")
else:
    print(f"{annee} n'est pas une année bissextile.")
