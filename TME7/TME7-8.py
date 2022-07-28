#Exercice 7.7:
#CarreMagique: list[list[int]]
CarreMagique=[ [2,7,6],
               [9,5,1],
               [4,3,8] ]

    #Question 1:

def presence(n,L):
    """
    int * list[int] -> bool
    retourne True si n est present dans L ou False sinon.
    """

    #i:int
    for i in L:
        if n==i:
            return True
        
    return False

#Jeu de test:
assert presence(5,[9,5,1])==True
assert presence(4,[9,5,1])==False


    #Question 2:

def mat_presence(n,LL):
    """
    int * list[list[int]] -> bool
    retourne True si n est present dans les liste de LL ou False sinon.
    """
    
    #i:list[int]
    for i in LL:
        if presence(n,i)==True:
            return True

    return False

#Jeu de test:
assert mat_presence(6,[[1,2,3],[4,5,6]])==True
assert mat_presence(7,[[1,2,3],[4,5,6]])==False
assert mat_presence(7,CarreMagique)==True
assert mat_presence(10,CarreMagique)==False

    #Question 3:

def verif_elems(n,LL):
    """
    int * list[list[int]] -> boolean
    hypothese: n!=0
    retourne True si tous les entiers dans l'intervalle [1,n*n] sont presents la liste LL ou false sinon.
    """

    #i:int
    for i in range(1,(n**2)+1):
        if mat_presence(i,LL)==False:
            return False

    return True

#Jeu de test:
assert verif_elems(3,[ [2,7,6],[8,5,1],[4,3,8]])==False
assert verif_elems(3,CarreMagique)==True

    #Question 4:
def somme_liste(L):
    """
    list[int]->int
    retourne la somme des elements d'une liste L.
    """
    #s:int
    s=0
    #i:int
    for i in L:
        s=s+i
    return s

    #Question 5:
def verif_lignes(LL,s):
    """
    list[list[int]]*int -> bool
    retourne True si toutes les sous liste de LL possedent la meme somme s ou False sinon.
    """
    
    #i:list[int]
    for i in LL:
        if somme_liste(i)!=s:
            return False
            
    return True

#Jeu de test:
assert verif_lignes(CarreMagique, 15)==True
assert verif_lignes(CarreMagique, 16)==False
assert verif_lignes([[2,7,6],[8,5,1],[4,3,8]],15)==False

    #Question 6:

def colonne(j,M):
    """
    int*list[list[int]] -> list[int]
    retourne la j-eme colonne de la matrice M de taille n.
    """

    #Cr:list[int]
    Cr=[]
    
    #i:list[int]
    for i in M:
        Cr.append(i[j])

    return Cr

#Jeu de test
assert colonne(0,[[2,7,6],[9,5,1],[4,3,8]])==[2, 9, 4]
assert colonne(1,[[2,7,6],[9,5,1],[4,3,8]])==[7, 5, 3]
assert colonne(2,[[2,7,6],[9,5,1],[4,3,8]])==[6, 1, 8]

    #Question 7:

def verif_colonnes(M,s):
    """
    list[list[int]]*int -> boolean
    retourne True si toutes les colonnes de M possedent la meme somme s ou False sinon.
    """
    #i:int
    i=0
    #taille:int
    taille=len(M[0])
    while i < taille:
        if (somme_liste(colonne(i,M))) != s:
            return False
        else:
            i=i+1
        
    return True

#Jeu de test:
assert verif_colonnes(CarreMagique,14)==False
assert verif_colonnes(CarreMagique,15)==True
assert verif_colonnes([[2,7,6],[8,5,1],[4,3,8]],15)==False

    #Question 8:

def diagonale_1(M):
    """
    list[list[int]] -> list[int]
    retourne la deuxieme diagonales de M sous formes de liste.
    """
    #taille:int
    taille=len(M[0])-1
    #D1:list[int]
    D1=[]

    #j:int
    j=0
    #i:int
    i=0
    while j <= taille:
        D1.append(M[j][i])
        j=j+1
        i=i+1
        
    return D1

def diagonale_2(M):
    """
    list[list[int]] -> list[int]
    retourne la deuxieme diagonale de M sous forme de liste.
    """
    #taille:int
    taille=len(M[0])-1
    #D2:list[int]
    D2=[]

    #j:int
    j=0
    #i:int
    i=taille
    while j <= taille:
        D2.append(M[j][i])
        j=j+1
        i=i-1
        
    return D2

#Jeu de test:
assert diagonale_1([[2,7,6],[9,5,1],[4,3,8]])==[2, 5, 8]
assert diagonale_2([[2,7,6],[9,5,1],[4,3,8]])==[6, 5, 4]
assert diagonale_1([[2,7,6,7],[9,5,1,8],[4,3,8,9],[2,7,6,9]])==[2, 5, 8, 9]
assert diagonale_2([[2,7,6,7],[9,5,1,8],[4,3,8,9],[2,7,6,9]])==[7, 1, 3, 2]

def verif_diagonales(M,s):
    """
    list[list[int]]*int -> boolean
    retourne True si toutes les diagonales de M possedent la meme somme s ou False sinon.
    """

    #i:int
    i=0
    #taille:int
    if somme_liste(diagonale_1(M)) != s and somme_liste(diagonale_2(M)) != s:
        return False
    else:
        return True
#Jeu de test:
assert verif_diagonales(CarreMagique,15)==True
assert verif_diagonales(CarreMagique,14)==False

    #Question 9:

def verif_magique(M):
    """
    list[list[int]] -> boolean
    verifie si M est Magique!
    """
    
    #s:int
    s=somme_liste(M[0])
    #t:int
    t=len(M[0])

    return verif_elems(t,M)==verif_lignes(M,s)==verif_diagonales(M,s)==verif_colonnes(M,s)

#Jeu de test:
assert verif_magique(CarreMagique)==True
assert verif_magique([[2,7,6],[9,5,1],[4,3,10]])==False


#Exercie 8.1
    #Question 1:
def repetition(x,k):
    """
    Numner**2 -> list[alpha]
    Retourne k occurrences de x.
    """
    return [x for i in range(0,k)]

#Jeu de tests:
assert repetition(5,0)==[]
assert repetition(4,3)==[4, 4, 4]
assert repetition(True,5)==[True, True, True, True, True]
assert repetition('Le chat !',2)==['Le chat !', 'Le chat !']

    #Question 2:

def liste_diviseurs(a):
    """
    int -> List[int]
    a>0
    Retourne la liste des diviseurs de a.
    """
    
    return [i for i in range(1,a+1) if a%i==0]

#Jeu de tests:
assert liste_diviseurs(0)==[]
assert liste_diviseurs(5)==[1,5]
assert liste_diviseurs(8)==[1,2,4,8]


def liste_diviseurs_impairs(a):
    """
    int -> List[int]
    a!=0
    Retourne la liste des diviseurs impairs de a.
    """

    return [i for i in range(1,a+1) if (i%2!=0 and a%i==0)]

#Jeu de tests:
assert liste_diviseurs_impairs(0)==[]
assert liste_diviseurs_impairs(5)==[1,5]
assert liste_diviseurs_impairs(8)==[1]


def liste_diviseurs_pairs(a):
    """
    int -> List[int]
    a!=0
    Retourne la liste des diviseurs pairs de a.
    """
    
    return [i for i in range(1,a+1) if (i%2==0 and a%i==0)]

#Jeu de tests:
assert liste_diviseurs_pairs(0)==[]
assert liste_diviseurs_pairs(5)==[]
assert liste_diviseurs_pairs(8)==[2,4,8]

    #Question 3:

def list_mult(L,k):
    """
    List[int] * int -> List[int]
    Retourne la liste avec tous les membres multipliés par k.
    """
    
    return [i*k for i in L]

def list_div(L,k):
    """
    List[int] * int -> List[int]
    Retourne la liste avec tous les membres divisés par k.
    """

    return [î//k for i in L if (i%k==0)]
