import math

def linesegment(v1, v2):

    strecke1=pow((v2[0] - v1[0]), 2)
    strecke2=pow((v2[1] - v1[1]), 2)

    ergebnis=math.sqrt(strecke1 + strecke2)
    return round(ergebnis, 2)

AB=[0, 0]
BC=[4, 2]

print("Das Ergebnis lautet",linesegment(AB, BC))