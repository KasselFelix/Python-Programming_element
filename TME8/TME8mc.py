#Exercice 8.5

    #Question 1

def liste_caractere(s):
    """str->list[str]
    convertis une chaine chaine de carac en liste """

    return [i for i in s]

#Jeu de test:
assert liste_caractere('les carottes')==['l', 'e', 's', ' ', 'c', 'a', 'r', 'o', 't', 't', 'e', 's']
assert liste_caractere('')==[]
assert liste_caractere('Marie-Celine')== ['M', 'a', 'r', 'i', 'e', '-', 'C', 'e', 'l', 'i', 'n', 'e']

    #Question 2

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

    #Question 3


def num_car(c):
    """ str->Int
    retourne le numero du caractere passé en parametre """

    return ord(c)-ord('a')

#Jeu de test:
assert num_car('a')==0
assert num_car('b')==1
assert num_car('z')==25

    #Question 4

def car_num(n):
    """int->str
    hyppthese : 0<=n<=25
    retourne le caractere correspondant au numero"""

    return chr(n+97)

#Jeu de test:
assert car_num(0)=='a'
assert car_num(1)=='b'
assert car_num(25)=='z'

    #Question 5

def rot13(c):
    """str->str
    hypothese : len(c)==1
    code c en ROT13
    """

    if c>='a' and c<='z':
        return car_num((num_car(c)+13)%26)
    else :
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

    #Question 6

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


    #Question 1

def mauvaise_note(etu):
    """ Etudiant -> bool
    Retourne True si l'étudiant a eu une note inférieure à 10.
    """

    (nom, prenom, ne, note) = etu

    for i in note :
        if i<10 :
            return True
    return False

#Jeu de test:
assert mauvaise_note(('APRAHAMIAN','Arnaud',3410492,[15,16,10,9,5,19]))==True
assert mauvaise_note(('BESHARA','Marie-Celine', 3521563,[15,16,10,11,15,19]))==False


    #Question 2

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

    #Question 3

def base_mauvaise_note_nom(base):
    """
    List[etudiant] -> List[str]
    Retourne la liste des noms des étudiants ayant eu une note inférieure à 10.
    """

    return [i[0] for i in base_mauvaise_note(base)]

#Jeu de test:
assert base_mauvaise_note_nom(BaseUPMC)== ['GARGA', 'POLO', 'AMANGEAI', 'DENT']

    #Question 4

def bonne_note(base):
    """
    List[etudiant] -> List[int]
    Retourne la liste des numéros des étudiant n'ayant pas eu de note inférieure à 10.
    """

    return [i[2] for i in base if not mauvaise_note(i)]

#Jeu de test:
assert bonne_note(BaseUPMC)== [30012024, 10100101]

#Exercice 9.2

    #Question 1

#Magasin = type dict[str:float]
Magasin={'Sabre Laser':229.0,
   'Mitendo DX':127.30,
   'Coussin Linux':74.50,
   'Slip Goldorak':29.90,
   'Station Nextpresso':184.60}


    #Question 2:

def disponible(prod,prix):
    """
    str * magasin -> bool
    Retourne True si prod est dispo dans prix.
    """
    return prod in prix

#Jeu de test:
assert disponible('tuc',Magasin)==False
assert disponible('Sabre Laser',Magasin)==True

    #Question 3:

def prix_moyen(prix):
    """
    magasin -> int
    hypo : prix != dict()
    Retourne la moyenne des prix des produit de prix.
    """
    
    #s:float
    s=0.0

    #d:int
    d=0
    
    for (i,j) in prix.items():
        s=s+j
        d=d+1

    return s/d

#Jeu de test:

assert prix_moyen(Magasin)==129.06

    #Question 4:

def fourchette_prix(mini, maxi, base):
    """
    number * number * Dict[str:float] -> set(str)
    """

    #E:set(float)
    E=set()

    for (i,j) in base.items():
        if j>mini and j<maxi:
           E.add(i)

    return E

    
#Jeu de test:

assert fourchette_prix(50.0,200.0,Magasin)=={'Coussin Linux','Mitendo DX','Station Nextpresso'}

    #Question 5:

F={'Sabre Laser':3,'Coussin Linux':2,'Slip Goldorak':1}

    #Question 6:

def tous_disponibles(Panier,Prix):
    """
    Dict[str:int] * Dict[str:float] -> bool
    """

    for i in Panier:
        if not i in Prix:
            return False

    return True

#Jeu de test:
assert tous_disponibles(F,Magasin)==True

    #Question 7:

def prix_achats(Panier,Prix):
    """
    Dict[str:int] * Dict[str:float] -> float
    Hypothèse : tous_disponible(Panier,Prix)==True
    """

    #s:float
    s=0.0

    for (i,j) in Panier.items():
        for (k,l) in Prix.items():
            if i==k:
                s=s+j*l

    return s

#Jeu de test:
assert prix_achats(F,Magasin)==865.9
