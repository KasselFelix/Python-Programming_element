#Exercice 2.3

    #Question 1:

def mention1(note):
    """
    Number -> String
    hypothèse : la note ne peut être négative ou supérieure à 20.

    Retourne la mention en fonction de la note entrée.
    """

    if note<10:
        return "Eliminé"
    elif note<12:
        return "Passable"
    elif note<14:
        return "AB"
    elif note<16:
        return "B"
    else:
        return "TB"

#Jeu de test:
    assert mention1(10)=="Passable"
    assert mention1(15.5)=="B"
    assert mention1(7)=="Eliminé"

    #Question 2

def mention2(note):
    """
    Number -> String
    hypothèse : la note ne peut être négative ou supérieure à 20.

    Retourne la mention en fonction de la note entrée.
    """

    if 10<note<12:
        return "Passable"
    elif note<10:
        return "Eliminé"
    elif note<14:
        return "AB"
    elif note<16:
        return "B"
    else:
        return "TB"

#Jeu de test:
    assert mention2(10)=="Passable"
    assert mention2(15.5)=="B"
    assert mention2(7)=="Eliminé"

#Exercice 2.7

def sablier(c,h,l):
    """
    Number**3 -> NoneType
    Dessine un sablier en fonction de son centre, sa hauteur et sa largeur.
    """
    
    #A = (c-l,c+h)
    #B = (c+l,c+h)
    #D = (c-l,c-h)
    #E = (c+l,c-h)
    #C = (c,c)

    T1 = fill_triangle(c,c,c-l,c+h,c+l,c+h)
    T2 = fill_triangle(c,c,c+l,c-h,c-l,c-h)

    return overlay(T1,T2)


#Exercice 2.8

#Question 1:

## def tour(l,h,b):
    # """
    #number**3 -> NoneType
    #dessine une tour de hauteur H et de base b, qui corespond a la largeur du rectangle du bas.
    #"""


#Question 2:
def rectangle(x,y,l,h):
    """
    Number**4 -> Image
    Dessine un rectangle en fonction de son point inferieur gauche, sa hauteur et sa largeur. Grace a deux triangle.
    """

    
    #A = (x,y)
    #B = (x,y+l)
    #C = (x+h,y)
    #D = (x+h,y+l)
    
    T1 = fill_triangle(x,y,x,y+l,x+h,y)
    T2 = fill_triangle(x,y+l,x+h,y,x+h,y+l)

    return overlay(T1,T2)


def tour(x,y,h,l,b):
    """
    Number**5->Image
    hypothese b < l
    Dessine une tour à partir de deux rectangles pleins
    """

    R1 = rectangle(x,y,l,h)
    R2 = rectangle((x+b),(y+(h/2)),h,b)

    return overlay (R1,R2)

