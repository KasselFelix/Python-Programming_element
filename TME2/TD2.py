import turtle
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

#Exercice 2.4

    #Question 1:

def f1(n1,n2,n3):
    """
    Number*Number*Number->str

    Retourne un cas parmi 6 selon les valeurs de n1, n2 et n3.
    """

    if n1<n2 and n2<n3:
        return 'cas 1'
    elif n1<n3 and n3<n2:
        return 'cas 2'
    elif n2<n1 and n1<n3:
        return 'cas 3'
    elif n2<n3 and n3<n1:
        return 'cas 4'
    elif n3<n1 and n1<n2:
        return 'cas 5'
    else:
        return 'cas 6'

#Jeu de test:
    assert f(1,2,3)=='cas 1'
    assert f(1,3,2)=='cas 2'
    assert f(3,2,4)=='cas 3'
    assert f(4,2,3)=='cas 4'
    assert f(1,2,-1)=='cas 5'
    assert f(0,0,0)=='cas 6'

    #Question 2:

def f2(n1,n2,n3):
    """
    Number*Number*Number->str

    Retourne un cas parmi 6 selon les valeurs de n1, n2 et n3.
    """

    if n1<n2<n3:
        return 'cas 1'
    elif n1<n3<n2:
        return 'cas 2'
    elif n2<n1<n3:
        return 'cas 3'
    elif n2<n3<n1:
        return 'cas 4'
    elif n3<n1<n2:
        return 'cas 5'
    else:
        return 'cas 6'

#Jeu de test:
    assert f2(1,2,3)=='cas 1'
    assert f2(1,3,2)=='cas 2'
    assert f2(3,2,4)=='cas 3'
    assert f2(4,2,3)=='cas 4'
    assert f2(1,2,-1)=='cas 5'
    assert f2(0,0,0)=='cas 6'

#Exercice 2.7

    #Question1:

def trait(x1,y1,x2,y2):
    """
    Number ^ 4 -> NoneType
    dessine le segment de droite entre les points (x1,y1) et (x2,y2)
    """

    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()

    turtle.goto(x2,y2)
    turtle.up()

def tangram():
    """
    Dessine les pièces du jeu de Tangram de côté 100 et de centre (0,0).
    """

    trait(0,0,50,50)
    trait(50,50,-50,50)
    trait(-50,50,0,0)
    trait(0,0,-50,-50)
    trait(-50,-50,-50,50)
    turtle.goto(50,50)
    trait(50,50,50,-50)
    trait(50,-50,-50,-50)
    turtle.goto(0,0)
    trait(0,0,25,-25)
    trait(25,-25,-25,-25)
    turtle.goto(0,-50)
    trait(0,-50,50,0)
    trait(50,0,25,25)

#Exercice 2.8

    #Question 1-2:

def sablier(centre, hauteur,largeur):
    """
    Number**3 -> NoneType
    Dessine un sablier en fonction de son centre, sa hauteur et sa largeur.
    """

    turtle.down()
    turtle.begin_fill()
    turtle.goto(largeur/2,centre + hauteur/2)
    turtle.goto(-largeur/2,centre + hauteur/2)
    turtle.up()
    turtle.end_fill()
    turtle.goto(-largeur/2,-(centre + hauteur/2))
    turtle.down()
    turtle.begin_fill()
    turtle.goto(largeur/2,-(centre + hauteur/2))
    turtle.goto(-largeur/2,centre + hauteur/2)
    turtle.goto(largeur/2,centre + hauteur/2)
    turtle.goto(-largeur/2,-(centre + hauteur/2))
    turtle.end_fill()
    turtle.up()

#Exercice 2.9

def rectangle(hauteur,largeur):
    """
    Number**2-> NoneType
    Hypothèse : la largeur est inférieure ou égale à la hauteur.
    Dessine un rectangle plein en fonction de sa largeur et de sa longueur.
    """

    turtle.down()
    turtle.begin_fill()
    turtle.goto(largeur,0)
    trait(largeur,0,largeur,hauteur)
    trait(largeur,hauteur,0,hauteur)
    trait(0,hauteur,0,0)
    turtle.end_fill()
    turtle.up()

def tour(hauteur1,largeur1,hauteur2,largeur2):
    """
    Number**4->Nonetype
    Hypothèse: La largeur du deuxième rectangle doit être inférieure à cell
e du premier.
    Dessine une tour à partir de deux rectangles plains
    """

    rectangle(hauteur1,largeur1)
    turtle.goto((largeur1/2)-(largeur2/2),hauteur1)
    rectangle(hauteur2,largeur2)
