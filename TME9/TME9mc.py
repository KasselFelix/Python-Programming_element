#Exercice 9.4:

Dessert = {
'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'},
'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'},
'crepes' : {'oeuf', 'farine', 'lait'},
'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'},
'kouign amann' : {'farine', 'beurre', 'sucre'}
}

    #Question 1:

def nb_ingredients(D,r):
    """
    Recette * str-> int
    retourne l enombre d'ingredients necessaire a la recette r contenu dans D
    """

    
    for (i,j) in D.items():
        if i==r:
            return len(j)

    return None

#Jeu de test:
assert nb_ingredients(Dessert,'crepes')==3
assert nb_ingredients(Dessert,'gateau chocolat')==5


    #Question 2:

def recette_avec(D,i):
    """
    Recette * str-> set(str)
    retourne l'ensemble des recettes qui utilise l'ingredient i.
    """

    #E:set(str)
    E=set()

   
    for (k,l) in D.items():
        if i in l:
            E.add(k)
    return E

    #Question 3:

def tous_ingredients(D):
    """
    Dict[str:set(str)] -> set(str)
    Retourne tous les ingredients contenu dans D
    """
    #E:set(str)
    E=set()
    for (i,j) in D.items():
        for k in j:
            E.add(k)
    return E

    #Question 4:

def table_ingredients(D):
    """
    Dict[str:set(str)] -> Dict[str:set(str)]
    Retourne le dictionnaire contenant tous les ingredients et leurs recette associé.
    """

    #R:Dict[str:set(str)]
    R=dict()

    #E:set(str)
    E=tous_ingredients(D)

    for i in E:
        R[i]=recette_avec(D,i)
        
    return R

    #Question 5:

def ingredient_principal(D):
    """
    Dict[str:set(str)] -> str
    renvoie le nom de l’ingrédient utilisé par le plus grand nombre de recettes.
    """

    #temp:int
    temp=0

    for (i,j) in table_ingredients(D).items():
        temp=max(temp,len(j))

    for (i,j) in table_ingredients(D).items():
        if len(j)==temp:
            return i

    return None

def recettes_sans(D,r):
    """
    Dict[str:set(str)] * str-> Dict[str:set(str)]
    renvoie un nouveau livre de recettes ne contenant que des recettes de D
n’utilisant pas l’ingrédient i.
    """

    #E:Dict[str:set(str)]
    E=dict()

    for (k,l) in D.items():
        if not r in l:
            E[k]=l
            
    return E
    


    
    
    
