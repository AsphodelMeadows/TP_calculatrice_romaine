def lettres_en_chiffres(lettre):
    if lettre == '':
        return 0
    elif lettre == 'I':
        return 1
    elif lettre == 'V':
        return 5
    elif lettre == 'X':
        return 10
    elif lettre == 'L':
        return 50
    elif lettre == 'C':
        return 100
    elif lettre == 'D':
        return 500
    elif lettre == 'M':
        return 1000
    else:
        conversion = 0
        for compteur in range(0, len(lettre)):
            if check_nombre_precedent_est_plus_petit(lettre, compteur):
                conversion = conversion - 2 * lettres_en_chiffres(lettre[compteur - 1])
                conversion = conversion + lettres_en_chiffres(lettre[compteur])
            else:
                conversion = conversion + lettres_en_chiffres(lettre[compteur])
        return conversion

def check_nombre_precedent_est_plus_petit(lettre, compteur):
    if lettres_en_chiffres(lettre[compteur - 1]) < lettres_en_chiffres(lettre[compteur]) and compteur != 0:
        return True
    return False

def sum(premier_chiffre, second_chiffre):
    return lettres_en_chiffres(premier_chiffre) + lettres_en_chiffres(second_chiffre)

def sub(premier_chiffre, second_chiffre):
    return lettres_en_chiffres(premier_chiffre) - lettres_en_chiffres(second_chiffre)

def mult(premier_chiffre, second_chiffre):
    return lettres_en_chiffres(premier_chiffre) * lettres_en_chiffres(second_chiffre)

def div(premier_chiffre, second_chiffre):
    if lettres_en_chiffres(second_chiffre) == 0:
        print("Division par zéro impossible")
        return "erreur"
    return lettres_en_chiffres(premier_chiffre) / lettres_en_chiffres(second_chiffre)

def calculatrice_romaine(operateur, premier_chiffre, second_chiffre):
    if operateur == '+':
        return sum(premier_chiffre, second_chiffre)
    elif operateur == '-':
        return sub(premier_chiffre, second_chiffre)
    elif operateur == '*':
        return mult(premier_chiffre, second_chiffre)
    elif operateur == '/':
        return div(premier_chiffre, second_chiffre)

def chiffres_arabes_en_chiffres_romains(operateur, premier_chiffre, second_chiffre):
    resultat = calculatrice_romaine(operateur, premier_chiffre, second_chiffre)
    liste_conversion = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
    conv=""
    for num in liste_conversion:
        while resultat >= num[0]:
            resultat -= num[0]
            conv += num[1]
    return conv