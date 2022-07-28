#Exercice 7.1

def partie_imaginaire(c):
    """tuple[float,float]->float
    renvoie la partie imaginaire de c"""
    #reelle : float
    #imaginaire : float
    reelle,imaginaire=c
    return imaginaire

assert partie_imaginaire((2.0,3.0))==3.0

def partie_reelle(c):
    """tuple[float,float]->float
    renvoie la partie imaginaire de c"""
    #reelle : float
    #imaginaire : float
    reelle,imaginaire=c
    return reelle

assert partie_reelle((2.0,3.0))==2.0

#Question 2:

def addition_complexe(c1,c2):
    """tuple[float,float]^2-> tuple[float,float]
    renvoie l'addition des nombres complexe c1 et c2
    """
    return (partie_reelle(c1)+partie_reelle(c2),partie_imaginaire(c1)+partie_imaginaire(c2))

assert addition_complexe((1.0,0.0), (0.0,1.0))==(1.0, 1.0)

#Question 3:

def produit_complexe(c1,c2):
    """tuple[float,float]^2-> tuple[float,float]
    renvoie le produit des nombres complexe c1 et c2
    """
    #a : float
    a=partie_reelle(c1)
    #b : float
    b=partie_imaginaire(c1)
    #c : float
    c=partie_reelle(c2)
    #d : float
    d=partie_imaginaire(c2)
    
    return ( (a*c)-(b*d) ) , ( (a*d)+(b*c) )

assert produit_complexe((2.0,3.0),(0.0,1.0))==(-3.0, 2.0)

#exercice 7.2

#Question 1:

def nb_de_max(L):
    """List[Number] -> tuple[Number,int]
    Hyp : len(L)>0
    Renvoie le plus grand nombre de la liste et le nombre de fois qu'il apparait
    """
    # n : int
    n=0

    # M :Number
    M=L[0]
    #i : Number
    for i in L:
        if i>M:
            M=i
        elif i==M:
            n=n+1
    return(M,n)

assert nb_de_max([3,7,9,5.4,8.9,9,8.999,5])==(9, 2)

#Exercice 7.3

def pgcd(a,b):
    """
    int**2 -> int
    Renvoie le pgcd de la fraction (a,b)
    """
    
    #r:int
    r=a%b
    #n:int
    n=a
    #d:int
    d=b
    
    while r!=0 :
        n=d
        d=r
        r=n%d
        
    return d

assert pgcd(9,12)==3

def fraction(a,b):
    """int^2 -> tuple[int,int]
    hyp: b!=0
    Renvoie la forme canonique de la Fraction f
    """

    #p :int
    p= pgcd(b,a)
    return (a//p,b//p)    

assert fraction(180, 240)==(3,4)

#Question 2:

def frac_mult(f1,f2):
    """
    tuple[int,int]^2-> tuple[int,int]
    retourne le produit de deux fraction sous la forme d'une fraction canonique.
    """
    
    #n1 : int
    #d1 : int
    n1,d1= f1
    #n2 : int
    #d2 : int
    n2,d2= f2

    return fraction((n1*n2),(d1*d2))


assert frac_mult((3,4),(8,4))==(3, 2)

#Question 3:

def frac_div(f1,f2):
    """
    tuple[int,int]^2-> tuple[int,int]
    retourne le produit de deux fraction sous la forme d'une fraction canonique
    """
    #fn2 : int
    #fd2 : int
    fn2,fd2 = f2

    return frac_mult(f1,(fd2,fn2))


assert frac_div((3,4),(8,4))==(3, 8)

#Question 4:

def ppcm(a,b):
    """int**2 -> int
    hypothese:a et b >0
    retourne le plus petit commmun multiple de a et b.
    """

    #p:int
    p=0
    if a>=b:
        p=pgcd(a,b)
    else:
        p=pgcd(b,a)

    return abs(a*b)//p

def frac_add(f1,f2):
    """tuple[int,int]^2 -> tuple[int,int]
    retourne la somme des fraction f1 et f2 sous forme d'une fraction canonique
    """
    #fn1 : int
    #fd1 : int
    fn1,fd1=f1
    #fn2 : int
    #fd2 : int
    fn2,fd2=f2

    #p:int
    p=ppcm(fd1,fd2)

    return fraction(fn1*(p//fd1) + fn2*(p//fd2),p)

assert ppcm(11, 17) == 187


#Exercice 8

def repetition(x, k):
    """alpha * int -> list[alpha]
    Hyp: k >= 0
    retourne la liste de k occurrences de x"""
    return [x for i in range(1,k+1)]
assert repetition(4,0) == []
assert repetition(0,4) == [0,0,0,0]


def liste_diviseurs(a):
    """int -> list[int]
    Hyp : a > 0
    retourne la liste des diviseurs de a"""
    return [i for i in range(1,a+1) if a % i ==0]

assert liste_diviseurs(12) == [1,2,3,4,6,12]
