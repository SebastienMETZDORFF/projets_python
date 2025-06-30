nombres = input("Entrez des nombres séparés par des virgules : ")
# On transforme la chaîne de caractères en liste
liste = nombres.split(",")

# Conversion des chaînes de caractère en entiers et ajout des nombres entiers dans liste_entiers
liste_entiers = []
for nombre in liste:
    liste_entiers.append(int(nombre))
print(f"Liste des nombres entiers : {liste_entiers}")

# Calcul et affichage de la somme des nombres dans la liste
somme = 0
for entier in liste_entiers:
    somme += entier
print(f"Somme des nombres entiers de la liste : {somme}")

# Calcul et affichage de la moyenne des nombres dans la liste
moyenne = somme / len(liste_entiers)
print(f"Moyenne des nombres entiers de la liste : {moyenne}")

# Je calcule et j'affiche le nombre de nombres dans la liste qui sont supérieurs à la moyenne
nombre_de_nombres_superieurs_a_la_moyenne = 0
for entier in liste_entiers:
    if entier > moyenne:
        nombre_de_nombres_superieurs_a_la_moyenne += 1
print(f"Nombre des nombres entiers supérieurs à la moyenne : {nombre_de_nombres_superieurs_a_la_moyenne}")
