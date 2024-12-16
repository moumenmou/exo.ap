# Demander à l'utilisateur d'entrer un nombre entier
nombre = int(input("Veuillez entrer un nombre entier : "))

# Vérifier les conditions et afficher le message correspondant
if nombre % 3 == 0 and nombre % 5 == 0:
    print("FizzBuzz")
elif nombre % 3 == 0:
    print("Fizz")
elif nombre % 5 == 0:
    print("Buzz")
else:
    print("Le nombre n'est divisible ni par 3 ni par 5.")
