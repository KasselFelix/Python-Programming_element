
#Exercice 4.4

    #Question 1:

def nb_couples_intervalle(n,p):
    """
    Number^2 -> Number
    Hypothèse : n<p
    Retourne le nombre de couples d'entiers [i,j] appartenant à l'intervalle [n;p].
    """

    #i:int
    i=n

    #j:int
    j=p

    #s:int
    s=0

    while i<p:
        while n<j:
            j=j-1
            s=s+1            
        i=i+1
        j=i
    
    return s

#jeu de tests:
assert nb_couples_intervalle(0,0)==0
assert nb_couples_intervalle(2,4)==3
assert nb_couples_intervalle(-1,3)==10
assert nb_couples_intervalle(2,2)==0


    #Question 2:

def nb_couples_divise(n,p):
    """
    Number^2 -> Number
    Hypothèse : n<p
    Retourne le nombre de couples d'entiers [i,j] appartenant à l'intervalle [n;p] tel que i divise j.
    """

    #i:int
    i=n

    #j:int
    j=p

    #s:int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            if i!=0 and j%i==0 and i<j:
                s=s+1
            j=j+1     
        i=i+1
    return s

#jeu de tests:
assert nb_couples_divise(4,6)==0
assert nb_couples_divise(2,6)==3
assert nb_couples_divise(-1,1)==2
assert nb_couples_divise(1,10)==17

    #Question 3:

def nb_couples_divise_trace(n,p):
    """
    Number^2 -> Number
    Hypothèse : n<p
    Affiche tous les couples d'entiers [i,j] appartenant à l'intervalle [n;p], et met en evidence les couples ou i divise j.
    Et affiche le nombre de couple ou i divise j.
    """

    #i:int
    i=n

    #j:int
    j=p

    #s:int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            print("couple (",i,",",j,")")
            if i!=0 and j%i==0 and i<j:
                s=s+1
                print("------------")
                print(i,"divise",j,"!")  #Rajouter un Print que ici permet de donné uniquement les couples ou i divise j ! 
                print("------------")
            j=j+1
        i=i+1
        
    print ("Il y a",s,"couple") #On retire le return mais pour eviter que "s" se balade tout seul on ajoute un texte. 

    #Question 4:

def existe_couples_divise_rapide(n,p):
    """
    Number^2 -> boolean
    Hypothèse : n<p
    renvoie True s'il existe couple d'entiers [i,j] appartenant à l'intervalle [n;p], tel que i divise j
    ou False sinon
    """
    #i:int
    i=n

    #j:int
    j=p

    #s:int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            if i!=0 and j%i==0 and i<j:
                s=s+1
                i=p+1 #Sortie anticipé de boucle
            j=j+1
            
        i=i+1
        
    return s>0

#jeu de tests:
assert existe_couples_divise_rapide(0,0)==False
assert existe_couples_divise_rapide(2,6)==True
assert existe_couples_divise_rapide(-1,1)==True
assert existe_couples_divise_rapide(1,10)==True
assert existe_couples_divise_rapide(21,34)==False





    #Question 5:

def existe_couples_divise_rapide2(n,p):
    """
    Number^2 -> boolean
    Hypothèse : n<p
    renvoie True s'il existe couple d'entiers [i,j] appartenant à l'intervalle [n;p], tel que i divise j
    ou False sinon
    """
    #i:int
    i=n

    #j:int
    j=p

    #s:int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            if i!=0 and j%i==0 and i<j:
                return True # Sortie anticipé de fonction !
            j=j+1
        i=i+1
        
    return False

#jeu de tests:
assert existe_couples_divise_rapide2(0,0)==False
assert existe_couples_divise_rapide2(2,6)==True
assert existe_couples_divise_rapide2(-1,1)==True
assert existe_couples_divise_rapide2(1,10)==True
assert existe_couples_divise_rapide2(21,34)==False

    #Question 6:

def existe_couples_divise_trace_3en1(n,p):
    """
    Number^2 -> boolean
    Hypothèse : n<p
    renvoie True s'il existe couple d'entiers [i,j] appartenant à l'intervalle [n;p], tel que i divise j
    ou False sinon
    """
    #i:int
    i=n

    #j:int
    j=p

    #s:int
    s=0

    #cpt:int
    cpt=0
    cpt2=0
   
    while i<p:
        j=i+1
        while j<=p:
            cpt=cpt+1
            if i!=0 and j%i==0 and i<j:
                if s==0:
                    s=s+1
                    cpt2=cpt
                else:
                    s=s+1
            j=j+1
        i=i+1

    print("Nombre de couples testés (basique): ",cpt)
    print("Nombre de couples testés (rapide): ",cpt2)
    return s>0


#Exercice 4.6

    #Question 1:

def decalage(c,d):
    """
    Number^2 -> Number
    Hypothèse : c est plus petit que 10.
    Renvoie le chiffre c décalé de d unités.
    """

    return (c+d)%10

#Jeu de tests:
assert decalage(0,2)==2
assert decalage(8,2)==0
assert decalage(9,2)==1
assert decalage(2,1)==3


    #Question 2 : #Avec fonction Partie Entiere!

def partie_entiere(x):
    """
    Number -> Number
    Retourne la partie entière de x.
    """

    #i:int
    i=0

    if x>0:
        while i<=x:
            i=i+1
    else:
        while i>=x:
            i=i-1

    if i<0:
        return i
    else:
        return i-1
    
def encodage(c,d):
    """
    Number^2 -> Number
    Hypothese: 10 <= C <= 9999 
    Renvoie de chiffre c encodé.
    """
    #D'apres l'enonce: Unite = d ! et on rajoute 1 a gauche

    unite=decalage(c%10,d) #C%10 donne ici le dernier chiffre du nombre c avec decalage d (soit les unité)
    dizaine=decalage(partie_entiere(c/10),d) #On utilise Partie Entiere pour recupere le premier chiffre (soit les dizaine)

    if c<1000 and c>99: #On traite le cas des nombre a 3 chiffre
        centaine=decalage(partie_entiere(c/100),d)
        return 1*1000+centaine*1000+dizaine*100+unite*10+d
    if c<10000 and c>999: #On traite le cas des nombre a 4 chiffre
        centaine=decalage(partie_entiere(c/100),d)
        millier=decalage(partie_entiere(c/1000),d)
        return 1*100000+millier*10000+centaine*1000+dizaine*100+unite*10+d

    #Meme logique pour les nombres a + de 4 chiffre

    return 1*1000+dizaine*100+unite*10+d #Ici le return pour un nombre a 2 chiffre

#jeu de tests:
assert encodage(84,2)==1062
assert encodage(1234,3)==145673
assert encodage(90,1)==1011

    #Question 4:

def encodage_inv(c,d):
    """
    Number^2 -> Number
    Hypothese: 10 <= C <= 9999
    Renvoie de chiffre c encodé inverse.
    """
    

    unite=decalage(c%10,d) 
    dizaine=decalage(partie_entiere(c/10),d)

    if c<1000 and c>99:
        centaine=decalage(partie_entiere(c/100),d)
        return 1*1000+unite*1000+dizaine*100+centaine*10+d
    if c<10000 and c>999:
        centaine=decalage(partie_entiere(c/100),d)
        millier=decalage(partie_entiere(c/1000),d)
        return 1*100000+unite*10000+dizaine*1000+centaine*100+millier*10+d

    return 1*1000+unite*100+dizaine*10+d

#Jeu de test:

assert encodage_inv(84,2)==1602
assert encodage_inv(1234,3)==176543
assert encodage_inv(90,1)==1101

#Exercice 4.7

    #Question 1:

def factorielle(n):
    """ int -> int
    hypothese : n >= 0
    Retourne le produit factoriel n!
    et affiche le nombre d'operation
    """
    
    # k : int
    k = 1 # on démarre au rang 1
    
    # f : int
    f = 1 # factorielle au rang 1

    # nb_ops: int
    nb_ops=0
    
    while k <= n:
        nb_ops=nb_ops+1
        f = f * k
        k = k + 1
     
    return f

def factorielle_trace(n):
    """ int -> int
    hypothese : n >= 0
    Retourne le produit factoriel n!
    et affiche le nombre d'operation
    """
    
    # k : int
    k = 1 # on démarre au rang 1
    
    # f : int
    f = 1 # factorielle au rang 1

    # nb_ops: int
    nb_ops=0
    
    while k <= n:
        nb_ops=nb_ops+1
        f = f * k
        k = k + 1

    print("Nombre d'operation = ",nb_ops)
    print("Nombre de multiplication = ",nb_ops-1)
     
    return f

    #Question 2:

def combinaison (n,k):
    """ int*2 -> number*2
    hypothese: k<=n
    Renvoie le nombre de facon de choisir k dans un ensemble E de taille n
    """

    #factn: int
    factn=factorielle(n) #n!

    #factk: int
    factk=factorielle(k) #k!

    #factn_k: int
    factn_k=factorielle((n-k)) #(n-k)!

    #s:int
    s= (factn)/(factk*factn_k)

    return s #Ou en 1 seul ligne: return (factorielle(n))/(factorielle(k)*factorielle((n-k)))

assert combinaison(5,3)==10
assert combinaison(10,4)==210
assert combinaison(12,6)==924

    #Question 3:
"""Le nombre de multiplication corespondrais a nb_ops-1 des 3 factorielle calculer dans combinaison + 1"""

    #Question 4:

def combis_rapide(n,k):
    """ int*2 -> number*2
    hypothese: k<=n
    Renvoie le nombre de facon de choisir k dans un ensemble E de taille n
    en plus rapide
    """

    #i:int
    i=1

    #s:int
    s=1

    while i <= k:
        s = s * ((n+1-i)/i)
        i = i + 1

    return s

assert combis_rapide(5,3)==combinaison(5,3)
assert combis_rapide(10,4)==combinaison(10,4)

#Exercice 4.8

    #Question 1:

def plus_grand(n):
    """
    Number -> Boolean
    Renvoie True si n est plus grand que m.
    """

    #m:int
    m=2014

    if n>=m:
            return False
    else:
        return True


#Jeu de tests:
    assert plus_grand(2)==True
    assert plus_grand(2014)==False
    assert plus_grand(2548)==False
    

    #Question 2:

def divination():
    """
    NoneType -> Number
    Trouve le nombre choisi par Alice.
    """

    #i:int
    i=0
    
    while plus_grand(i)==True:
        i=i+1

    return i


    #Question3:

def divination_rapide(k):
    """
    Number -> Number
    Hypothèse : m est compris entre 0 et k.
    Trouve le nombre choisi par Alice.
    """

    #i:int
    i=0

    #t:int
    t=k

    while plus_grand(i)==True:
        if plus_grand(t)==False:
            t=t-1
        i=i+1
        

    if plus_grand(i)==False:
        return i
    elif plus_grand(t)==True:
        return t+1

