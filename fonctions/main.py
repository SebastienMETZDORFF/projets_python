def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

# Je demande à l'utilisateur d'entrer un salaire annuel (il ne faut pas oublier de le convertir en float)
salaire_annuel = float(input("Entrez un salaire annuel : "))

# Je demande à l'utilisateur d'entrer le nombre d'heures travaillées par semaine
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))

# Appel de fonctions
resultat_salaire_mensuel = salaire_mensuel(salaire_annuel)
resultat_salaire_hebdomadaire = salaire_hebdomadaire(resultat_salaire_mensuel)
resultat_salaire_horaire = round(salaire_horaire(resultat_salaire_hebdomadaire, heures_travaillees), 2)

# J'affiche le salaire horaire
print(f"Votre salaire horaire est de {resultat_salaire_horaire} euros.")
