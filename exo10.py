# Demander à l'utilisateur de saisir un mot
mot = input("Veuillez entrer un mot : ")

# Initialiser une variable pour indiquer si le mot est un palindrome
est_palindrome = True

# Boucle pour parcourir la première moitié du mot
for i in range(len(mot) // 2):
    # Comparer le caractère à l'index i avec le caractère à l'index négatif correspondant
    if mot[i] != mot[-(i + 1)]:
        est_palindrome = False
        break

# Afficher le résultat en fonction de la valeur de est_palindrome
if est_palindrome:
    print("Oui, c'est un palindrome.")
else:
    print("Non, ce n'est pas un palindrome.")
