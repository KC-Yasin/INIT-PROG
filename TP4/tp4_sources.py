def plus_long_plateau(chaine): #EXERCICE 1
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 1  # longueur du plateau actuel
    n=len(chaine)
    for i in range(1, n):
        if chaine[i] == chaine[i-1]:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    if len(chaine) ==0:
        res = 0
    else:
        res = lg_max
    return res
plus_long_plateau("abeille")

def test_plus_long_plateau():
    assert plus_long_plateau("abeille")== 2
    assert plus_long_plateau("fouuuuu u")== 5
    assert plus_long_plateau("aabbb")== 3
    assert plus_long_plateau('')== 0
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]

 # EXERCICE 2
def ville_peupler(liste_ville, liste_popu):
    """compare et donne la ville la plus peupler

    Args:
        liste_ville (str): liste de ville
        liste_popu (int): liste de population de ville
    Returns:
        str:nom de la ville la plus peuplée
    """ 
    if len(liste_popu) > 0:
        pos_max = 0
        maxi = liste_popu[0]   
        n = len(liste_popu)

        for i in range(n):
            if liste_popu[i] > maxi:
                maxi = liste_popu[i]
                pos_max = i
        return liste_ville[pos_max]



def test_ville_peupler():
    assert ville_peupler(["Berlin", "Rome"], [100000, 1200000])== "Rome"
    assert ville_peupler(liste_villes, population) == "Tours"
    assert ville_peupler([], []) == None


#EXERCICE 3
def carac_en_nb(carac):
    """transforme une chaine de caract en Int

    Args:
        carac (str): _description_
    """   
    res=0
    for i in range(len(carac)):
        if carac[i] in '0123456789':
            if carac[i]=='0':
                nb=0
            elif carac[i]=='1':
                nb=1
            elif carac[i]=='2':
                nb=2
            elif carac[i]=='3':
                nb=3
            elif carac[i]=='4':
                nb=4
            elif carac[i]=='5':
                nb=5
            elif carac[i]=='6':
                nb=6
            elif carac[i]=='7':
                nb=7
            elif carac[i]=='8':
                nb=8
            elif carac[i]=='9':
                nb=9
            res = res*10+nb
    return res

print(carac_en_nb("512"))                


def test_carac_en_nb():
    assert carac_en_nb("512")==512
    assert carac_en_nb("28caliste")==28
    assert carac_en_nb("")== 0


#Exercice 4

def search_word_firstletter(search, list_mot):
    """Permet de retrouver les mots qui commencent par une certaine lettre dans une liste de mots

    Args:
        liste_mot (list): liste de mot qu'on va lui fournire
        search (str): lettre qu'on cherche
    Returns:
        (list): retourne les mots commencant par la lettre
    """    

    list_repsearch=[]
    for i in range(len(list_mot)):
        if list_mot[i][0] == search:
            list_repsearch.append(list_mot[i])
    return list_repsearch
search_word_firstletter("c",["caliste","rekkles","saken","caliste","targamas"])


def test_search_word_firstletter():
    assert search_word_firstletter("h",["salut","hello","hallo","ciao","hola"])== ["hello","hallo","hola"]
    assert search_word_firstletter("c",["caliste","rekkles","saken","cabochard","targamas"])==["caliste","cabochard"]



#Exercice 5
def mot_alphabetique(phrase):
    """Recupere dans la phrase uniquement les chaines de caracteres

    Args:
        phrase (str):phrase qu'on va lui envoyer

    Returns:
        (list): liste de mot qu'on a recuperer
    """    
    phraserep= []
    mot = ""
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            mot += phrase[i]
        elif mot != "": 
            phraserep.append(mot)
            mot=""
    if mot != "":
        phraserep.append(mot)
    return phraserep


def test_mot_alphabetique():
    assert mot_alphabetique("Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!")== ["Cela", "fait", "déjà", "jours", "jours", "à", "l", "IUT", "O", "Cool"]
    assert mot_alphabetique("3630 3630 545454 20")== []


#exercice 6

def fusionn(search, phrase):
    """fonction qui permet de retrouver tous les
mots qui commencent par une certaine lettre dans un texte

    Args:
        phrase (str):phrase qu'on va lui envoyer

    Returns:
        list: _description_
    """    


    return search_word_firstletter(search, mot_alphabetique(phrase))




def test_fusionn():
    assert fusionn('S', "Salut ta vu76 la Souris ?!! elle 21me Souri")== ["Salut", "Souris", "Souri"]
    assert fusionn('P', "184641 Pooooo:!:!:; idi Pi")== ["Pooooo", "Pi"]

print(fusionn('P', "184641 Pooooo:!:!:; idi Pi"))