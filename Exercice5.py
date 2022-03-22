# Exercice 5: En se basant sur l'exercice 4, modifier le menu utilisateur en y ajoutant une option lui permettant
# de faire une recherche d'enseignant. Vérifier si l'enseignant entré par l'utilisateur est présent dans votre
# liste de cours et indiquer le résultat à la console.

def planning():

    dico_cours = {}
    dico_cours = {"Keven Presseau-St-Laurent": "Concepts de programmation 1", "Emma Senez": "Logique Mathématiques", "Fisset J": "Systeme d'exploitation"}

    print("Veuillez sélectionner votre cours parmis les choix proposés: ")
    print("#1 Concepts de programmation 1")
    print("#2 Logique Mathématiques")
    print("#3 Systeme d'exploitation")
    print("#4 Rechercher un cours par nom de l'enseignant")

    utilisateur = int(input("Veuillez rentrer votre choix: "))

    if utilisateur == 1:
        print(dico_cours.get("Keven Presseau-St-Laurent"))
        print("Keven Presseau-St-Laurent")
    elif utilisateur == 2:
        print(dico_cours.get("Emma Senez"))
        print("Emma Senez")
    elif utilisateur == 3:
        print(dico_cours.get("Fisset J"))
        print("Fisset J")
    elif utilisateur == 4:
        
    else:
        print("Merci de rentrer un des choix proposés")

planning()