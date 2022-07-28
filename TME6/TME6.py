#Exercice 6.1

    #Question 1:
#Tous les manipulations des listes repose sur le meme principe: Python connais toujours la taille de la liste,
#Donc pour "naviguer" dans la liste on utilisera un For i in L . Pour en creer une: For i in range(0,taille) .
#Une fois dans le for, il suffit de faire L.append(b) pour ajouter l'element b a la liste.

def repetition(x,k):
    """
    Numner**2 -> list[alpha]
    Retourne k occurrences de x.
    """

    #r:int
    r=abs(k)
    
    #L:List[type(x)]
    L=[]

    for i in range(0,r):
        L.append(x)

    return L

#Jeu de tests:
assert repetition(5,0)==[]
assert repetition(4,3)==[4, 4, 4]
assert repetition(True,5)==[True, True, True, True, True]
assert repetition('Le chat !',2)==['Le chat !', 'Le chat !']

    #Question 2:

def repetition_bloc(x,k):
    """
    List[alpha]*int -> List[alpha]
    Retourne k occurrences de x.
    """

    #r:int
    r=abs(k)
    
    #L:List[type(x)]
    L=[]

    for i in range(0,r):
        for i in x:
            L.append(i)

    return L

#Jeu de tests:
assert repetition_bloc([5,7,8],3)==[5,7,8,5,7,8,5,7,8]
assert repetition_bloc([4,7],0)==[]
assert repetition_bloc(['Le chat',"n'est pas", 'là', '!'],2)==['Le chat',"n'est pas",'là','!','Le chat',"n'est pas", 'là', '!']

#Exercice 6.2

    #Question 1:

def max_liste(L):
    """
    List[Number] -> Number
    Hypothèse : len(L)>0
    Renvoie le plus grand nombre de la liste.
    """

    #temp:int
    temp=L[0]

    for i in L:
        temp=max(temp,i)

    return temp

#Jeu de tests:
assert max_liste([5,488,878,5,2,789,0])==878
assert max_liste([0])==0
assert max_liste([5,-8,5.0000001,-2,4])==5.0000001

    #Question 2:

def nb_occurences(L,x):
    """
    List[alpha]*alpha -> int
    Retourne le nombre d'occurences de x dans L.
    """

    #nb:int
    nb=0

    for i in L:
        if i==x:
            nb=nb+1

    return nb

#Jeu de tests:
assert nb_occurences([5,8,48,7,9,7,3,2,4,8,8,8,8],8)==5
assert nb_occurences([0,1,8,7,6,8,8,4,0],2)==0
assert nb_occurences([],1)==0

    #Question 3:

def nb_max(L):
    """
    List[Number] -> Number
    Retourne le nombre d'occurences du maximum de L.
    """

    #s:number
    s=max_liste(L)

    return nb_occurences(L,s)

#Jeu de tests:
assert nb_max([8,7,9,78,4,78,5,2,4,7])==2
assert nb_max([-5,-8,-84,-9,-5,-6,-5])==3
assert nb_max([0,-8,4,-5,1,4,-568,4,4])==4

#Exercice 6.3

    #Question 1:

def somme(L):
    """
    List[int] -> Int
    Retourne la somme des éléments de la liste L.
    """

    #s:int
    s=0

    for i in L:
        s=s+i

    return s

#Jeu de tests:
assert somme([5,8,9,7,7])==36
assert somme([8])==8
assert somme([0,0])==0
assert somme([3,-8,9,-4,0])==0

    #Question 2:

def moyenne(L):
    """
    List[int] -> Int
    Hypothèse : len(L)>0
    Retourne la moyenne des éléments de la liste L.
    """

    #m:int
    m=0

    m=somme(L)/len(L)
    return m

#Jeu de tests:
assert moyenne([5,5,5,5,5])==5
assert moyenne([0,-1,6,-5])==0
assert moyenne([-5,-8,-9,-14,-7,-6])==-8.166666666666666

    #Question 3:

def carres(L):
    """
    List[int] -> int
    Renvoie les carrés des éléments de la liste L.
    """

    #M:List[int]
    M=[]

    for i in L:
        M.append(i**2)

    return M

#Jeu de tests:
assert carres([5,6,2,3,4,1])==[25,36,4,9,16,1]
assert carres([0])==[0]
assert carres([])==[]

    #Question 4:

def variance(L):
    """
    List[int] -> int
    Hypothèse: len(L)>0
    Retourne la variance de la liste.
    """

    #v:int
    v=0

    #x:int
    x=0

    x=moyenne(L)

    for i in L:
        v=v+(i-x)**2

    v=v/len(L)
    return v

#Jeu de tests:
assert variance([20,0,20,0])==100.0
assert variance([0,0,0,0])==0.0
assert variance([5,7,20,3])==44.1875

    #Question 5:

import math

def ecart_type(L):
    """
    List[int] -> int
    Hypothèse: len(L)>0
    Retourne l'écart-type de la liste.
    """

    #e:int
    e=0

    e=math.sqrt(variance(L)) #Ou variance(L)**(1/2)
    
    return e

#Jeu de tests:
assert ecart_type([20,0,20,0])==10.0
assert ecart_type([15,15,5,5])==5.0
assert ecart_type([12,11,10,12,11])==0.7483314773547882

#Exercice 6.4

    #Question 1:

def liste_diviseurs(a):
    """
    int -> List[int]
    a>0
    Retourne la liste des diviseurs de a.
    """
    
    #L:List[int]
    L=[]

    #i:int
    i=1

    while i<=a:
        if a%i==0: 
            L.append(i)
        i=i+1

    return L

#Jeu de tests:
assert liste_diviseurs(0)==[]
assert liste_diviseurs(5)==[1,5]
assert liste_diviseurs(8)==[1,2,4,8]

    #Question 2:

def liste_diviseurs_impairs(a):
    """
    int -> List[int]
    a!=0
    Retourne la liste des diviseurs impairs de a.
    """

    #L:List[int]
    L=[]

    #i:int
    i=1

    while i<=a:
        if i%2!=0 and a%i==0:
            L.append(i)
        i=i+1

    return L

#Jeu de tests:
assert liste_diviseurs_impairs(0)==[]
assert liste_diviseurs_impairs(5)==[1,5]
assert liste_diviseurs_impairs(8)==[1]

    #Question 3:

def liste_diviseurs_pairs(a):
    """
    int -> List[int]
    a!=0
    Retourne la liste des diviseurs pairs de a.
    """

    #L:List[int]
    L=[]

    #i:int
    i=1

    while i<=a:
        if i%2==0 and a%i==0:
            L.append(i)
        i=i+1

    return L

#Jeu de tests:
assert liste_diviseurs_pairs(0)==[]
assert liste_diviseurs_pairs(5)==[]
assert liste_diviseurs_pairs(8)==[2,4,8]

#Exercice 6.6

    #Question 1:

def list_mult(L,k):
    """
    List[int] * int -> List[int]
    Retourne la liste avec tous les membres multipliés par k.
    """

    #R:int
    R=[]

    for i in L:
        R.append(i*k)

    return R

    #Question 2:

def list_div(L,k):
    """
    List[int] * int -> List[int]
    Retourne la liste avec tous les membres divisés par k.
    """

    #R:int
    R=[]

    for i in L:
        if i%k==0:
            R.append(i//k)

    return R

#Exercice 6.7

    #Question 1:

def decoupage_simple(L,i,j):
    """
    List[alpha]*int^2 -> List[alpha]
    Hypothèse : i et j sont positifs, j<=len(L)
    Retourne les éléments i à j de la liste L.
    """

    #R:List[alpha]
    R=[]

    for a in range(i,j):
        R.append(L[a])

    return R

    #Question 2:

def decoupage_pas(L,i,j,p):
    """
    List[alpha]*int^3 -> List[alpha]
    Hypothèse : i et j sont positifs, j<=len(L)
    Retourne les éléments i à j de la liste L.
    """

    #R:List[alpha]
    R=[]

    for a in range(i,j,p):
        R.append(L[a])

    return R

    #Question 3:

def decoupage_pas_inverse(L,j,i,p):
    """
    List[alpha]*int^3 -> List[alpha]
    Hypothèse : i et j sont positifs, j<=len(L) et p<0
    Retourne les éléments i à j de la liste L.
    """

    #R:List[alpha]
    R=[]

    while i<=j+p:
        R.append(L[j-1])
        j=j+p

    return R

#Exercice 6.8

    #Question 1:

def entrelacement(L1,L2):
    """
    List[alpha]**2 -> List[alpha]
    Entrelace les deux listes.
    """

    #L:List[alpha]
    L=[]

    #j:int
    j=0

    for i in L1:
        L.append(i)
        while j<len(L2):
            L.append(L2[j])
            j=len(L2)
        j=i
            

    return L

#Jeu de tests:
assert entrelacement([1,2,3],[4,5,6])==[1,4,2,5,3,6]
assert entrelacement([1,2,3],[])==[1,2,3]

    #Question 2:

def entrelacement_general(L1,L2):
    """
    List[alpha]**2 -> List[alpha]
    Entrelace les deux listes.
    """

    #L:List[alpha]
    L=[]

    #j:int
    j=0

    for i in L1:
        L.append(i)
        while j<len(L2):
            L.append(L2[j])
            j=len(L2)
        j=i

    if len(L1)<len(L2):
        L=L+L2[len(L1):len(L2)]
            

    return L

#Jeu de tests:
assert entrelacement_general([1,2,3],[4,5,6,7,8])==[1,4,2,5,3,6,7,8]
assert entrelacement_general([1,2,3,4,5,6],[7,8,9])==[1,7,2,8,3,9,4,5,6]
assert entrelacement_general([],[1,2,3])==[1,2,3]

#Exercice 6.9

    #Question 1:

def jonction(L,c):
    """
    List[alpha]*str -> Str
    Convertis la liste en chaine de caractère avec comme séparation le caractère c.
    """

    #r:str
    r=''

    for i in L:
        r=r+i+c

    return r

#Jeu de Test:
assert jonction(["Salut","comment","ca","va","?"],'_')=='Salut_comment_ca_va_?_'
    
    #Question 2:

def separation(s,c):
    """
    Str**2 -> List[str]
    Hypothèse : len(c)=1
    Retourne la liste de chaines composées de sous-chaines de s séparées par le caractère c. Le séparateur c n'est pas présent dans la liste résultat.
    """

    #temp:int
    temp=''

    #L:List[str]
    L=[]
        
    for j in s:
        if j==c:
            L.append(temp)
            temp=''
        else:
            temp=temp+j

        if j==s[len(s)-1] and j!=c:
            L.append(temp)
        
    return L
