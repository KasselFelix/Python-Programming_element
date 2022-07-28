#Exercice 8.3

    #Question 1:

def alphabet():
    """
    None -> List[str]
    Retourne une liste des lettres de l'alphabet.
    """

    return [ chr(i) for i in range(ord('a'),ord('z')+1)]

#Jeu de test:
assert alphabet()== ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def est_voyelle(c):
    """
    Str -> Bool
    Hypothèse : len(c)==1.
    Retourne True si c est une voyelle.
    """

    return c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='y'

#Jeu de test:
assert est_voyelle('t')== False
assert est_voyelle('a')== True


    #Question 3:

def liste_voyelle():
    """
    None -> List[str]
    Retourne la liste des voyelle de l'alphabet.
    """

    return [i for i in alphabet() if est_voyelle(i)]

#Jeu de test:
assert liste_voyelle()== ['a', 'e', 'i', 'o', 'u', 'y']

    #Question 4:

def liste_consonne():
    """
    None -> List[str]
    Retourne la liste des consonnes de l'alphabet.
    """
    
    return [i for i in alphabet() if not est_voyelle(i)]

#Jeu de test:
assert liste_consonne() == ['b', 'c', 'd', 'f',
                            'g', 'h', 'j', 'k',
                            'l', 'm', 'n', 'p',
                            'q', 'r', 's', 't',
                            'v', 'w', 'x', 'z']

#Exercice 8.4

    #Question 1:

def liste_non_multiple(n,L):
    """
    int * List[int] -> List[int]
    Retourne la liste sans les multiples de n.
    """

    return [i for i in L if i%n!=0 and i!=n]

#Jeu de test:
assert liste_non_multiple(2,[2,3,4,5,6,7,8,9,10])==[3,5,7,9]
assert liste_non_multiple(3,[2,3,4,5])==[2,4,5]
assert liste_non_multiple(2,[2,4,6])==[]
assert liste_non_multiple(2,[])==[]
assert liste_non_multiple(7,[2,3,4,5])==[2,3,4,5]

    #Question 2:

def suppr_liste(n,L):
    """
    int * List[int] -> List[int]
    Retire l'élément n de la liste L.
    """

    #R:List[int]
    R=[]

    for i in L:
        if i!=n:
            R.append(i)

    return R

def eratosthene(n):
    """
    int -> List[int]
    Retourne la liste des entier premiers inférieurs ou égaux à n.
    """
    
    L = [2]
 
    for i in range(3, n, 2):
        L.append(i)
 
    for i in L:
        for n in L:
            if n % i == 0 and i != n:
                L=suppr_liste(n,L)
 
    return L

#Jeu de test:
assert eratosthene(10)==[2,3,5,7]
assert eratosthene(2)==[2]
assert eratosthene(50)==[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]


    #Question 3:

def liste_facteurs_premiers(n):
    """
    int -> List[int]
    Hypothèse : n>=2
    """

    return [i for i in eratosthene(n) if n%i==0]

#Jeu de test:
assert liste_facteurs_premiers(2)==[2]
assert liste_facteurs_premiers(10)==[2,5]
assert liste_facteurs_premiers(2*3*7)==[2,3,7]
assert liste_facteurs_premiers(2*3*4*7*9)==[2,3,7]

#Exercice 8.5

    #Question 1:

def liste_caractere(s):
    """
    str -> List[str]
    Convertis une chaine de caractères en liste.
    """

    return [i for i in s]

#Jeu de test:
assert liste_caractere('les carottes')==['l', 'e', 's', ' ', 'c', 'a', 'r', 'o', 't', 't', 'e', 's']
assert liste_caractere('')==[]
assert liste_caractere('Marie-Celine')== ['M', 'a', 'r', 'i', 'e', '-', 'C', 'e', 'l', 'i', 'n', 'e']

    #Question 2:

def chaine_de(L):
    """
    List[str] -> str
    """

    #s:str
    s=''

    for i in L:
        s=s+i

    return s

#Jeu de test:
assert chaine_de (['s','a','l','u','t'])=='salut'
assert chaine_de(liste_caractere('les carottes'))=='les carottes'
assert chaine_de([])==''

    #Question 3:

def num_car(c):
    """
    str -> int
    Hypothèse : len(c)==1
    """

    return ord(c)-ord('a')

#Jeu de test:
assert num_car('a')==0
assert num_car('b')==1
assert num_car('z')==25

    #Question 4:

def car_num(n):
    """
    int -> str
    Hypothèse: 0<=n<26.
    """

    return chr(n+ord('a'))

#Jeu de test:
assert car_num(0)=='a'
assert car_num(1)=='b'
assert car_num(25)=='z'

    #Question 5:

def rot13(c):
    """
    str -> str
    Hypothèse : len(c)==1
    """

    if c>='a' and c<='z':
        return car_num((num_car(c)+13)%26) 
    else:
        return c

#Jeu de test:
assert rot13('a')=='n'
assert rot13('n')=='a'
assert rot13('b')=='o'
assert rot13('o')=='b'
assert rot13('m')=='z'
assert rot13('z')=='m'
assert rot13('')==''
assert rot13('e')=='r'
assert rot13('r')=='e'
assert rot13('8')=='8'
assert rot13(rot13('a'))=='a'
assert rot13(rot13('f'))=='f'

    #Question 6:

def codage_rot13(s):
    """
    str -> str
    Retourne la chaîne de caractère s codé avec le cryptage ROT13.
    """

    return chaine_de([rot13(i) for i in liste_caractere(s)])

#Jeu de test:
assert codage_rot13('thunderbolt')=='guhaqreobyg'
assert codage_rot13(codage_rot13('thunderbolt'))=='thunderbolt'

#Exercice 8.6

#type Etudiant = tuple[str,str,int,list[int]]

#baseUPMC: list[Etudiant]
BaseUPMC= [('GARGA','Amel',20231343,[12,8,11,17,9]),
            ('POLO','Marcello',20342241,[9,11,19,3]),
            ('AMANGEAI','Hildegard',20244229,[15,11,7,14,12]),
            ('DENT','Arthur',42424242,[8,4,9,7,12,5]),
            ('ALEZE','Blaise',30012024,[17,15,20,14,18,16,20]),
            ('D2','R2',10100101,[10,10,10,10,10,10])]

    #Question 1:

def mauvaise_note(etu):
    """
    tuple[str,str,int,List[int]] -> bool
    Retourne True si l'étudiant a eu une note inférieure à 10.
    """

    (nom, pre, ne, note) = etu

    for i in note:
        if i<10:
            return True

    return False

#Jeu de test:
assert mauvaise_note(('APRAHAMIAN','Arnaud',3410492,[15,16,10,9,5,19]))==True
assert mauvaise_note(('BESHARA','Marie-Celine', 3521563,[15,16,10,11,15,19]))==False


    #Question 2:

def base_mauvaise_note(base):
    """
    List[etudiant] -> List[etudiant]
    Retourne la liste des étudiants ayant eu une note inférieure à 10.
    """

    return [i for i in base if mauvaise_note(i)]
#Jeu de test:
assert base_mauvaise_note(BaseUPMC)== [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
                                      ('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
                                      ('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
                                      ('DENT', 'Arthur', 42424242, [8, 4, 9, 7, 12, 5])]

    #Question 3:

def base_mauvaise_note_nom(base):
    """
    List[etudiant] -> List[str]
    Retourne la liste des noms des étudiants ayant eu une note inférieure à 10.
    """

    return [i[0] for i in base_mauvaise_note(base)]

#Jeu de test:
assert base_mauvaise_note_nom(BaseUPMC)== ['GARGA', 'POLO', 'AMANGEAI', 'DENT']

    #Question 4:

def bonne_note(base):
    """
    List[etudiant] -> List[int]
    Retourne la liste des numéros des étudiant n'ayant pas eu de note inférieure à 10.
    """

    return [i[2] for i in base if not mauvaise_note(i)]

#Jeu de test:
assert bonne_note(BaseUPMC)== [30012024, 10100101]

#Exercice 8.7

    #Question 1:

def triplets(n):
    """
    int -> List[tuple(int,int,int)]
    Hypothèse : n est un entier.
    """

    return [(i,j,k) for i in range(1,n+1) for j in range(1,n+1) for k in range(1,n+1)]

#Jeu de test:
assert triplets(0)==[]
assert triplets(1)==[(1, 1, 1)]
assert triplets(2)== [(1, 1, 1), (1, 1, 2), (1, 2, 1),
                      (1, 2, 2), (2, 1, 1), (2, 1, 2),
                      (2, 2, 1), (2, 2, 2)]

    #Question 2:

def decompositions(n):
    """
    int -> List[tuple(int,int,int)]
    Hypothèse : n est un entier.
    """

    return [i for i in triplets(n) if i[0]+i[1]==i[2]]

#Jeu de test:

assert decompositions(0)== []
assert decompositions(1)== []
assert decompositions(2)== [(1, 1, 2)]
assert decompositions(3)== [(1, 1, 2), (1, 2, 3), (2, 1, 3)]
assert decompositions(4)== [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 1, 3), (2, 2, 4), (3, 1, 4)]

    #Question 3:

def encadrements1(n):
    """
    int -> List[tuple(int,int,int)]
    Hypothèse : n est un entier.
    """

    return [i for i in triplets(n) if i[0]<=i[1]<=i[2]]

def encadrements2(n):
    """
    int -> List[tuple(int,int,int)]
    Hypothèse : n est un entier.
    """

    return [(i,j,k) for i in range(1,n+1) for j in range(1,n+1) for k in range(1,n+1) if i<=j<=k]

    #Question 4:

def encadrements3(n):
    """
    int -> List[tuple(int,int,int)]
    Hypothèse : n est un entier.+
    
    """

    #L:List[tuple(int,int,int)]
    L=[]

    #cpt:int
    cpt=0

    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                cpt=cpt+1
                if i<=j<=k:
                    L.append((i,j,k))

    return L

def encadrements4(n):
    """
    int -> List[tuple(int,int,int)]
    Hypothèse : n est un entier.
    """

    #L:List[tuple(int,int,int)]
    L=[]
    
    #cpt:int
    cpt=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            for k in range(j,n+1):
                    cpt=cpt+1
                    L.append((i,j,k))

    return L 

#Jeu de test:
assert encadrements1(1)== [(1, 1, 1)] == encadrements2(1) == encadrements3(1) == encadrements4(1)
assert encadrements1(2)== encadrements2(2) == encadrements3(2) == encadrements4(2)
