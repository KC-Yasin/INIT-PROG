def qualif_Jo(temps, nb_course_gagner, champion, genre):
    """

    Args:
        temps (float): record personnel au 100m
        nb_course_gagner (int): nb de course gagner 
        champion (bool): si l'athlète est champion du monde
        genre (str): sexe de l'athlète

    Returns:
        bool: True si l'athlète est qualifié aux Jo
    """
    res = False
    if genre == 'Homme':
       if (temps <= 12.0 and nb_course_gagner >= 3) or champion:
            res = True
    elif genre == 'Femme':
        if (temps <= 15.0 and nb_course_gagner >= 3) or champion:
            res = True

    return res





def test_qualif_JO():
    assert qualif_Jo(18.67, 7, False, 'Femme') == False
    assert qualif_Jo(10.6, 4, False, 'Homme') == True
    assert qualif_Jo(11.5, 4, True, 'Homme') == True
    assert qualif_Jo(14.0, 2, False, 'Femme') == False
