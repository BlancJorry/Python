#1
import string
import random
def rev(r):
    return print(r[::-1])

antre = input("tape on mo:")
rev(antre)

#2
def chAl():
    antreval=int(input("antre on chif"))
    c=string.ascii_letters
    cA="".join(random.choice(c)for _ in range(antreval))
    return print(cA)
chAl()

#3
def fusionner_dictionnaires(dict1, dict2):
    resultat = dict(dict1)

    for cle, valeur in dict2.items():
        if cle in resultat:
            valeur_actuelle = resultat[cle]
            if isinstance(valeur, int):
                if isinstance(valeur_actuelle, int):
                    resultat[cle] = valeur_actuelle + valeur
            elif isinstance(valeur, (str, list, set)):
                if isinstance(valeur_actuelle, (str, list, set)):
                    resultat[cle] = valeur_actuelle + valeur
        else:
            resultat[cle] = valeur

    return resultat

dict1 = {"a": 1, "b": "Hello", "c": [1, 2]}
dict2 = {"a": 2, "b": " World", "d": 42}

nouveau_dict = fusionner_dictionnaires(dict1, dict2)
print(nouveau_dict)


#4
def chAl1():
    antreval=int(input("antre on chif"))
    c=string.ascii_letters+string.digits
    cA="".join(random.choice(c)for _ in range(antreval))
    return print(cA)
chAl1()

#5
"""lis="ghcklului7864@#*-"
lisn="@#$%^&*"
def slug():
    for i in range(0,6):
        ch = random.choice(lis)
        if ch == lisn:

        ch_sl="".join(ch)"""

#6
def movig():
    antre = input("antre on mo:")
    movigul = ",".join(antre)
    print(movigul)
movig()

#7


#8


#9
def dpara(a,b):
    res1 = a
    res2 = b
    restup = (a,b)
    return print(res1,res2,restup)
dpara(3,9)

#10