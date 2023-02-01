import math

capital1 = float(input("Entrer le capital"))
duree1 = float(input("Entrer la durée"))
taux_ann1 = float(input("Entrer le taux annuel"))/100


def mensualite(c, d, t):
    return (c*t/12) / (1-(1+(t/12))**(-d))


def emprunt(capital, duree, taux):
    result = []
    paye = 0
    m = mensualite(capital, duree, taux)
    interets = 0
    while int(capital) > 0:
        paye += m
        interets += capital * taux / 12
        nouveau_capital = max(capital - m + capital * taux / 12, 0)
        result.append([round(nouveau_capital, 2), round(interets, 2), round(capital * taux / 12, 2)])
        capital = nouveau_capital
    return result


print(emprunt(capital1, duree1, taux_ann1))
