import math
import random

#Exercice 3.1

    #Question 1:
def somme_impairs_inf(n):
    
    """
    Number -> Number
    Hypothèse : n est strictement positif.
    Calcul la somme des entiers inférieurs ou égaux à n.
    """

    #s:int
    s=0
    
    #i:int
    i=1

    while i<=n:
        s=s+i
        i=i+2

    return s

#Jeu de tests:

assert somme_impairs_inf(1)==1
assert somme_impairs_inf(2)==1
assert somme_impairs_inf(5)==9

    #Question 2:

def somme_premiers_impairs(n):
    
    """
    Number -> Number
    Hypothèse : n est strictement positif.
    Calcul la somme des n premiers entiers impairs.
    """
    
    #s:int
    s=0

    #i:int
    i=1

    while i<n*2:
        s=s+i
        i=i+2

    return s

#Jeu de tests:

assert somme_premiers_impairs(1)==1
assert somme_premiers_impairs(2)==4
assert somme_premiers_impairs(5)==25

#Exercice 3.2:

    #Question 1:

def reste(n,d):

    """
    Number^2 -> Number
    Renvoie le reste d'une division euclidienne.
    """

    #i:int
    i=0

    while i*d<=n:
        i=i+1
        
    return n-(i-1)*d

#Jeu de tests:

assert reste(11,4)==3
assert reste(21,7)==0
assert reste(0,3)==0

    #Question 2:

def est_divisible(a,b):

    """
    Number^2 -> Boolean
    Retourne vrai si a est divisible par b.
    """

    if reste(a,b)==0:
        return True

    else:
        return False

#Jeu de tests:

assert est_divisible(11,4)==False
assert est_divisible(21,7)==True
assert est_divisible(0,3)==True

    #Question 3:

def ppcm(a,b):

    """
    Number^2 -> Number
    Calcule le plus petit multiplicateur commun.
    """

    #i:int
    i=1

    while est_divisible(i,a)==False or est_divisible(i,b)==False:
        i=i+1

    return i

#Jeu de tests:

assert ppcm(2,3)==6
assert ppcm(6,8)==24
assert ppcm(12,15)==60

#Exercice 3.3:

def somme_carre(x,y):
    """
    number^2 -> number
    hypothese: y >= x
    retourne la somme des carrés des nombre de x a y
    """
    #z:int
    z=0

    #w:int
    w=x

    while w<= y:
        z=z+w*w
        w=w+1
        
    return z

#Jeu de tests:

assert somme_carre(2,2)==4
assert somme_carre(3,6)==86
assert somme_carre(5,10)==355

#Exercice 3.4:

    #Question 1:

def divise(n,p):
    """
    number^2 -> boolean
    retourne True si n divise p False sinon
    """

    return p%n==0
    
#Jeu de tests:

assert divise(1,4)==True
assert divise(2,4)==True
assert divise(3,4)==False
assert divise(4,2)==False

    #Question 2:

def est_premier(n):
    """
    number -> boolean
    Retourne True si n est premier False sinon
    """

    #cpt:int
    #Si Cpt > 2 alors n n'est forcement pas Premier
    cpt=0

    #i:int
    i=1

    if n==0 or n==1:
        return False

    while i<=n:
        if divise(i,n)==True:
            cpt=cpt+1
            i=i+1
        else:
            i=i+1
            
    if cpt==2:
        return True
    else:
        return False

#Jeu de tests:

assert est_premier(0)==False
assert est_premier(1)==False
assert est_premier(2)==True
assert est_premier(17)==True
assert est_premier(357)==False

#Exercice 3.5:

    #Question 1:

def fibonacci(n):

    """
    Number -> Number
    Calcul le n-ième terme de la suite de Fibonacci
    """

    #i:int
    i=0

    #s:int
    s=0

    #t:int
    t=1

    while i<n:
        s=s+t
        t=s-t
        i=i+1

    return s

#Jeu de tests:

assert fibonacci(3)==2
assert fibonacci(10)==55
assert fibonacci(41)==165580141

    #Question 3:

def fibo_diff(k):

    """
    Number -> Number
    Hyppthèse : k est supérieur ou égal çà 2.
    Retourne le k-ième terme de la suite D.
    """

    return fibonacci(k)/fibonacci(k-1)

#Jeu de tests:

assert fibo_diff(5)==1.6666666666666667
assert fibo_diff(10)==1.6176470588235294
assert fibo_diff(41)==1.618033988749895

    #Question 4:

def fibo_approx(n):

    """
    Number -> Number
    Hypothèse : n est très grand.
    Retourne la n-ième valeur de la suite de Fibonacci.
    """

    return (((1+math.sqrt(5))/2)**n)/math.sqrt(5)

#Jeu de tests:

assert round(fibo_approx(50))==round(fibonacci(50))
assert round(fibo_approx(25))==round(fibonacci(25))
assert round(fibo_approx(28))==round(fibonacci(28))

#Exercice 3.6:

    #Question 1:

def partie_entiere(x):
    """
    number -> int
    hypothese x >= 0
    Retourne la partie entiere du nombre n
    """
    
    #n:int
    n=0


    while x<n or x>=n+1:
        n=n+1
        
    return n

#Jeu de tests:

assert partie_entiere(0.66)==0
assert partie_entiere(2.75)==2
assert partie_entiere(3.14159)==3
assert partie_entiere(2.0)==2

    #Question 2:

def encadrement(x,b):
    """
    number -> int
    hypothese x >= 0
    Renvoie le plus petit entier naturel tel que b<=x<b+ecart
    """
    
    #n:int
    n=0

    while x<n or x>=n+b:
        n=n+1
        
    return n

#Jeu de tests:

assert encadrement(0.66,2)==0
assert encadrement(7.42,1)==7
assert encadrement(7.42,3)==5
assert encadrement(7.42,4)==4

#Exercice 3.7:

    #Question 1:

def suite_racine(x,n):
    """
    number^2 -> number
    Retourne la nieme approximation de racine de x
    """

    #u:float
    u=1.0

    #temp:float
    temp=0.0

    #i:int
    i=0

    while i<n:
        temp=u
        u = (( (temp)+ ( x/(temp)) ) /2)
        i=i+1

    return u

#Jeu de tests:

assert suite_racine(4,0)==1.0
assert suite_racine(4,1)==2.5
assert suite_racine(4,2)==2.05
assert suite_racine(4,6)==2.0

    #Question 2:

def approx_racine_stable(x):
    """
    number -> number
    Retourne l'approximation de racine de x quand Un et Un-1 sont indistinguables
    """
    
    #u:float
    u=1.0

    #temp:float
    temp=0.0

    while temp-u!=0:
        temp=u
        u = (( (temp)+ ( x/(temp)) ) /2)

    return u

#Jeu de tests:

assert approx_racine_stable(4)==2.0
assert approx_racine_stable(25)==5.0
assert approx_racine_stable(2)==1.414213562373095

    #Question 3:

def approx_racine_eps(x,eps):
    """
    number -> number
    Retourne l'approximation de racine de x quand Un et sqrt(x) est identique a eps pres
    """
    
    #u:float
    u=1.0

    #temp:float
    temp=0.0

    while temp-u<eps:
        temp=u
        u = (( (temp)+ ( x/(temp)) ) /2)

    return u

#Jeu de tests:

##assert approx_racine_eps(4)==2.05
##assert approx_racine_eps(25)==5.0
##assert approx_racine_eps(2)==1.414213562373095

#Exercice 3.8:

    #Question 1:

def lancer_de6():

    """
    Retourne un entier entre 1 et 6.
    """

    #r:int
    r=random.random()*6

    return math.floor(r)+1

    #Question 2:

def lancer_de6s(a):

    """
    Retourne un entier entre 1 et 6.
    """

    #r:int
    random.seed(a)

    r=random.random()*6

    return math.floor(r)+1

#Jeux de tests:

assert lancer_de6s(1)==1
assert lancer_de6s(2)==6
assert lancer_de6s(3)==2
assert lancer_de6s(4)==2

    #Question 3:

def moyenne_plusieurs_lancers(n):

    """
    Number -> Number
    Retourne la moyenne de n lancers.
    """

    #i:int
    i=0

    #s=int
    s=0

    r=random.random()*6

    while i<n:
        s=s+lancer_de6()
        i=i+1

    return s/n

    #Question 4:

def frequence_valeur(r,n):

    """
    Number**2 -> Number
    Hypothèse : n est compris entre 1 et 6.
    Retourne fréquence d'apparition d'un nombre r pour n lancers.
    """

    #i:int
    i=0

    #f:int
    f=0

    while i<n:
        if lancer_de6()==r:
            f=f+1
        i=i+1

    return f/n

#La génération des valeurs aléatoire suit une loi uniforme. En effet, plus n est grand, plus la fréquence se rapproche de 1/6.

    #Question 5:

def lancer_deN(n):

    """
    Number -> Number
    Retourne une valeur entre 1 et n.
    """

    #r:int
    r=random.random()*n

    return math.floor(r)+1
