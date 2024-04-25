import json

class JsonReader:

    def jsonAusgeben(inputDatei):
        try:
            with open(inputDatei, "r") as datei:
                daten = json.load(datei)
                print(daten)

        except FileNotFoundError:
            print("Die Datei wurde nicht gefunden")
