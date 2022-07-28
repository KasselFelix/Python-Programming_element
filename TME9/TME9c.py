#Exercice 9.1:

    #Question 1:

def diff_sym(e1,e2):
    """
    set(alpha)*set(alpha) -> set(alpha)
    Construit la difference symetrique entre deux ensembles E1 et E2.
    """

    #e3:set(alpha)
    e3=set()

    for i in e1:
        for j in e2:
            e3.add(i)
            e3.add(j)
    
    return e3

    #Question 2:

def diff_sym2(e1,e2):
    """
    set(alpha)*set(alpha) -> set(alpha)
    Construit la difference symetrique entre deux ensembles E1 et E2.
    """

    return (e1|e2) - (e1&e2)


 #Exercice 2:

    #Question 1:

def repetes(L):
    """
    list [alpha] -> set(alpha)
    retourne les element repete d'une liste L.
    """

    K=set()

    for i in L:
        if L.count(i)>1:
            K.add(i)
    return K

##def repetes(L):
##    """
##    list [alpha] -> set(alpha)
##    retourne les element repete d'une liste L
##    """
##
##    K=set()
##    j=0
##    cpt=0
##
##    while j < len(L):
##        for i in L:
##            if L[j]==i:
##                cpt=cpt+1
##            if cpt>2:
##                K.add(L[j])
##                cpt=0
##            j=j+1
##            
##    return K

#Jeu de test:
assert repetes([1, 2, 23, 9, 2, 23, 6, 2, 9])=={2, 9, 23}
assert repetes([1, 2, 3, 4])== set()
assert repetes(['bonjour', 'ça', 'ça', 'va', '?'])=={'ça'}

    #Question 2:

def sans_repetes(L):
    """
    List[alpha] -> List[alpha]
    retourne les element sans les repete d'une liste L.
    """

    #D:Dict[alpha:int]
    D=dict()
    #R:List[alpha]
    R=[]

    for i in L:
        if i in D:
            D[i]=D[i]+1
        else:
            D[i]=1
            R.append(i)

    return R

#Jeu de test:
assert sans_repetes([1,2,23,9,2,23,6,2,9])==[1,2,23,9,6]
assert sans_repetes([1,2,3,4])==[1,2,3,4]
assert sans_repetes(['bonjour', 'ça', 'ça', 'va', '?'])== ['bonjour', 'ça','va', '?']

    #Question 3:

def uniques(L):
    """
    list [alpha] -> set(alpha)
    retourne les elements qui apparaissent qu'une seul fois d'une liste L.
    """

    K=set()

    for i in L:
        if L.count(i)==1:
            K.add(i)
    return K

#Jeu de test:
assert uniques([1,2,23,9,2,23,6,2,1])=={6,9}
assert uniques([1,2,1,1])=={2}
assert uniques([1,2,1,2,1])==set()

    #Question 4:

def frequences(L):
    """
    List[alpha] -> Dict[alpha:int]
    retourne les elements de L et leur nombre d'apparition.
    """

    #D:Dict[alpha:int]
    D=dict()
    
    for i in L:
        if i in D:
            D[i]=D[i]+1
        else:
            D[i]=1

    return D

#Jeu de test:
assert frequences([])=={}
assert frequences([2])=={2: 1}
assert frequences([2, 2, 2])=={2: 3}
assert frequences([1, 2, 23, 9, 2, 23, 6, 2, 9])=={1: 1, 2: 3, 9: 2, 6: 1, 23: 2}

    #Question 5:

def repetes_fois(k,L):
    """
    alpha * List[alpha] -> set(alpha)
    Hypothèse : k>0
    Retourne l'ensemble des elements repete k fois dans L.
    """

    #E:set(alpha)
    E=set()

    #D:Dict[alpha:int]
    D=frequences(L)

    for (i,j) in D.items():
        if j==k:
            E.add(i)

    return E

#Jeu de test:
assert repetes_fois(1, [1, 2, 23, 9, 2, 23, 6, 2, 9])=={1, 6}
assert repetes_fois(2, [1, 2, 23, 9, 2, 23, 6, 2, 9])=={9, 23}
assert repetes_fois(3, [1, 2, 23, 9, 2, 23, 6, 2, 9])=={2}
assert repetes_fois(4, [1, 2, 23, 9, 2, 23, 6, 2, 9])==set()

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

#Exercice 9.6

# Dict_Ang_Fra : dict[str:str]
Dict_Ang_Fra = {'the': 'le', 'cat': 'chat',
'fish' : 'poisson', 'catches': 'attrape'}

# Dict_Fra_Ita : dict[str:str]
Dict_Fra_Ita = {'le': 'il', 'chat': 'gatto',
'poisson' : 'pesce', 'attrape': 'cattura'}

    #Question 1:

def traduction_mot_a_mot(L,D):
    """
    List[str] * Dict[str:str] -> List[str]
    """

    #R:List[str]
    R=[]

    for i in L:
        if i in D:
            R.append(D[i])

    return R

#Jeu de test:
assert traduction_mot_a_mot([],Dict_Ang_Fra)==[]
assert traduction_mot_a_mot(['cat'],Dict_Ang_Fra)==['chat']
assert traduction_mot_a_mot(['the', 'cat', 'catches', 'the', 'fish'],
                            Dict_Ang_Fra)==['le', 'chat', 'attrape', 'le', 'poisson']
assert traduction_mot_a_mot(['le', 'chat', 'attrape', 'le', 'poisson'],
                            Dict_Fra_Ita)==['il', 'gatto', 'cattura', 'il', 'pesce']

    #Question 2:

def dictionnaire_inverse(D):
    """
    Dict[alpha:beta] -> Dict[beta:alpha]
    """

    #I:Dict[beta:alpha]
    I=dict()

    for (i,j) in D.items():
        I[j]=i

    return I

#Jeu de test:
assert dictionnaire_inverse({"cat": "chat"})=={'chat': 'cat'}
assert dictionnaire_inverse(Dict_Ang_Fra)=={'poisson': 'fish', 'le': 'the', 'chat': 'cat', 'attrape': 'catches'}
assert dictionnaire_inverse(Dict_Fra_Ita)=={'pesce': 'poisson', 'il': 'le', 'gatto': 'chat', 'cattura': 'attrape'}

    #Question 3:

def composition_dictionnaires(D1,D2):
    """
    Dict[alpha:beta] * Dict[beta:alpha] -> Dict[beta:alpha]
    Retourne le dictionnaire correspondant a la composition des traductions.
    """
    
    #D3:Dict[alpha:beta]
    D3=dict()

    
    
#Exercice 9.7

    #Question 1:

def valeur_decomposition(D):
    """
    Dict[int:int] -> int
    """

    #s:int
    s=1

    for (i,j) in D.items():
        s=s*(i**j)

    return s

#Jeu de test:
assert valeur_decomposition({2:1, 3:1, 5:1})==30
assert valeur_decomposition({2:3, 7:1})==56
assert valeur_decomposition({2:10})==1024

    #Question 2:

def decomposition(L):
    """
    List[int] -> Dict[int:int]
    """

    #D:Dict[int,int]
    D=dict()

    for i in L:
        if i in D:
            D[i]=D[i]+1
        else:
            D[i]=1

    return D

#Jeu de test:
assert decomposition([2, 3, 5])=={2: 1, 3: 1, 5: 1}
assert decomposition([2, 2, 2, 7])=={2: 3, 7: 1}
assert decomposition([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])=={2: 10}

    #Question 3:

def suppr_liste(n,L):
    """
    int * List[int] -> List[int]
    Retire l'élément n de la liste L.
    """

    #R:List[int]
    R=[]

    for i in L:
        if i!=n:
            R.append(i)

    return R

def eratosthene(n):
    """
    int -> List[int]
    Retourne la liste des entiers premiers inférieurs ou égaux à n.
    """
    
    L = [2]
 
    for i in range(3, n, 2):
        L.append(i)
 
    for i in L:
        for n in L:
            if n % i == 0 and i != n:
                L=suppr_liste(n,L)
 
    return L

def liste_facteurs_premiers(n):
    """
    int -> List[int]
    Hypothèse : n>=2.
    """

    #Prem:List[int]
    Prem=eratosthene(n)

    #L:List[int]
    L=[]

    for i in Prem:
        if n%i==0:
            L.append(i)

    for i in L:
        n=n//i

    return L

def decomposition_facteurs_premiers(n):
    """
    int -> Dict[int:int]
    """

    return decomposition(liste_facteurs_premiers(n))
