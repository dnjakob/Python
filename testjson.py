import json

class Daten:

    def __init__(self):
        self.listen = []

    def eintragen(self):
        name = input("Bitte geben Sie einen Namen ein: ")
        beruf = input("Bitte geben Sie einen Beruf ein: ")
        mail = input("Bitte geben Sie eine Mail-Adresse ein: ")

        liste = {
            "name": name,
            "beruf": beruf,
            "mail": mail
        }

        self.listen.append(liste)
        Aufruf.weitereEingabe()

    def weitereEingabe(self):
        self.frage = input("Wollen Sie neue Werte eintragen? (Y/N): ").capitalize()
        if self.frage == "Y":
            Aufruf.eintragen()
        elif self.frage == "N":
            print("Keine weitere Eingabe!")
            self.array = json.dumps(self.listen, ensure_ascii=False)
            Aufruf.ausgebenAbfrage()
        elif self.frage != "Y" or self.frage != "N":
            print("Bitte gültige Eingabe tätigen! Bitte erneut tätigen!")
            Aufruf.weitereEingabe()

    def ausgebenAbfrage(self):
        self.ausgabe = input("Wollen Sie die Werte hier ausgeben? (Y/N): ").capitalize()
        if self.ausgabe == "Y":
            self.ergebnis = json.loads(self.array)
            Aufruf.tatsaechlicheAusgabe()
        elif self.ausgabe == "N":
            print("Keine Ausgabe!")
        elif self.ausgabe != "Y" or self.frage != "N":
            print("Bitte gültigen Wert eintragen! Bitte erneut tätigen!")
            Aufruf.ausgebenAbfrage()

    def tatsaechlicheAusgabe(self):
        self.pruefung = input("Welcher Index? Hinweis - Es beginnt bei 0 | ")
        if self.pruefung.isnumeric() == True:
            try:
                print(self.ergebnis[int(self.pruefung)])
            except:
                print("Der Index ist nicht belegt! Bitte einen gültigen Index nennen!")
                Aufruf.tatsaechlicheAusgabe()
            else:
                Aufruf.abfrageNeueAusgabe()
        elif self.pruefung.isnumeric() == False:
            print("Kein gültiger Index! Bitte erneut tätigen!")
            Aufruf.tatsaechlicheAusgabe()
    
    def abfrageNeueAusgabe(self):
        self.erneutepruefung = input("Wollen Sie noch einen Wert ausgeben? (Y/N): ").capitalize()
        if self.erneutepruefung == "Y":
            Aufruf.tatsaechlicheAusgabe()
        elif self.erneutepruefung == "N":
            print("Vielen Dank für die Verwendung des Skriptes!")
        elif self.erneutepruefung != "Y" and self.erneutepruefung != "N":
            print("Ungültige Eingabe! Bitte erneut tätigen!")
            Aufruf.abfrageNeueAusgabe()

Aufruf = Daten()
Aufruf.eintragen()