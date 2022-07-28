#Exercice 1:

#type Complexe = tuple[float,float]
#2+3i => (2.0,3.0)

    #Question 1:

def partie_reelle(c):
    """
    Complexe -> float
    Renvoie la partie Reelle de c.
    """
    #r,i:float
    (r,i)= c
    
    return r

def partie_imaginaire(c):
    """
    Complexe -> float
    Renvoie la partie Reelle de c.
    """
    #r,i:float
    (r,i)= c
    
    return i

#Jeu de tests:
assert partie_reelle((2.0,3.0))==2.0
assert partie_imaginaire((2.0,3.0))==3.0
assert partie_reelle((0.0,1.0))==0.0
assert partie_imaginaire((0.0,1.0))==1.0

    #Question 2:

def addition_complexe(c1,c2):
    """
    Complexe**2 -> Complexe
    renvoie l'addition des nombres complexe c1 et c2.
    """
    #a,b,c,d:float
    a=partie_reelle(c1)
    b=partie_imaginaire(c1)
    c=partie_reelle(c2)
    d=partie_imaginaire(c2)
    
    return (a+c),(b+d)

#Jeu de tests:
assert addition_complexe((1.0,0.0),(0.0,1.0))==(1.0, 1.0)
assert addition_complexe((2.0,3.0),(0.0,1.0))==(2.0, 4.0)

    #Question 3:

def produit_complexe(c1,c2):
    """
    Complexe**2 -> Complexe
    renvoie le produit des nombres complexe c1 et c2.
    """
    #a,b,c,d:float
    a=partie_reelle(c1)
    b=partie_imaginaire(c1)
    c=partie_reelle(c2)
    d=partie_imaginaire(c2)
    
    return ( (a*c)-(b*d) ) , ( (a*d)+(b*c) )

#Jeu de tests:
assert produit_complexe((0.0,0.0),(1.0,1.0))==(0.0, 0.0)
assert produit_complexe((0.0,1.0),(0.0,1.0))==(-1.0, 0.0)
assert produit_complexe((2.0,3.0),(0.0,1.0))==(-3.0, 2.0)

#Exercice 2:

    #Question 1:

def nb_de_max(L):
    """
    List[Number] -> Number
    Hypothèse : len(L)>0
    Renvoie le plus grand nombre de la liste et le nombre de fois qu'il apparait.
    """
    #M:number
    M=max(L)
    #nb:int
    nb=0

    #i:number
    for i in L:
        if i==M:
            nb=nb+1
            
    return (M,nb)

#Jeu de test:
assert nb_de_max([10])==(10, 1)
assert nb_de_max([3,7,9,5.4,8.9,9,8.999,5])==(9, 2)
assert nb_de_max([-2,-1,-5,-3,-1,-4,-1])==(-1, 3)

#Exercice 3:
#type Fraction=tuple[int,int]
#2/3 = (2,3)

def pgcd(a,b):
    """
    int**2 -> int
    Renvoie le pgcd de la fraction (a,b).
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

def ppcm(a,b):
    """
    int**2 -> int
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

    #Question 1:

def fraction(a,b):
    """
    int**2 -> Fraction
    Renvoie la forme canonique de la Fraction f.
    """
    p=pgcd(a,b)
    
    return (a//p),(b//p)

#jeu de test:
assert fraction(9,12)==(3, 4)
assert fraction(12,9)==(4, 3)
assert fraction(180,240)==(3, 4)
assert fraction(121,187)==(11, 17)

    #Question 2:

def frac_mult(f1,f2):
    """
    Fraction**2 -> Fraction
    retourne le produit de deux fraction sous la forme d'une fraction canonique.
    """
    
    #n1,d1,n2,d2:int
    (n1,d1)= f1
    (n2,d2)= f2

    return fraction((n1*n2),(d1*d2))

#Jeu de test:
assert frac_mult((3,4),(8,4))==(3, 2)
assert frac_mult((3,4),(4,3))==(1, 1)
assert frac_mult((3,4),(1,1))==(3, 4)
assert frac_mult((3,4),(0,4))==(0, 1)

    #Question 3:

def frac_div(f1,f2):
    """
    Fraction**2 -> Fraction
    retourne le produit de deux fraction sous la forme d'une fraction canonique.
    """
    #n1,d1,n2,d2:int
    (n1,d1)= f1
    (n2,d2)= f2

    if n2==0 or n1==0:
        return 0

    return fraction((n1*d2),(d1*n2))

#Jeu de test:
assert frac_div((3,4),(8,4))==(3, 8)
assert frac_div((3,4),(0,4))==0

    #Question 4:

def frac_add(f1,f2):
    """
    Fraction**2 -> Fraction
    retourne la somme des fraction f1 et f2 sous forme d'une fraction canonique.
    """
    
    #n1,d1,n2,d2:int
    (n1,d1)= f1
    (n2,d2)= f2

    #p:int
    p=ppcm(d1,d2)

    return fraction(((n1*(p//d1)) + (n2*(p//d2))),p)

#Jeu de test:
assert frac_add((8,4),(1,4))==(9,4)
assert frac_add((9,4),(5,4))==(7,2)
assert frac_add((1,3),(1,2))==(5, 6)

#Exercice 7.4:
#type Point = tuple[int,int]

    #Question 1:

def vecteur(p1,p2):
    """
    Point**2 -> (int,int)
    Renvoie le couple de coordonnee du vecteur forme par les points p1 et p2.
    """
    
    #x1,y1,x2,y2:int
    (x1,y1)= p1
    (x2,y2)= p2

    return (x1-x2),(y1-y2)

#Jeu de test: 
assert vecteur((5,4),(6,5))==(-1,-1)
assert vecteur((6,5),(5,4))==(1,1)

    #Question 2:

def alignes(p1,p2,p3):
    """
    Point**3 -> boolean
    Return True si les points sont aligne sinon False.
    """
    #v1v2:tuple(int,int)
    (v1,v2)=vecteur(p1,p2)
    #v2v3:tuple(int,int)
    (v3,v4)=vecteur(p2,p3)

    if v3==0 or v4==0:
        return False

    return (v1//v3)==(v2//v4)
#Jeu de test:
assert alignes((0,0),(1,1),(5,5))== True
assert alignes((0,0),(1,1),(1,2))== False

#Question 3:

def alignement(L):
    """
    list[Point] -> boolean
    hypothese len(L)>3
    retourne True si tous les points de L sont alignes ou False sinon.
    """

    #temp:bool
    temp=False

    #p:Point
    for (p1,p2,p3) in len(L):
        if alignes(L[p1],L[p2],L[p3])==True:
            temp=True
            
    return temp

#Exercice 7.5:
#type Etudiant = tuple([str,str,int,list[int])
#BaseUPMC: list[Etudiant]
BaseUPMC= [('GARGA','Amel',20231343,[12,8,11,17,9]),
           ('POLO','Marcello',20342241,[9,11,19,3]),
           ('AMANGEAI','Hildegard',20244229,[15,11,7,14,12]),
           ('DENT','Arthur',42424242,[8,4,9,4,12,5]),
           ('ALEZE','Blaise',30012024,[17,15,20,14,18,16,20]),
           ('R2','D2',10100101,[10,10,10,10,10,10])]

    #Question 1:

def note_moyenne(L):
    """
    list(int) -> float
    renvoie la moyenne des notes (entre 0 et 20) de la list L.
    """
    #s:int
    s=0
    #cpt:
    cpt=0
    #i:int
    for i in L:
        s=s+i
        cpt=cpt+1

    if cpt>0:
        return s/cpt
    else:
        return 0

#Jeu de test:
assert note_moyenne([12,8,14,6,5,15])== 10.0
assert note_moyenne([])==0

    #Question 2:

def moyenne_generale(base):
    """
    BaseUPMC -> float
    retourne la note moyenne generale de tous les etudiants.
    """

    #s:int
    s=0
    #cpt:
    cpt=0

    #N,n,num,notes:str,str,int,list[int]:
    for N,n,num,notes in base:
        #i:int
        for i in notes:
            s=s+i
            cpt=cpt+1

    if cpt>0:
        return s/cpt
    else:
        return 0

#Jeu de test:
assert moyenne_generale(BaseUPMC)== 11.515151515151516
assert moyenne_generale([])== 0

    #Question 3:

def top_etudiant(BD):
    """
    BaseUPMC -> tuple[str,str]
    hypothese len(BD)>0

    retourne un etudiant de la base BD avec la meilleur moyenne.
    si des etudiant sont ex-aequo alors on retourne le premier
    dans l'ordre sequentiel de la liste.
    """

    #top:float
    top=0.0
    #etu_top:tuple[str,str]
    etu_top=('a','b')
    
    #N,n,num,notes:str,str,int,list[int]:
    for N,n,num,notes in BD:
        if note_moyenne(notes) > top:
            top=note_moyenne(notes)
            etu_top=(N,n)

    return etu_top

#Jeu de test:
assert top_etudiant(BaseUPMC)==('ALEZE', 'Blaise')

    #Question 4:

def recherche_moyenne(n_e,base):
    """
    int*BaseUPMC -> float or None
    recherche la moyenne corespondant au numeros de l'etudiant dans la base.
    retourne la moyenne si elle existe ou None si elle existe pas.
    """

    #N,n,num,notes:str,str,int,list[int]:
    for N,n,num,notes in base:
        if n_e==num:
            return note_moyenne(notes)

    return None
    
#Jeu de test:
assert recherche_moyenne(20244229,BaseUPMC)==11.8
assert recherche_moyenne(20342241,BaseUPMC)==10.5
assert recherche_moyenne(2024129111,BaseUPMC)==None

#Exercice 7.6:

    #Question 1:

def intersection_2_listes(L1,L2):
    """
    list[int]**2 -> list[int]
    renvoie la liste des elements appartenant a la fois a L1 et a L2.
    """
    #LR:list[int]
    LR=[]

    #i:int
    for i in L1:
        #j:int
        for j in L2:
            if i==j and i not in LR:
                LR.append(i)
                
    return LR

    #Question 2:

def intersection(L):
    """
    list(list(int)) -> list(int)
    renvoie la liste triée des entiers appartenant a chacune des liste de L.
    """
    #LR:list[int]
    LR=[]
                
    return LR

#Exercice 7.7:
#CareeMagique: list[list[int]]
CarreMagique=[ [2,7,6],
               [9,5,1],
               [4,3,8] ]

    #Question 1:

def presence(n,L):
    """
    int * list[int] -> boolean
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
    int * list[list[int]] -> boolean
    retourne True si n est present dans les liste de LL ou False sinon.
    """

    #temp:boolean
    temp=False
    #i:list[int]
    for i in LL:
        if presence(n,i)==True:
            temp=True

    return temp

#Jeu de test:
assert mat_presence(6,[[1,2,3],[4,5,6]])==True
assert mat_presence(7,[[1,2,3],[4,5,6]])==False
assert mat_presence(7,CarreMagique)==True
assert mat_presence(10,CarreMagique)==False

    #Question 3:

def verif_elems(n,LL):
    """
    int * list[list[int]] -> boolean
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
    list[list[int]]*int -> boolean
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
    retourne la deuxieme diagonales de M sous formes de liste.
    """
    #taille:int
    taille=len(M[0])-1
    #D1:list[int]
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

    return verif_lignes(M,s)==verif_diagonales(M,s)==verif_colonnes(M,s)

#Jeu de test:
assert verif_magique(CarreMagique)==True
assert verif_magique([[2,7,6],[9,5,1],[4,3,10]])==False

