#exercice 5.3

def est_voyelle(c):
    """str -> bool
    Hypothèse : len(c) == 1
    retourne True si et seulement si c est une voyelle
    miniscule ou majuscule."""
    return (c =='a')or(c=='A')\
           or(c=='e')or(c=='E')\
           or(c=='i')or(c=='I')\
           or(c=='o')or(c=='O')\
           or(c=='u')or(c=='U')\
           or(c=='y')or(c=='Y')

# Jeu de tests
assert est_voyelle('a')==True
assert est_voyelle('E')==True
assert est_voyelle('b')==False
assert est_voyelle('y')==True
assert est_voyelle('z')==False

#Q2

def est_voyelles_accents(c):
    """str -> bool
    Hypothèse : len(c) == 1
    retourne True si et seulement si c est une voyelle
    miniscule ou majuscule."""
    return (c =='a')or(c=='A')\
           or(c=='e')or(c=='E')\
           or(c=='i')or(c=='I')\
           or(c=='o')or(c=='O')\
           or(c=='u')or(c=='U')\
           or(c=='y')or(c=='Y')\
           or(c =='ä')or(c=='Ä')\
           or(c=='é')or(c=='É')\
           or(c=='è')or(c=='È')\
           or(c=='à')or(c=='À')\
           or(c=='â')or(c=='Â')

# Jeu de tests
assert est_voyelles_accents('a')==True
assert est_voyelles_accents('É')==True
assert est_voyelles_accents('â')==True
assert est_voyelles_accents('y')==True
assert est_voyelles_accents('z')==False


def nb_voyelles(s):
    """str->int
    retourne le nombre de voyelles dans la chaine de caractères."""
    #res : int
    res=0
    #e : str
    for e in s:
        if est_voyelles_accents(e):
            res= res+1
    return res

assert nb_voyelles('la maman du petit enfant le console')==12
assert nb_voyelles('mr brrxcx')==0
assert nb_voyelles('ai al o ents')==5
assert nb_voyelles('la maman du bébé le réconforte')==11

def sans_voyelle(s):
    """str-> str
    elimine les voyelles d'une chaine de caractere"""

    #r : str
    r=''
    #e : str
    for e in s:
        if not est_voyelles_accents(e):
            r=r+e
    return r

assert sans_voyelle('aeiouy')==''
assert sans_voyelle('la balle au rebond')=="l bll  rbnd"

#exercice 5.6:

def base_comp(a):
    """str->str
    hyp: a = 'A' or 'c' or 'T' or 'G' 
    return la base complementaire"""
    if a =='A':
        return 'T'
    elif a =='G':
        return 'C'
    elif a =='T':
        return 'A'
    else:
        return 'G'
    
assert base_comp('C')=='G'
assert base_comp('G')=='C'
assert base_comp('A')=='T'
assert base_comp('T')=='A' 
    

#Q2

def brin_comp(s):
    """str->str
    Renvoie le brin complémentaire de s.
    """

    #r : str
    r = ''
    #e : str
    for e in s:
        r= r + base_comp(e)
    return r

assert brin_comp('ATCG')=='TAGC'
assert brin_comp('ATTGCCGTATGTATTGCGCT')=='TAACGGCATACATAACGCGA'
assert brin_comp('')==''

#Q3

def test_comp(a,b):
    """str^2->bool
    Renvoie true si a et b sont complémentaires
    """

    return brin_comp(a)==b

assert test_comp('ATCG','TAGC')==True
assert test_comp('','')==True
assert test_comp('ATCG','TAAG')== False
assert test_comp('ATTGCCGTATGTATTGCGCT','TAACGGCATACATAACGCGA')==True

#Q4

def test_sous_sequence(b1,b2):
    """str^2->bool
    Teste si b1 est une sous-séquence de b2.
    """
    #i : int
    i=0

    #j : int
    j=0
    
    #r : str
    r = ''
    
    while i <= len(b2)-len(b1):
        j=i
        while j<len(b1)+i:
            r=r+b2[j]
            j=j+1
        if r==b1:
            return True
        r= ''
        i=i+1
    return False        

assert test_sous_sequence('ATCG','')==False
assert test_sous_sequence('','')==True
assert test_sous_sequence('','ATCG')==True
assert test_sous_sequence('GC','TACG')==False
assert test_sous_sequence('CA','TAACGGCATACATAACGCGA')==True

def test_sous_sequence2(b1,b2):
    """str^2->bool
    Teste si b1 est une sous-séquence de b2.
    """

    #i : int
    i=0

    #j : int
    j=len(b1)

    while (i<=(len(b2)-len(b1))) and (b1 != b2[i:j]) :
        i=i+1
        j=j+1
    return b1 == b2[i:j]

assert test_sous_sequence2('ATCG','')==False
assert test_sous_sequence2('','')==True
assert test_sous_sequence2('','ATCG')==True
assert test_sous_sequence2('GC','TACG')==False
assert test_sous_sequence2('CA','TAACGGCATACATAACGCGA')==True

def test_sous_sequence3(b1,b2):
    """str^2->bool
    Teste si b1 est une sous-séquence de b2.
    """
    
    if len(b2)<len(b1):
        return False
    if b1 =='' and b2 =='':
        return True
    if b1 in b2:
            return True
    return False    

assert test_sous_sequence3('','ATCG')==True
assert test_sous_sequence3('CA','TAACGGCATACATAACGCGA')==True
assert test_sous_sequence3('GC','TACG')==False
assert test_sous_sequence3('ATCG','')==False
assert test_sous_sequence3('','')==True

            
def recherche_sous_sequence(b1,b2):
    """str^2->int
    Recherche la position de la sous_séquence dans la séquence s
    """
    #i : int
    i=0

    #j : int
    j=0
    
    #r : str
    r = ''
    
    while i <= len(b2)-len(b1):
        j=i
        while j<len(b1)+i:
            r=r+b2[j]
            j=j+1
        if r==b1:
            return i
        r= ''
        i=i+1  
        
assert recherche_sous_sequence('','')==0
assert recherche_sous_sequence('','ATCG')==0
assert recherche_sous_sequence('GC','TAGC')==2
assert recherche_sous_sequence('CA','TAACGGCATACATAACGCGA')==6
assert recherche_sous_sequence('ATCG','')==None
assert recherche_sous_sequence('GC','TAAC')==None

#exercice 5.7:

#Q1

def chiffre(c):
    """str->int
    retourne l’entier qui correspond au caractere representant un chiffre"""
    return ord(c)-48

assert chiffre('0')==0
assert chiffre('5')==5

#Q2

def entier(s):
    """str->int
    retourne l’entier représenté par une chaîne s"""
    #r : int
    r=0

    #n : int
    n=0

    #i : str
    for i in s:
        r=r+chiffre(i)*10**(len(s)-n-1)
        n=n+1
    return r

assert entier('9')==9
assert entier('0012')==12
assert entier('0')==0

def entier2(s):
    """str->int
    retourne l'entier représenté par une chaine s"""
    #r : int
    r=0
    #i : int
    i=0
    #e : str
    for e in s:
        r=r+(chiffre(s[len(s)-i-1])*10**i)
        i=i+1
    return r

assert entier2('9')==9
assert entier2('0012')==12
assert entier2('0')==0


#Q3

def caractere(n):
    """int->str
    retourne le caractere qui represente le chiffre n"""
    return chr(48+n)

assert caractere(8)=='8'
assert caractere(0)=='0'

#Q4
    
def chaine(n):
    """int->str
    retourne la chaine representant l'entier naturel n"""
    #r : str
    r=''

    #i : int
    i=n
    
    #c : int
    c=0
    
    if n==0:
        return '0'
    while i !=0:
        if i==0:
            r='0'+r
        else:
            c=i%10
            r=caractere(c)+r
            i=i//10
        
    return r

assert chaine(423)=='423'
assert chaine(0)=='0'
assert chaine(entier('420'))=='420'
assert entier(chaine(122))==122



    
    
