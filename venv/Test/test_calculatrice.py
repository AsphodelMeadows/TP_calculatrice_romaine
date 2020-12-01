from Calculatrice.calculatrice import *

def test_lettres_romaines_en_chiffres():
    assert lettres_en_chiffres('') == 0
    assert lettres_en_chiffres('I') == 1
    assert lettres_en_chiffres('V') == 5
    assert lettres_en_chiffres('X') == 10
    assert lettres_en_chiffres('L') == 50
    assert lettres_en_chiffres('C') == 100
    assert lettres_en_chiffres('D') == 500
    assert lettres_en_chiffres('M') == 1000

def test_lettres_romaines_double():
    assert lettres_en_chiffres('') == 0
    assert lettres_en_chiffres('II') == 2
    assert lettres_en_chiffres('VV') == 10
    assert lettres_en_chiffres('XX') == 20
    assert lettres_en_chiffres('LL') == 100
    assert lettres_en_chiffres('CC') == 200
    assert lettres_en_chiffres('DD') == 1000
    assert lettres_en_chiffres('MM') == 2000

def test_conversion():
    assert lettres_en_chiffres("IV") == 4
    assert lettres_en_chiffres("MMVI") == 2006
    assert lettres_en_chiffres("MCMXLIV") == 1944

def test_sum():
    assert sum('III', 'MCMXLIV') == 1947
    assert sum('XIX', 'IX') == 28
    assert sum('I', '') == 1

def test_sub():
    assert sub('III', 'III') == 0
    assert sub('X', 'IX') == 1
    assert sub('X', 'XI') == -1
    assert sub('V', '') == 5

def test_mult():
    assert mult('X', 'X') == 100
    assert mult('X', 'V') == 50
    assert mult('I', '') == 0

def test_div():
    assert div('X', 'X') == 1
    assert div('I', '') == "erreur"
    assert div('', 'I') == 0
    assert div('X', 'II') == 5
    assert div('V', 'III') == 1.6666666666666667

def test_calculatrice():
    assert calculatrice_romaine('+', 'III', 'MCMXLIV') == 1947
    assert calculatrice_romaine('-', 'III', 'III') == 0
    assert calculatrice_romaine('*', 'X', 'V') == 50
    assert calculatrice_romaine('/', 'X', 'II') == 5

def test_chiffres_arabes_vers_chiffres_romains():
    assert chiffres_arabes_en_chiffres_romains('+', 'III', 'I') == 'IV'
    assert chiffres_arabes_en_chiffres_romains('+', 'III', 'MCMXLIV') == 'MCMXLVII'
    assert chiffres_arabes_en_chiffres_romains('-', 'III', 'I') == 'II'
    assert chiffres_arabes_en_chiffres_romains('*', 'X', 'V') == 'L'
    assert chiffres_arabes_en_chiffres_romains('/', 'X', 'X') == 'I'