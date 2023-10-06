def moyenne_nb_negatif(list_nb):

    total_negatif=0
    somme_negatif=0
    res= 0
    for nombre in list_nb:
        if nombre < 0:
            somme_negatif += nombre
            total_negatif += 1
    
    if total_negatif == 0:
        res = 0
    else:
        res += somme_negatif / total_negatif

    return res
            
moyenne_nb_negatif([0, -0,])

def test_moyenne_nb_negatif():
    assert moyenne_nb_negatif([7, 10, 5 ,9 ,13 ,1]) == 0
    assert moyenne_nb_negatif([-12, 5, 30, -6, -2, 5]) == -6.66
    assert moyenne_nb_negatif([-12, -50, -35, -46, -81]) == -44.8
    assert moyenne_nb_negatif([]) == 0
    assert moyenne_nb_negatif([0, -0,]) == 0
