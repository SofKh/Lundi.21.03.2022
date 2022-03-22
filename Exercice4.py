# Exercice 4:

dico_cours2 = {}
f1=open("bdd.txt", "r", encoding='utf8')
s=f1.read().split("\n")

dico_cours2[s[0]] = s[1]
dico_cours2[s[2]] = s[3]
dico_cours2[s[4]] = s[5]

print(dico_cours2)













