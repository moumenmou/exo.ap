# Demander à l'utilisateur la température
temperature = int(input("Veuillez entrer la température (en entier) : "))

# Vérifier les conditions et afficher les messages correspondants
if temperature < 0:
    print("Il fait très froid !")
elif temperature < 10:
    print("Il fait froid !")
elif temperature < 20:
    print("Il fait frais !")

# Message de fin
print("Restez prudent !")
