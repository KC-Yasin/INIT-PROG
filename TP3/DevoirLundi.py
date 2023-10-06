def moyenne_valeurImpair(nb_list):
    """calcule la moyenne des valeurs impaires d'une liste de nombres

    Args:
        nb_list (int): liste de nombres qu'on vas lui fournire
    
    Returns
        (float): la moyenne des valeurs impaires de la liste
    """
    n= len(nb_list)
    somme_impair=0
    cpt_impair=0
    for i in range(n):
        if nb_list[i] % 2 !=0:
            somme_impair += nb_list[i]
            cpt_impair +=1
    if cpt_impair==0:
        res=0
    else:
        res=somme_impair/cpt_impair
    return res
moyenne_valeurImpair([1.5, 4.8, 7.8, 15.3, 9.6])

def test_moyenne_valeurImpair(nb_list):
    assert moyenne_valeurImpair([15, 16, 17, -20, 72, 62])==16.0
    assert moyenne_valeurImpair([16, 14, 8, 2, 24, 28])== 0
    assert moyenne_valeurImpair([])==0
    assert moyenne_valeurImpair([3])==3.0
    #assert moyenne_valeurImpair([1.5, 4.8, 7.8, 15.3, 9.6])==7.8 j'ai essayer avec des nombres decimaux mais enfaite je vient de comprendre que le % ne fonctionne que avec des nombres entier