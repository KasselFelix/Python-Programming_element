#exercice 10.2

#Q1

def diff_sym(E1,E2):
    """set[alpha]^2->set[alpha]
    construit la différence symétrique entre deux ensembles E1 et E2."""

    return {e for e in E1|E2 if not((e  in E1) and (e in E2))}

assert diff_sym({2, 5, 9}, {3, 5, 8})=={2, 3, 8, 9}
assert diff_sym({'a', 'b', 'c'}, {'d', 'e', 'f'})=={'a', 'b', 'c', 'd', 'e', 'f'}



#Q2

#BasePrix : dict[str:float]
BasePrix={'Sabre Laser': 229.0,
           'Mitendo DX': 127.30,
           'Coussin Linux': 74.50,
           'Slip Goldorak': 29.90,
           'Station Nextpresso': 184.60}

def fourchette_prix(mini,maxi,Prix):
    """float^2*dict[str:float]->set[str]
    retourne l’ensemble des noms de produits disponibles
    dans cette fourchette de prix."""

    return {k for k,v in Prix.items() if v<=maxi and v>=mini}

assert fourchette_prix(50.0, 200.0,BasePrix)=={'Mitendo DX', 'Station Nextpresso', 'Coussin Linux'}


#Q3

# Dessert : dict[str :set[str]]
Dessert = {
        'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'},
        'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'},
        'crepes' : {'oeuf', 'farine', 'lait'},
        'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'},
        'kouign amann' : {'farine', 'beurre', 'sucre'}}

        
def recette_avec(D,i):
    """dict[str :set[str]]*str->set[str]
    étant donnés un livre de recettes D et le nom d’un ingrédient i,
    renvoie l’ensemble des recettes qui utilisent cet ingrédient."""
    
    #recette : str
    return {recette for recette in D if i in D[recette]}    

assert recette_avec(Dessert, 'beurre')=={'quatre-quarts', 'kouign amann', 'gateau chocolat'}

def tous_ingredients(D):
    """dict[str :set[str]]->set[str]
    renvoie l’ensemble de tous les ingrédients apparaissant au moins une fois dans une recette de D."""
    
    return  {i for recette in D for i in D[recette] } 

assert tous_ingredients(Dessert)=={'lait', 'yaourt', 'chocolat', 'sucre', 'oeuf', 'beurre', 'farine'}

def table_ingredients(D):
    """dict[str :set[str]]->dict[str:set[str]]
    renvoie la table des ingrédients associée."""
    
    return {i:recette_avec(D,i) for i in tous_ingredients(D)}

assert table_ingredients(Dessert)=={'oeuf': {'gateau yaourt', 'gateau chocolat', 'crepes', 'quatre-quarts'},
                                    'chocolat': {'gateau chocolat'},
                                    'farine': {'kouign amann', 'gateau yaourt', 'gateau chocolat', 'crepes', 'quatre-quarts'},
                                    'lait': {'crepes'}, 'beurre': {'kouign amann', 'gateau chocolat', 'quatre-quarts'},
                                    'sucre': {'kouign amann', 'gateau yaourt', 'gateau chocolat', 'quatre-quarts'},
                                    'yaourt': {'gateau yaourt'}}

def recettes_sans(D,i):
    """dict[str :set[str]]->dict[str :set[str]]
    renvoie un nouveau livre de recettes ne contenant que des recettes de D
    n’utilisant pas l’ingrédient i."""
  
    return {recette:D[recette] for recette in D if recette not in table_ingredients(D)[i]}

assert recettes_sans(Dessert,'farine')=={} 
assert recettes_sans(Dessert,'oeuf')=={'kouign amann': {'farine', 'beurre', 'sucre'}}
assert recettes_sans(Dessert,'beurre')=={'gateau yaourt': {'oeuf', 'farine', 'yaourt', 'sucre'},
                                         'crepes': {'farine', 'lait', 'oeuf'}}

#Q5


