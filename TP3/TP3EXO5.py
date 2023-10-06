def somme_npremier(nombre_entre):
    """calcule la somme des n premiers entiers

    Args:
        list_nb (int): entier max
    
    Returns:
        (int): renvoie la somme des n premiers entier
    """    
    res =0
    for nombre in range(1, nombre_entre+1):
            res += nombre
    return res

        
somme_npremier(0)





def test_somme_npremier():
    assert somme_npremier(4)== 10
    assert somme_npremier(5)== 15
    assert somme_npremier(0)== 0



def suite_syracuse(Uentre, Terme):
    """va calculer le terme entrer 

    Args:
        Uentre (int): entrer du terme 
    """    
    Uentre1=Uentre
    for nombre in range(1, Terme+1):
        if Uentre1%2== 0:
             Uentre1= Uentre1/2
        else:
             Uentre1= 1+Uentre1*3
    return Uentre1

suite_syracuse(6, 153)

def test_suite_syracuse():
     assert suite_syracuse(1, 4)==4
     assert suite_syracuse(6, 3)==5