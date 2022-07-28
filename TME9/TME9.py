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
    Dict[str:set(str)] * str-> int
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
    Dict[str:set(str)] * str-> set(str)
    retourne l'ensemble des recettes qui utilise l'ingredient i.
    """

    #E:set(str)
    E=set()

    for (k,l) in D.items():
        if i in l:
            E.add(k)

    return E

#Jeu de test:
assert recette_avec(Dessert,'beurre')=={'gateau chocolat','kouign amann','quatre-quarts'}
assert recette_avec(Dessert,'lait')=={'crepes'}
assert recette_avec(Dessert,'fraise')==set()

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
    renvoie le nom de l’ingrédient utilisé par le plus grand nombre de recettes
    """

    #temp:int
    temp=0

    for (i,j) in table_ingredients(D).items():
        temp=max(temp,len(j))

    for (i,j) in table_ingredients(D).items():
        if len(j)==temp:
            return i

    return None

#Jeu de test:
assert ingredient_principal(Dessert)=='farine'

    #Question 6:

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

#Jeu de test:
assert recettes_sans(Dessert,'farine')== {}
assert recettes_sans(Dessert,'oeuf')=={'kouign amann':{'beurre','farine','sucre'}}
assert recettes_sans(Dessert,'beurre')=={'gateau yaourt':{'farine','oeuf','sucre','yaourt'},
                                         'crepes' : {'farine', 'lait', 'oeuf'}}

#Exercice 9.5:

def est_lettre(c):
    """
    str -> bool
    Hypothèse : len(c) == 1 (caractère)
    Retourne True si le caractère c est une lettre, ou False sinon.
    """

    return ((c >= 'a') and (c <= 'z')) \
        or ((c >= 'A') and (c <= 'Z')) \
        or (c in {'é', 'è', 'à', 'ù', 'œ'})

    #Question 1:

def frequences_lettres(s):
    """
    str -> Dict[str:int]
    retourne les fréquences des lettres de s sous la forme d’un dictionnaire de type dict[str:int].
    """

    #D:Dict[str:int]
    D=dict()

    for i in s:
        if est_lettre(i):
            if i in D:
                D[i]=D[i]+1
            else:   
                D[i]=1
        
    return D

#Jeu de test:
assert frequences_lettres('alea jacta est')== {'j': 1, 'e': 2, 't': 2, 'c': 1, 'a': 4, 's': 1, 'l': 1}
assert frequences_lettres("l'élève")=={'é': 1, 'e': 1, 'v': 1, 'l': 2, 'è': 1}

    #Question 2:

def lettre_freq_max(s):
    """
    str -> str
    retourne la lettre de fréquence maximale dans un dictionnaire Freqs de fréquences.
    """

    #D:Dict[str:int]
    D=frequences_lettres(s)
    #temp:int
    temp=1

    for (i,j) in D.items():
        if temp<j:
            temp=j

    for (i,j) in D.items():
        if temp==j:
            return i

    return None

#Jeu de test:
assert lettre_freq_max('alea jacta est')=='a'
assert lettre_freq_max("l'élève")=='l'

def chargement_texte(fichier):
    """
    str -> str
    Hypothèse : le fichier est présent sur le disque
    Retourne la chaîne de caractères correspondant au contenu
    du fichier.
    """

    # contenu : str
    contenu = '' # contenu du fichier

    with open(fichier, 'r') as f:
        contenu = f.read()

    return contenu

    #Question 4:

def lettres_freq_inf(Freqs,fseuil):
    """
    Dict[str:int] * int -> set(str)
    """

    #E:set(str)
    E=set()

    for (i,j) in Freqs.items():
        if j<=fseuil:
           E.add(i)

    return E

#Jeu de test:
assert lettres_freq_inf(frequences_lettres('alea jacta est'), 1)=={'c', 'j', 'l', 's'}
assert lettres_freq_inf(frequences_lettres("l'élève"), 2)=={'e', 'l', 'v', 'è', 'é'}

    #Question 5:
##lettre_freq_inf(Freqs,100)

