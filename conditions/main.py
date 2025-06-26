# Demande à l'utilisateur d'entrer deux nombres
nombre1 = input("Entrez un premier nombre : ")
nombre2 = input("Entrez un second nombre : ")

# Si une des deux variables n'est pas un nombre, alors l'utilisateur sort du programme avec un message d'erreur
if not nombre1.isnumeric() or not nombre2.isnumeric():
    raise SystemExit("Vous n'avez pas entré deux nombres !")
else:
    # Les deux variables sont des nombres.
    # Je convertis les deux chaînes de caractère en nombres entiers
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
    
    # Demande à l'utilisateur d'entrer une opération
    operation = input("Entrez une opération (+, -, *, /) : ")
    
    # Teste la variable operation avec un match case
    match operation:
        case "+":
            resultat = nombre1 + nombre2
        case "-":
            resultat = nombre1 - nombre2
        case "*":
            resultat = nombre1 * nombre2
        case "/":
            if nombre2 == 0:
                raise SystemExit("Vous ne pouvez pas diviser un nombre par zéro !")
            else:
                resultat = round(nombre1 / nombre2, 2)
        case _:
            raise SystemExit("Vous avez entré un caractère invalide pour l'opération !")
        
    # Afficher le résultat de l'opération
    print(f"Le résultat de l'opération est égal à {resultat}")
