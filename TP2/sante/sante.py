def sante(taille, poids):
    """Permet de détecter un pb de santé en fonction de l’imc

Args:
taille (float): la taille de la personne en mètres
poids (int): le poids de la personne en kg

Returns:
    str: le problème éventuellement détecté
"""
    imc = poids/taille**2
    if imc < 16.5:
        res = "famine"
    elif imc < 18.5:
        res = "maigreur"    
    elif imc < 25:
        res = "normal"
    elif imc < 30:
        res ="surpoids"
    else:
        res = "obésité"
    return res

def test_sante():
    assert sante(1.8, 80)== "normal" # indique que l'appel sante(1.80) doit retourner "normal"
    assert sante (1.6, 67) =="surpoids" # indique que l'appel sante(1.67) doit retourner "surpoids"
