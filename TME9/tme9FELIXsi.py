def diff_sym(E1,E2):
    """set[alpha]^2->set[alpha] """

    #res : set[alpha]
    res=set()
    #e : alpha
    for e in E1:
        if e not in E2:
            res.add(e)
    #i : alpha
    for i in E2:
        if i not in E1:
            res.add(i)

    return res    

assert diff_sym({2, 5, 9}, {2, 5, 8, 9})=={8}        
assert diff_sym({'a', 'b', 'c'}, {'a', 'b', 'c'})==set()

def diff_sym(E1,E2):
    """set[alpha]^2->set[alpha]"""
    return (E1-E2)|(E2-E1)


#exercice 9.5

def est_lettre(c):
    """ str -> bool
    Hypothèse : len(c) == 1
    (caractère)
    Retourne True si le caractère c est une lettre, ou False sinon."""

    return ((c >= 'a') and (c <= 'z')) \
        or ((c >= 'A') and (c <= 'Z')) \
        or (c in {'é', 'è', 'à', 'ù', 'œ'})

def frequences_lettres(s):
    """str->dict[str:int]
    retourne les fréquences des lettres de s
    sous la forme d’un dictionnaire de type dict[str:int]"""
    #res : dict[str:int]
    res=dict()
    #c : str
    for c in s:
        if est_lettre(c):
            if c in res:
                res[c]=res[c]+1
            else:
                res[c]=1
    return res
assert frequences_lettres('alea jacta est')=={'s': 1, 'l': 1, 'a': 4, 'c': 1, 'e': 2, 't': 2, 'j': 1}

def lettre_freq_max(s):
    """str-> str
    retourne la lettre de fréquence maximale dans un
    dictionnaire Freqs de fréquences"""
    #Freqs : dict[str:int]
    Freqs=frequences_lettres(s)
    #maj : int
    maj=-1
    #fmax : str
    fmax=''
    #e : str
    for e in Freqs:
        if Freqs[e]>maj:
            maj=Freqs[e]
            fmax=e
    return fmax             
    


    
