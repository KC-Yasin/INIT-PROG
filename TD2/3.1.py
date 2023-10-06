def nb_syllabes(mot):
    """repere le nombre de syllabes dans un mot
    
    Args:
       mot (str): entrer du mot 

    returns:
        int: nombre de syllabes
    """
    cpt_voyelle = 0
    cpt_consonne = 0
    for lettre in mot:
        if lettre in 'aeiouy':
            cpt_voyelle += 1
        else:
            cpt_consonne += 1
