# exercice 2.2:

#Q1:
import math

def volume_tetraedre(a,b,c,d,e,f):
    """ Number^6-> float
    calcule le volume du tetraedre
    a,b,c,d,e,f >= 0"""
    #x:float
    x=a**2+b**2-a**2
    #y:float
    y=b**2+c**2-e**2
    #z:float
    z=a**2+c**2-f**2
    #p:float
    p= 4*a**2*b**2*c**2
    #q:float
    q=a**2*x**2+b**2*z**2+c**2*y**2
    #r:float
    r=x*y*z
    return 1/12*math.sqrt(p-q+r)
#Q2:

def volume_tetraedre_regulier(L):
    """Number-> float
    calcule le volume du tetraedre regulier
    L>=0"""
    return volume_tetraedre(L,L,L,L,L,L)

#exercice 2.3:

#Q1:

def mention(note):
    """Number-> NoneType
    0<=note<=20
    renvoie une chaine de caratere"""
    if note >= 16:
        return "TB"
    elif note >=  14:
        return "B"
    elif note >= 12:
        return "AB"
    elif note >= 10:
        return "Passable"
    else:
        return "Eliminé"


# exercice 2.5:

#Q1:

def ou(p,q):
    """bool*bool->bool
    return la disjonction de p et q"""
    if p:
        return p
    return q

assert ou(True,False)==True
assert ou(False,False)==False
assert ou(True,True)==True
assert ou(False,True)==True
    
def et(p,q):
    """bool*bool->bool
    return la conjonction de p et q"""
    if p:
        return q
    return p

assert et(True,False)==False
assert et(False,False)==False
assert et(True,True)==True
assert et(False,True)==False

def non(p):
    """bool->bool
    return la negation de p"""
    if p:
        return False
    return True

assert non(False)==True
assert non(True)==False

#Q2
#ou(3==3, 5//0 == 2)
#erreur division par 0, le programme ne peut pas interpreter la fonction ou

#(3==3) or (5//0==2)
#(3==3) est vraie ,(5//0==2) est une erreur,
#on utilise ou,la premiere proposition est vrai donc renvoie True


#et(3def volume_tetraedre(a,b,c,d,e,f):
#    """ Number^6-> float
#    calcule le volume du tetraedre
#   a,b,c,d,e,f >= 0"""
    #x:float
#     x=a**2+b**2-a**2
    #y:float
#     y=b**2+c**2-e**2
    #z:float
#     z=a**2+c**2-f**2
    #p:float
#     p= 4*a**2*b**2*c**2
    #q:float
#     q=a**2*x**2+b**2*z**2+c**2*y**2
    #r:float
#     r=x*y*z
#     return 1/12*math.sqrt(p-q+r)def volume_tetraedre(a,b,c,d,e,f):
#     """ Number^6-> float
#     calcule le volume du tetraedre
#     a,b,c,d,e,f >= 0"""
    #x:float
#    x=a**2+b**2-a**2
    #y:float
#    y=b**2+c**2-e**2
    #z:float
#    z=a**2+c**2-f**2
    #p:float
#    p= 4*a**2*b**2*c**2
    #q:float
 #   q=a**2*x**2+b**2*z**2+c**2*y**2
    #r:float
 #   r=x*y*z
  #  return 1/12*math.sqrt(p-q+r)


#(3==4) and (5//0==2)
#3==4 est faux,(5//0==2) est une erreur,
#on utilise et, la premiere proposition est fausse donc renvoie False










