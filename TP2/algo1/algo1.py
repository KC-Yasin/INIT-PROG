def algo1(a, b, c, d):
    """

    Args:
        a (int): premier entrer nombre
        b (int): deuxieme entrer nombre
        c (int): troisieme entrer nombre
        d (int): quatrieme entrer nombre

    Returns:
        int: affiche le plus petit nombre des quatres
    """
    if a < b:
        res = a
    else:
        res = b
    if c < res:
        res = c
    if d < res:
        res = d
    return res

def test_algo1():
    assert algo1(16, 6, 3, 7)== 3 
    assert algo1(8, 4, 7, 1) ==1 