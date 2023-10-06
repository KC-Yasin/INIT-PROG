def algo2(m):
    """

    Args:
        m (str): mot en miniscule


    Returns: 
       bool: True si le mot contient plus de voyelle et False sinon
    """
    
    res = 0
    for lettre in m:
        if lettre in 'aeiouy':
            res = res + 1
        else:
            res = res - 1
    return res > 0


def test_algo2():
    assert algo2('bonjour') == False # indique que l'appel sante(1.80) doit retourner "normal"
    assert algo2('informatique') == False # indique que l'appel sante(1.67) doit retourner "surpoids"
