# Exercice 1:
# Créer une liste contenant tous les nombres premiers entre 2 et 20. Ensuite, demander à l'utilisateur d'écrire un nombre
# entre 2 et 20 (bien vérifier si c'est le cas) et vérifier si ce nombre est premier à l'aide de votre liste
# en affichant le résultat à la console.

def prime():
    premiers = [2, 3, 5, 7, 11, 13, 17, 19]

    utilisateur = int(input("Merci d'écrire un nombre entre 2 et 20: "))
    if 2 <= utilisateur <= 20:
        print(utilisateur in premiers)
    else:
        return "Votre nombre n'est pas entre 2 et 20"

prime()





