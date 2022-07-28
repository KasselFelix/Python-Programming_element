#Exercice 5.1:
    #Question 1:

def produit_cubes(m,n):
    """
    Number -> Number
    Hypothese: M<N ! (Intervale [m,n])
    Renvoie le produit des puissance cubiques des entiers entre m et n.
    """

    #p:int
    p=1

    #k: int
    #k=m       #On peux mettre directement m dans le while

    while m<n:
        p = p*m**3  #m**3 = m*m*m
        m=m+1

    return p


def produit_cubes_avec_for(m,n):
    """
    Number -> Number
    Hypothese: M<N ! (Intervale [m,n]
    Renvoie le produit des puissance cubiques des entiers entre m et n.
    En utilisant un for!
    """

    #s:int
    s=1

    for i in range(m,n):
        s=s*i**3

    return s

#Jeu de tests:
assert produit_cubes_avec_for(4,8)==produit_cubes(4,8)==592704000

#Exercice 5.2:

def nombre_de_chiffre(a):
    """
    str -> number
    Retourne le nombre de chiffre dans la chaine de caractere a
    """

    #b:int
    b=0

    for c in a:
        if c >= '0' and c <= '9':
            b=b+1

    return b

#Jeu de tests:
assert nombre_de_chiffre('bonjour')==0
assert nombre_de_chiffre('un:1')==1
assert nombre_de_chiffre('10 auout')==2
assert nombre_de_chiffre('606060')==6

#Exercice 5.3:

def est_voyelle(c):
    """
    Str -> Bool
    Hypothèse : len(c)==1
    Retourne True si et seulement si c est une voyelle minuscule ou majuscule.
    """

    return (c=='a') or (c=='A')\
        or (c=='e') or (c=='E')\
        or (c=='i') or (c=='I')\
        or (c=='o') or (c=='O')\
        or (c=='u') or (c=='U')\
        or (c=='y') or (c=='Y')

#Jeu de tests:
assert est_voyelle('a')==True
assert est_voyelle('E')==True
assert est_voyelle('b')==False
assert est_voyelle('y')==True
assert est_voyelle('z')==False

    #Question 1:

def nb_voyelles(s):
    """
    Str -> Int
    Retourne le nombre de voyelles dans la chaine de caractères.
    """

    #nb:int
    nb=0

    for i in s:
        if est_voyelle(i)==True:
            nb=nb+1

    return nb

#Jeu de tests:
assert nb_voyelles('la maman du petit enfant le console')==12
assert nb_voyelles('mr brrxcx')==0
assert nb_voyelles('ai al o ents')==5
assert nb_voyelles('la maman du bébé le réconforte')==8

    #Question 2:

def est_voyelle_accents(c):
    """
    Str -> Bool
    Hypothèse : len(c)==1
    Retourne True si et seulement si c est une voyelle minuscule ou majuscule.
    """

    return (c=='a') or (c=='A')\
        or (c=='e') or (c=='E')\
        or (c=='i') or (c=='I')\
        or (c=='o') or (c=='O')\
        or (c=='u') or (c=='U')\
        or (c=='y') or (c=='Y')\
        or (c=='é') or (c=='à')\
        or (c=='ù') or (c=='è')\
        or (c=='ê')                 #Liste incomplete


#Jeu de tests:
assert est_voyelle_accents('à')==True
assert est_voyelle_accents('E')==True
assert est_voyelle_accents('b')==False
assert est_voyelle_accents('é')==True
assert est_voyelle_accents('è')==True

def nb_voyelles_accents(s):
    """
    Str -> Int
    Retourne le nombre de voyelles dans la chaine de caractères.
    """

    #nb:int
    nb=0

    for i in s:
        if est_voyelle_accents(i)==True:
            nb=nb+1

    return nb

#Jeu de tests:
assert nb_voyelles_accents('la maman du bébé le réconforte')==11
assert nb_voyelles_accents('ài àl o énts')==5

    #Question 3:

def sans_voyelle(s):
    """
    Str -> Str
    Retourne la chaîne de caractère sans voyelles.
    """

    #r:str
    r=''
    
    for i in s:
        if est_voyelle_accents(i)==False: #Le False conditione l'entre dans la nouvelles chaine 'r' que l'on retourne
            r=r+i

    return r

#Jeu de tests:
assert sans_voyelle('aeiouy')==''
assert sans_voyelle('la balle au bond rebondit')=='l bll  bnd rbndt'
assert sans_voyelle('mr brrxcx')=='mr brrxcx'

    #Question 4:

def mot_mystere(s):
    """
    Str -> Str
    Remplace les voyelles par un underscore_.
    """

    #r:str
    r=''

    for i in s:
        if est_voyelle_accents(i)==False: #On reprend Question 3 
            r=r+i
        else:
            r=r+'_'

    return r

#Jeu de tests:
assert mot_mystere('aeiouy')=='______'
assert mot_mystere('la balle au bond rebondit')=='l_ b_ll_ __ b_nd r_b_nd_t'
assert mot_mystere('mr brrxcx')=='mr brrxcx'

#Exercice 5.4

    #Question 1:

def est_palindromme(s):
    """
    Str -> Bool
    Retourne True si s est un palindromme.
    """

    #r:str
    r=''

    for i in s:
        r=i+r #On obtien l'inverse du nombre [!] r+i avec des lettre c'est pas comme i+r

    return r==s

#Jeu de tests:
assert est_palindromme('')==True
assert est_palindromme('je ne suis pas un palindrome')==False
assert est_palindromme('aba')==True
assert est_palindromme('amanaplanacanalpanama')==True

    #Question 2:

def miroir(s):
    """
    Str -> Str
    Forme un palindromme.
    """

    #r:str
    r=''

    for i in s:
        r=i+r #On reprend question 1

    return s+r

#Jeu de tests:
assert miroir('amanaplanacanalpanama')=='amanaplanacanalpanamaamanaplanacanalpanama'
assert miroir('abc')=='abccba'
assert miroir('do-re-mi-fa-sol')=='do-re-mi-fa-sollos-af-im-er-od'
assert est_palindromme(miroir('je ne suis pas un palindrome'))==True

#Exercice 5.5:

    #Question 1:

def suppression(c,s):
    """
    Str^2 -> Str
    Supprime le caractère c de la chaîne s.
    """

    #r:str
    r=''
    
    for i in s:
        if i!=c:
            r=r+i

    return r

def suppression2(c,s):
    """
    Str^2 -> Str
    Supprime le caractère c de la chaîne s.
    Variante possible
    """

    #r:str
    r=''
    
    for i in s:
        if i==c:
            r=r
        else:       #Plus long !
            r=r+i

    return r

#Jeu de tests:
assert suppression('a','')==''
assert suppression('a','aaaaa')==''
assert suppression('p','le papa noel')=='le aa noel'
assert suppression('a','bbbbb')=='bbbbb'
assert suppression2('p','le papa noel')==suppression('p','le papa noel')


#Question 2:

def suppression_debut(c,s):
    """
    Str^2 -> Str
    Supprime la première occurence du caractère c dans la chaîne s.
    """

    #r:str
    r=''

    #o:bool
    o=False  #Ou cpt=0 et on incremente cpt pour sortir du if!
    
    for i in s:
        if i!=c:
            r=r+i
        elif o==True:
            r=r+i
        else:
            o=True

    return r

#Jeu de tests:
assert suppression_debut('a','')==''
assert suppression_debut('a','aaaaa')=='aaaa'
assert suppression_debut('p','le papa noel')=='le apa noel'
assert suppression_debut('a','bbbbb')=='bbbbb'

    #Question 3:

def suppression_fin(c,s):
    """
    Str^2 -> Str
    Supprime la dernière occurence d caractère c dans la chaine s.
    """

    #r:str
    r=''

    for i in s:     #On inverse la chaine de caractere
        r=i+r

    r=suppression_debut(c,r) #On applique suppression_debut (qui supprime donc le premier en partant de la fin)
    s=''
    
    for i in r:
        s=i+s  #On inverse de nouveau pour remettre la chaine dans l'ordre initial

    return s

#Jeu de tests:
assert suppression_fin('a','')==''
assert suppression_fin('a','aaaaa')=='aaaa'
assert suppression_fin('p','le papa noel')=='le paa noel'
assert suppression_fin('a','bbbbb')=='bbbbb'

#suppression_fin peut se faire en comptant le nombre total de caractere n
# puis en recherchant le caractere c le plus proche de n pour le supprime (Super long)

def base_comp(c):
    """
    Str -> Str
    Donne la base complémentaire de c.
    """

    if c=='A':
        return 'T'
    elif c=='G':
        return 'C'
    elif c=='T':
        return 'A'
    elif c=='C':
        return 'G'

#Comme avec est_voyelle on traite les tous les cas directement
    
#Jeu de tests:
assert base_comp('A')=='T'
assert base_comp('G')=='C'
assert base_comp('T')=='A'
assert base_comp('C')=='G'

    #Question 2:

def brin_comp(s):
    """
    Str -> Str
    Renvoie le brin complémentaire de s.
    """

    #r:str
    r=''

    for i in s:
        r=r+base_comp(i)

    return r

#Meme principe que mot mystere mais au lieux de remplacer par '_' on remplace par la base_comp

#Jeu de tests:
assert brin_comp('ATCG')=='TAGC'
assert brin_comp('ATTGCCGTATGTATTGCGCT')=='TAACGGCATACATAACGCGA'
assert brin_comp('')==''

    #Question 3:

def test_comp(a,b):
    """
    Str^2 -> Str
    Renvoie true si a et b sont complémentaires.
    """

    a=brin_comp(a)

    return a==b

#On creer le complementaire de a et on le compare a b

#Jeu de tests:
assert test_comp('','')==True
assert test_comp('','ATCG')==False
assert test_comp('ATCG','')==False
assert test_comp('ATCG','TAGC')==True
assert test_comp('ATCG','TAAG')==False
assert test_comp('ATTGCCGTATGTATTGCGCT','TAACGGCATACATAACGCGA')==True


    #Question 4:

def test_sous_sequence(b1,b2):
    """
    Str^2 -> Bool
    Hypothese: b1 < b2 sinon la fonction return False!
    Teste si b1 est une sous-séquence de b2.
    """

    #lss:int (longueur de la sous-séquence)
    lb1=0

    #ls:int
    lb2=0

    #j:int
    j=0

    #i:int
    i=0

    #r:str
    r=''

    for i in b1:        #On determine la longeur de b1
        lb1=lb1+1

    for i in b2:        #On determine la longeur de b2
        lb2=lb2+1

    while j<=lb2-lb1:
        i=j
        while i<lb1+j:
            r=r+b2[i]   #On extrait une sous chaine
            i=i+1
        if r==b1:       #On la compare
            return True
        j=j+1
        r=''
    return False

#Jeu de tests:
assert test_sous_sequence('','')==True
assert test_sous_sequence('','ATCG')==True
assert test_sous_sequence('ATCG','')==False
assert test_sous_sequence('GC','TAGC')==True
assert test_sous_sequence('GC','TAAG')==False
assert test_sous_sequence('CA','TAACGGCATACATAACGCGA')==True
assert test_sous_sequence('ATCA','CA')==False

    #Question 5:

def recherche_sous_sequence(b1,b2):
    """
    Str^2 -> number
    Recherche la position de la sous_séquence ss dans la séquence s.
    """

    #lss:int
    lb1=0

    #ls:int
    lb2=0

    #j:int
    j=0

    #i:int
    i=0

    #r:str
    r=''

    for i in b1:    #On determine la longeur de b1
        lb1=lb1+1

    for i in b2:    #On determine la longeur de b2
        lb2=lb2+1

    while j<=lb2-lb1:
        i=j
        while i<lb1+j:
            r=r+b2[i] #On extrait une sous chaine
            i=i+1
        if r==b1: #On la compare
            return j #On retourne la position
        j=j+1
        r=''

    #Rien a la sortis de boucle, la fonction renvoie donc None !
#Jeu de tests:
assert recherche_sous_sequence('','')==0
assert recherche_sous_sequence('','ATCG')==0
assert recherche_sous_sequence('ATCG','')==None
assert recherche_sous_sequence('GC','TAGC')==2
assert recherche_sous_sequence('GC','TAAC')==None
assert recherche_sous_sequence('CATA','TAACGGCATACATAACGCGA')==6

#Exercice 5.7:

    #Question 1:

def chiffre(s):
    """
    Str -> Number
    Hypothese: s est forcement un chiffre compris entre 1 et 9 en caractere!
    Convertis le caractère en chiffre.
    """

    #Unicode de 1 a 9 -> 48 a 57
    #Donc 57-48 -> 9 d'ou:
    
    return ord(s)-48

#Jeu de tests:
assert chiffre('5')==5
assert chiffre('8')==8

    #Question 2:

def entier(s):
    """
    Str -> Number
    Hypothese: s est forcement une chaine de caractere representant un entier!
    Convertis la chaîne de caractère en entier.
    """

    #t:int
    t=0

    #r:int
    r=0
    
    for i in s: #On regarde combien de caractere(chiffre) dans s
        t=t+1

    for i in s:
        r=r+chiffre(i)*10**(t-1) #On creer l'entier en partant de son premier chiffre 10^t-1 (unité = 10^0)
        t=t-1

    return r

#Jeu de tests:
assert entier('9')==9
assert entier('42')==42
assert entier('0')==0
assert entier('0012')==12

    #Question 3:

def caractere(n):
    """
    Number -> Str
    Hypothese n compris entre 1 et 9 !
    Convertis la chiffre en caractère.
    """

    return chr(n+48)

#Jeu de tests:
assert caractere(8)=='8'
assert caractere(4)=='4'

    #Question 4:
def chaine(n):
    """
    Number -> Str
    Retourne la chaîne représentant l'entier n.
    """

    #i:int
    i=1

    #j:int
    j=0

    #r:str
    r=''

    while i<=n: #On compte combien de chiffre compose l'entier
        i=i*10
        j=j+1

    while j>0:
        j=j-1
        r=r+caractere((n//10**j)-(n//10**(j+1))*10) #On applique caractere en partant du premier chiffre de n

    return r

#Jeu de tests:
assert chaine(9)=='9'
assert chaine(42)=='42'
assert chaine(entier('122'))=='122'
assert entier (chaine(122))==122

#Exercice 5.8:

def est_chiffre(c):
    """
    Str -> Bool
    Hypothèse : len(c)==1
    Retourne True si et seulement si c est un chiffre.
    """

    return ('0' <= c) and (c <= '9')

#Jeu de tests:
assert est_chiffre('4')==True
assert est_chiffre('9')==True
assert est_chiffre('x')==False

    #Question 1:

def decompression(s):
    """
    Str -> Str
    Décompresse la chaîne s.
    """

    #r:str
    r=''

    #t:int
    t=0

    for i in s:
        if est_chiffre(i)==True: #Si le caractere est un chiffre on le transforme en indice
            t=int(i) #On peux aussi utilisé chiffre(i) de l'exercice 5.7
        elif t!=0:
            r=r+t*i
            t=0
        else:
            r=r+i

    return r

#Ne traite pas le cas ou len(n)>1 donc decompression('ab10cd') renvoie 'abcd'

#Jeu de tests:
assert decompression('ab3cd')=='abcccd'
assert decompression('ab3c2d4efgh')=='abcccddeeeefgh'
assert decompression('abcdefg')=='abcdefg'
assert decompression('abc11d')=='abcd'

    #Question 2:

def compression(s):
    """
    Str -> Str
    Compresse la chaîne s.
    """

    #r:str
    r=''

    #temp:str
    temp=''

    #j:int
    j=1

    for i in s:
        if temp==i:
            j=j+1
        elif j!=1:
            r=r+str(j)+i #On peux aussi utilisé caractere(j)
            j=1
        else:
            r=r+i
        temp=i

    return r

#Si un caractere est repete plus de 9 fois il seras impossible de decompresé la chaine !

#Jeu de tests:
assert compression('abcccd')=='abc3d'
assert compression('abcccddeeeefgh')=='abc3d2e4fgh'
assert decompression(compression('ab3cd'))=='abcccd'
assert compression('abcccccccccccd')== 'abc11d'

#Exercice 5.9:

    #Question 1:

def moins_lettre(c,a):
    """
    Str -> Str
    Supprime la première occurence de la lettre a dans la chaîne c ou renvoie none si c ne contient pas a.
    """

    #r:str
    r=suppression_debut(a,c) #On reutilise suppression_debut de l'exercice 5.5
    
    if r!=c:
        return r
    else:
        return None

#Jeu de tests:
assert moins_lettre('abcdefg','b')=='acdefg'
assert moins_lettre('bonbon','b')=='onbon'
assert moins_lettre('a','b')==None


    #Question 2:

def anagramme(m1,m2):
    """
    Str^2 -> Bool
    Retourne True si et seulement si m1 et m2 sont annagrammes.
    """

    for i in m1:
        if moins_lettre(m2,i)!=None:
            m2=moins_lettre(m2,i)
        else:
            return False

    return m2==''

#Jeu de tests:
assert anagramme('alberteinstein','riennestetabli')==True
assert anagramme('alberteinstein','toutestrelatif')==False
assert anagramme('lesfeuxdelamour','dramesexuelflou')==True

    #Question 1:

import random

def choix_parmi(n):
    """
    Number -> Number
    Choisi un nombre au hasard entre 1 et n.
    """

    n=random.random()*n+1

    return int(n)

    #Question 2:

def sujet(n):
    """
    Int -> Str
    Hypothèse: n>0
    Retourne un sujet de phrase.
    """

    if n==1:
        return 'le chat'
    elif n==2:
        return 'la fleur'
    elif n==3:
        return 'le voisin'
    elif n==4:
        return "l'infirmière"
    else:
        return "l'aspirateur"

def choix_sujet():
    """
    NoneType -> Str
    Choisi un sujet au hasard.
    """

    return sujet(choix_parmi(5))

    #Question 3:

#On reprend le procede de la question 1 et 2 et on l'applique au verbe et au complement !

def verbe(n):
    """
    Int -> Str
    Hypothèse: n>0
    Retourne un verbe.
    """

    if n==1:
        return 'mange'
    elif n==2:
        return 'assemble'
    elif n==3:
        return 'cultive'
    elif n==4:
        return 'prend'
    else:
        return 'imagine'

def complement(n):
    """
    Int -> Str
    Hypothèse: n>0
    Retourne un complément.
    """

    if n==1:
        return 'la tartiflette'
    elif n==2:
        return 'de la tomate pas vraiment fraiche'
    elif n==3:
        return "l'escalier"
    elif n==4:
        return 'la morue'

def choix_complement():
    """
    NoneType -> Str
    Choisi un complement au hasard.
    """

    return complement(choix_parmi(4))

def choix_verbe():
    """
    NoneType -> Str
    Choisi un verbe au hasard.
    """

    return verbe(choix_parmi(5))

#On creer une phrase en utilisant les 3 choix (sujet + verbe + comlement
#On oublie pas de separé par des espaces et on rajoute le point final !

def phrase():
    """
    NoneType -> Str
    COnstruit une phrase au hasar.
    """

    return choix_sujet() + ' ' + choix_verbe() + ' ' + choix_complement() + '.'

#En plus:

    #Question 1 Exercice 5.7: Avec Decompression gerant len(n)>2

def decompression2(s):
    """
    Str -> Str
    Décompresse la chaîne s.
    si n (de nc) est superieur a 9 ca marche
    """

    #r:str
    r=''

    #t:int
    t=0

    #i:int
    i=0
    
    #j:int
    j=0
    
    #cpt:int
    cpt=0
    
    while i < len(s):
        j=i
        t=0
        cpt=0
        while est_chiffre(s[i])==True:
            t2=j
            cpt=cpt+1
            i=i+1   
        while cpt+1 > 1:
            t=t+(chiffre(s[j])*(10**(cpt-1)))
            j=j+1
            cpt=cpt-1     
        if cpt==1:
            t=chiffre(s[j])
            r=r+t*s[i]
            t=0
            cpt=2
            i=i+1
        if cpt==0:
            if t!= 0:
                r=r+t*s[i]
            else:
                r=r+s[i]
            i=i+1

    return r

#Jeu de tests:
assert decompression2('ab3cd')=='abcccd'
assert decompression2('ab3c2d4efgh')=='abcccddeeeefgh'
assert decompression2('abcdefg')=='abcdefg'
assert decompression2('abc11d')=='abcddddddddddd'


    #Question 2 Exercice 5.7

def compression2(s):
    """
    Str -> Str
    Compresse la chaîne s.
    """

    #r:str
    r=''

    #temp:str
    temp= s[0]

    #j:int
    j=0
    
    for i in s:
        if temp==i:
            j=j+1
        elif j>1:
            r=r+str(j+1)+temp
        else:
            r=r+temp
            j=0
        temp=i

    return r

#assert compression2('abcccd')=='ab3cd'
