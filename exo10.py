
mot = input("Veuillez entrer un mot : ")


est_palindrome = True


for i in range(len(mot) // 2):
   
    if mot[i] != mot[-(i + 1)]:
        est_palindrome = False
        break


if est_palindrome:
    print("Oui, c'est un palindrome.")
else:
    print("Non, ce n'est pas un palindrome.")
