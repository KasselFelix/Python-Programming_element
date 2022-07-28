#Exercice 10.4
LivresBD = {'Les misérables':('Victor Hugo', 5),
'Le dernier des Mohicans' :('James F. Cooper', 0),
'Un animal doué de raison' : ('Robert Merle', 6),
'Le grand Meaulnes' :('Alain Fournier', 1),
'Notre-dame de Paris' :('Victor Hugo', 4),
'Les comtemplations' :('Victor Hugo', 0) }

    #Question 1:

def auteurs(Livres):
    """
    dict[str:tuple[str,int]] -> set(str)
    """

    #E:set(str)
    E=set()

    for (i,j) in Livres.items():
        nom, num = j
        E.add(nom)

    return E

    #Question 2:

def titres_empruntables(Livres):
    """
    dict[str:tuple[str,int]] -> set(str)
    """

    #E:set(str)
    E=set()

    for (i,j) in Livres.items():
        nom, num = j
        if num>0:
            E.add(i)

    return E

#Jeu de test:
assert titres_empruntables(LivresBD)=={'Le grand Meaulnes',
                                       'Les misérables',
                                       'Notre-dame de Paris',
                                       'Un animal doué de raison'}
     #Question 3:

def titres_auteur(auteur, Livres):
    """
    str * dict[str:tuple[str,int]] -> set(str)
    """

    #E:set(str)
    E=set()

    for (i,j) in Livres.items():
        nom, num = j
        if nom==auteur:
            E.add(i)

    return E
    
#Jeu de test:
assert titres_auteur('Victor Hugo', LivresBD)=={'Les comtemplations', 'Les misérables', 'Notre-dame de Paris'}
assert titres_auteur('Robert Merle', LivresBD)=={'Un animal doué de raison'}
assert titres_auteur('Gaston Leroux', LivresBD)==set()

#ExoTP11_gr133.py
import math
import random

base = { 'Bernard': [ 10, 12, 12, 14, 8],
         'Bernardine': [13, 13, 15, 17, 2],
         'Hans': [5, 12, 3, 15, 10],
         'Totoro': [17, 16, 18, 19, 15],
         'Claudine': [ 2, 2, 2, 2, 3],
         'Zebulon': [0, 0, 0, 0, 0] }

    #Question 1:

def moylist(L):
    """
    list(float)->float
    retourne la moyenne de la liste.
    """

    #c:float
    c=0.0

    for i in L:
        c=c+i
    return c/len(L)

#Jeu de test:
assert moylist([1.0,0.5,14.0,8.5])==6.0



    #Question 2:

def liste_tp(L):
    """
    list(int) -> list(int)
    Retourne 3 entiers differents compris entre 0 et len(l) exclu.
    """
    #r:int
    r=int(random.random()*len(L))
    #cpt:int
    cpt=0
    #LL:list(int)
    LL=[]

    while cpt<3:
        if L[r] in LL:
            r=int(random.random()*len(L))
        else:
            LL.append(L[r])
            cpt=cpt+1

    return LL
            
    #Question 3:

def compar_moy(L,Li):
    """
    list(number)*list(int)->list(float)
    Retourne une list avec comparaison de moyenne
    """
    #LL:list(float)
    LL=[0,0,0]

    LL[0]=round(moylist(L),2)
    LL[1]=round(moylist(Li),2)
    LL[2]=max(LL[0],LL[1])
    return LL

    #Question 4:

def dicmoy(D):
    """
    Dict() -> dict[str: list[float]]
    """

    DD=dict()

    for i,j in D.items():

       DD(i)=compar_moy(list_tp(j),list_tp(j))

    return DD
    
