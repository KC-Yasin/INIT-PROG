# exercice 1 PAIR OU IMPAIRE
def plus_de_pair(list_nb):
    """détérmine si une liste de nombres contient au moins autant de nombre pairs que de nombre impairs

    Args:
        list_nb (int): liste de nombres
    Returns:
        [bool]: True si il y a au moins autant de nombre pairs et False sinon 
    """
    cpt_pair = 0
    cpt_impaire = 0
    # au début de chaque tour de boucle
    for valeur in list_nb:
        if valeur % 2 == 0:
            cpt_pair += 1
        else:
            cpt_impaire += 1
    return cpt_pair >= cpt_impaire
plus_de_pair([1,4,6,-2,-5,3,10])
def test_plus_de_pair():
    assert plus_de_pair([1,4,6,-2,-5,3,10]) == True
    assert plus_de_pair([1,3,7,-2,-5,3,10]) == False
    assert plus_de_pair([1,4,6,3,6,3]) == True
    assert plus_de_pair([]) == True




# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = None
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur
    for elem in liste_nombres:
        if res == None:
            if elem > valeur:
                res = elem
        else:
            if valeur < elem < res:
                res = elem 
    return res
min_sup([-2, -5, 2, 9.8, -8.1, 7], 0)

def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None


# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = ' '
    # au début de chaque tour de boucle
    # c1 vaut
    # c2 vaut
    # resultat vaut
    for c2 in phrase:
        if c1 == ' ' and c2 != ' ': 
            resultat = resultat + 1
        c1 = c2
    return resultat
nb_mots(" ce  test ne  marche pas ")

def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

# exercice 4.1

def somme_des_pairs(list_nb):
    """fait la somme des nombres pairs d'une liste d'entiers

    Args:
        list_nb (int): liste de nombres
    """    
    res = 0
    for nombre in list_nb:
        if nombre % 2 == 0:
            res += nombre
    return res

somme_des_pairs([-10, 5, 6, 3, -2, 2])

def test_somme_des_pairs():
    assert somme_des_pairs([10, 5, 6, 3, 2, 2]) == 20
    assert somme_des_pairs([1, 5, 7, 3, 11, 17]) == 0
    assert somme_des_pairs("") == 0
    assert somme_des_pairs([-10, 5, 6, 3, -2, 2]) == -4


# exercice 4.2

def last_voyelle(mot):
    """retourne la dernière voyelle d'une chaine de caractère

    Args:
        mot (str): mot entree

    returns:
    """

    voyelle= None
    for lettre in mot:
        if lettre in 'aeiouy':
            voyelle= lettre 
    return voyelle


def test_last_voyelle():
    assert last_voyelle("informatique") == 'e'
    assert last_voyelle("ordinateur") == 'u'
    assert last_voyelle("") == None
    assert last_voyelle("Grrrr")== None

# exercice 4.3

def proportion_nb_negatif(list_nb):
    """donne la proportion de nombres strictement négatifs dans une liste

    Args:
        list_nb (int): entree nb

    returns:
    """
    
    nb_negatif = 0
    nb_total = 0
    for nombre in list_nb:
        if nombre < 0:
            nb_negatif += 1
        nb_total += 1
    if nb_total == 0:
        res = 0
    else: 
        res = nb_negatif / nb_total
    return res

proportion_nb_negatif([])

def test_proportion_nb_negatif():
    assert proportion_nb_negatif([4,-2,8,2,-2,-7]) == 0.5


# exercice 5s

def somme_des_n(nb_entre):
    """fait la sommes des n premiers entiers

    Args:
        nb_entre (int): _description_

    returns:
    int: somme des n 
    """

    res = 0
    



    return res
