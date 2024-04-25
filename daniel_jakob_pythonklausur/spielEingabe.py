# Klausur Python 3. Semester

# Jakob

# Daniel

"""

Entwickle ein Python-Skript „spielEingabe.py“, das eine Klasse „Eingabe“ verwendet, um Benutzereingaben für die beiden

Attribute „Name“ und „Hersteller“ von Lieblingsspielen zu erfassen. >>> 25 Punkte

Diese Eingaben sollen auf der obersten Root-Ebene des Ordners in einer JSON-Datei gepeichert werden. >>> 25 Punkte

Erstelle nun ein Modul „auswertungJSON.py“, das eine Funktion zum Lesen und Ausgeben der Inhalte der JSON-Datei enthält. >>> 25 Punkte

Verwende schließlich „spielAusgabe.py“, um das Modul zu importieren, die JSON-Datei zu laden und die Daten daraus zu präsentieren. >>> 25 Punkte

Anleitung

Erstelle zuerst die „spielEingabe.py“ und führe diese aus. Hier gibst du Name und Hersteller des Lieblingsspiels ein, welche dann in der Datei „lieblingsspiel.json“ gespeichert werden.

Führe anschließend „spielAusgabe.py“ aus. Dieses Skript verwendet das Modul „auswertungJSON.py“, um die Daten aus „lieblingsspiel.json“ zu lesen und auszugeben.

"""
import json

class Eingabe:
    def __init__(self, name, hersteller):
        self.name = name
        self.hersteller = hersteller

    def konvertiereZuJson(self):

        konvertierendeListe = []

        lieblingsspiel = {
            "name": self.name,
            "hersteller": self.hersteller
        }

        konvertierendeListe.append(lieblingsspiel)

        Eingabe.weitereEingaben(konvertierendeListe)
        

        with open("lieblingsspiel.json", "w") as datei:
            json.dump(konvertierendeListe, datei, indent=2)

    def weitereEingaben(konvertierendeListe):

        schalter = input("Wollen Sie weitere Spiele abspeichern? (Y/N) ")

        while (schalter == "Y"):
            neuerName = input("Geben Sie den Namen des Lieblingsspiels ein: ")
            neuerHersteller = input("Geben Sie den Hersteller des Spiels ein: ")

            neuesLieblingsspiel = {
            "name": neuerName,
            "hersteller": neuerHersteller
        }
            
            konvertierendeListe.append(neuesLieblingsspiel)
            
            schalter = input("Wollen Sie weitere Spiele abspeichern? (Y/N) ")
            if schalter == "N":
                break
            
            
        



benutzereingabe = Eingabe(input("Geben Sie den Namen des Lieblingsspiels ein: "), input("Geben Sie den Hersteller des Spiels ein: "))
benutzereingabe.konvertiereZuJson()