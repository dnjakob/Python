import json

def jsonReader(inputFile):
    with open(inputFile, "r") as eingabeDatei:
        auszugebendeDatei = json.load(eingabeDatei)

    for eintrag in auszugebendeDatei:
        print("Name:", eintrag['name'], "|", "Hersteller:", eintrag['hersteller'])