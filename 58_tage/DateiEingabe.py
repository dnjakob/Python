import json

class DateiEingabe:

    def benutzerEingabe():

        benutzerDaten = []

        name = input("Geben Sie einen Namen ein: ")
        alter = input("Geben Sie ein Alter ein: ")

        benutzerEingabeDaten = {
            "name": name,
            "alter": alter
        }

        benutzerDaten.append(benutzerEingabeDaten)

        with open("daten.json", "w") as datei:
            json.dump(benutzerDaten, datei, indent=2)

DateiEingabe.benutzerEingabe()