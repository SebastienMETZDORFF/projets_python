# Création du dictionnaire fruits
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Ajout d'une paire clé-valeur
fruits["kiwi"] = "vert"
print(fruits)

# Stocker la valeur de la clé "banane" dans une variable
couleur_banane = fruits["banane"]
print(couleur_banane)

# Modification de la valeur d'une clé
fruits["pomme"] = "vert"
print(fruits)

# Suppression d'une paire clé-valeur
fruits.pop("banane")
print(fruits)

# Affichage des clés restantes dans le dictionnaire
print(fruits.keys())
