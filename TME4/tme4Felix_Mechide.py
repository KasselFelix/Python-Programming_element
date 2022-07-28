#exercice 4.4

#Q1

def nb_couples_intervalle(n,p):
    """int^2->int
    hyp: i<j
    hyp: n<=p
    renvoie le nombres de couples(i,j) appartenant a l'intervalle [n,p]"""

    #i : int
    i=n
    
    #j : int
    j=p

    #s : int
    s=0

    while i < p:
        while j>n:
            j=j-1
            s=s+1
            print("i =",i,"\nj =",j,"\ns =",s)
        i=i+1
        j=i
    return s            

assert nb_couples_intervalle(0,0)==0
assert nb_couples_intervalle(2,4)==3
assert nb_couples_intervalle(-1,3)==10


#Q2
#Q3

def nb_couples_divise(n,p):
    """int^2->int
    hyp: j%i==0
    hyp: n<=p
    renvoie le nombres de couples(i,j) appartenant a l'intervalle [n,p]"""

    #i :int
    i=n  

    #j :int
    j=n

    #s :int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            print("couple (",i,",",j,")")
            if i!=0 and j%i==0:
                s=s+1
                print("------------")
                print(i,"divise",j,"!")
                print("------------")
            j=j+1
                
        i=i+1
    return s

assert nb_couples_divise(4,6)==0
assert nb_couples_divise(2,6)==3
assert nb_couples_divise(-1,1)==2
assert nb_couples_divise(1,10)==17


#Q4

def existe_couples_divise(n,p):
    """int^2 -> bool
    hyp: n<=p
    renvoie True s'il existe couple d'entiers [i,j]
    appartenant à l'intervalle [n;p], tel que i divise j
    ou False sinon
    """
    return nb_couples_divise(n,p) >0


assert existe_couples_divise(0,0)==False
assert existe_couples_divise(2,6)==True
assert existe_couples_divise(-1,1)==True
assert existe_couples_divise(1,10)==True
assert existe_couples_divise(21,34)==False

def existe_couples_divise_rapide(n,p):
    """int^2 -> bool
    hyp: n<=p
    renvoie True s'il existe couple d'entiers [i,j]
    appartenant à l'intervalle [n;p], tel que i divise j
    ou False sinon
    """
    #i:int
    i=n

    #j:int
    j=n

    #s:int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            if i!=0 and j%i==0:
                s=s+1
                i=p+1 
            j=j+1
            
        i=i+1
        
    return s>0


assert existe_couples_divise_rapide(0,0)==False
assert existe_couples_divise_rapide(2,6)==True
assert existe_couples_divise_rapide(-1,1)==True
assert existe_couples_divise_rapide(1,10)==True
assert existe_couples_divise_rapide(21,34)==False



#Q5:

def existe_couples_divise_rapide2(n,p):
    """int^2 -> bool
    hyp: n<=p
    renvoie True s'il existe couple d'entiers [i,j]
    appartenant à l'intervalle [n;p], tel que i divise j
    ou False sinon
    """
    #i:int
    i=n

    #j:int
    j=n

    #s:int
    s=0

    while i<p:
        j=i+1
        while j<=p:
            if i!=0 and j%i==0:
                return True 
            j=j+1
        i=i+1
        
    return False

assert existe_couples_divise_rapide2(0,0)==False
assert existe_couples_divise_rapide2(2,6)==True
assert existe_couples_divise_rapide2(-1,1)==True
assert existe_couples_divise_rapide2(1,10)==True
assert existe_couples_divise_rapide2(21,34)==False

#Q6

def existe_couples_divise_rapide_trace_tour(n,p):
    """int^2-> bool
    hyp: n<=p
    affiche le nombre de couples testés et renvoie si
    il un existe couple d'entiers [i,j]
    appartenant à l'intervalle [n;p], tel que i divise j"""

    #i : int
    i=n

    #j : int
    j=n

    #s : int
    s=0
    
    while i<p:
        j=i+1
        while j<=p:
            s=s+1
            if i!=0 and j%i==0:
                print("nombre de couples testés :",s)
                return True
            j=j+1  
        i=i+1
    print("nombre de couples testés :",s)
    return False

assert existe_couples_divise_rapide_trace_tour(3,1000)==True
assert existe_couples_divise_rapide_trace_tour(21,35)==False
        
#exercice 4.8


#Q1
def plus_grand(n):
    """Number->bool
    hyp: n and m >0
    return True si m>n False sinon"""

    #m : int
    m=2014

    if n < m:
        return True
    return False

assert plus_grand(100)==True
assert plus_grand(2014)==False
assert plus_grand(3000)==False

#Q2

def divination():
    """->Number
    hyp: n and m >0
    trouve le nombre choisi par Alice"""

    #i :int
    i=1

    while plus_grand(i):
        i=i+1
    return i

assert divination()==2014

#pas tres efficace,prendre un nombre grand,
#obtenir un intervalle et reduire, obtenir un nouvelle intervalle
#puis reduire jusque a obtenir m

#Q3

def divination_rapide(k):
    """Number->int
    hyp: n and m and k >0,m est compris entre 0 et k.
    trouve le nombre choisi par Alice"""
    #i :int
    i = 1

    #t : Number
    t=k

    while plus_grand(i)==True:
        if plus_grand(t)==False:
            t=t-1
        i=i+1
        

    if plus_grand(i)==False:
        return i
    elif plus_grand(t)==True:
        return t+1
            
assert divination_rapide(10000)==2014
