# Exercice 2:
# Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. Ensuite, créer deux copies de cette liste, une copie en surface
# et une copie profonde intitulée respectivement surface et profonde. Finalement, demander à l'utilisateur d'entrer un mot,
# modifier le 2e élément de la liste «surface» et le 3e élément de la liste «profonde» et imprimer les trois listes à la console

import copy
def ensemble():
    elements = [1, 2, 5, 3, 4]
    surface = elements[:]
    profonde = copy.deepcopy(elements)

    mot_utilisateur = input("Veuillez entrer un mot: ")

    del surface[1]
    surface.insert(1,mot_utilisateur)

    del profonde[1]
    profonde.insert(1,mot_utilisateur)

    print(elements)
    print(surface)
    print(profonde)

ensemble()




