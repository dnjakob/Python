
# 1. PYTHON-KLAUSUR

# Gib zurerst Deinen Namen unten ein und speichere die Datei als "klausur_python_vorname_nachname.py ab". Schreibe die Ergebnisse direkt unterhalb der Aufgaben. Achte auf die Punkteverteilung.

# Name: Daniel Jakob
# =====================================================================================================================

# Aufgabe 1: Iteriere über eine Liste von Obstsorten und gib jedes Element aus. 5 Punkte

obst = ["Apfel", "Birne", "Banane", "Kirsche", "Traube"]

for x in obst:
    print(x)

print("\n")

# Aufgabe 2: Schreibe eine Funktion, die einen Iterator für die Fibonacci-Folge erstellt und gib die ersten 20 Zahlen aus. 10 Punkte


def fibonacci(anzahl):
    zahl1 = 0
    zahl2 = 1

    for x in range(anzahl):
        print(x + 1, "- Fibonacci Zahl: ", zahl1)
        zahl1, zahl2 = zahl2, zahl1 + zahl2


fibonacci(20)

print("\n")

# Aufgabe 3: Gib jeden Buchstaben eines Wortes rückwärts aus. 5 Punkte

wort = "Fibonacci"

for x in reversed(wort):
    print(x)

print("\n")

# Aufgabe 4: Erstelle eine Klasse, die einen Iterator für die Quadrate von Zahlen von 1 bis 10 erstellt. 15 Punkte

zaehler = 1

class Quadrate:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        if self.x <= 10:
            quadrat = self.x * self.x
            self.x += 1
            return quadrat
        else:
            raise StopIteration
        
Quadratklasse = Quadrate()

for x in Quadratklasse:
    print("Das",zaehler,"Quadrat lautet: ",x)
    zaehler += 1

print("\n")

# Aufgabe 5: Schreibe eine Funktion, die nur die geraden Zahlen aus einer Liste ausgibt. 10 Punkte

werte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in werte:
    if x % 2 == 0:
        print(x)

print("\n")

# Aufgabe 6: Erstelle ein Modul namens 'meinmodul' mit einer Funktion 'begruessung', die einen Namen als Parameter nimmt und eine Begrüßung ausgibt. 5 Punkte

# siehe Datei meinmodul_daniel_jakob.py

# Aufgabe 7: Importiere dein Modul 'meinmodul' in dieses Skript und rufe die Funktion 'begruessung' mit deinem Namen auf. 5 Punkte

import meinmodul_daniel_jakob

meinmodul_daniel_jakob.begruessung("Daniel")

print("\n")

# Aufgabe 8: Füge dem Modul 'meinmodul' ein Dictionary 'person1' hinzu mit den Schlüsseln 'name', 'alter', und 'stadt'. 5 Punkte

# siehe Datei meinmodul_daniel_jakob.py

# Aufgabe 9: Importiere das Dictionary 'person1' aus deinem Modul und gib das Alter der Person aus. 5 Punkte

print(meinmodul_daniel_jakob.person1["alter"])

print("\n")

# Aufgabe 10: Erstelle einen Alias 'mm' für dein Modul 'meinmodul' und greife auf die Stadt der 'person1' aus dem Modul zu. 5 Punkte

import meinmodul_daniel_jakob as mm

print(mm.person1["stadt"])

print("\n")

# Aufgabe 11: Erstelle eine Basisklasse mit dem Namen 'Tier' mit den Attributen 'name' und 'fellfarbe' und einer Methode 'futter', die "Ich liebe Knochen" ausgibt. 5 Punkte

class Tier:
    
    def __init__(self, name, fellfarbe):
        self.name = name
        self.fellfarbe = fellfarbe

    def futter(self):
        print("Ich liebe Knochen")

Ausgabe1 = Tier("Paulina", "braun")
Ausgabe1.futter()

print("\n")

# Aufgabe 12: Leite eine Klasse 'Hund' von der Klasse 'Tier' ab und fügen eine Methode 'anzeige' hinzu, die Name und Fellfarbe des Hundes ausgibt. 5 Punkte

class Hund(Tier):

    def anzeige(self):
        print("Der Name des Hundes lautet",self.name,"mit der Fellfarbe",self.fellfarbe)

Ausgabe2 = Hund("Paulina", "braun")
Ausgabe2.anzeige()

print("\n")

# Aufgabe 13: Erstelle ein Objekt der Klasse 'Hund', setze seinen Namen auf 'Fussel' und rufe die Methode 'anzeige' auf. 5 Punkte

Ausgabe3 = Hund("Fussel", "weiß")
Ausgabe3.anzeige()

print("\n")

# Aufgabe 14: Rufe die Methode 'futter' für das Objekt der Klasse 'Hund' auf. 5 Punkte

Ausgabe3.futter()

print("\n")

# Aufgabe 15: Erstelle eine Klasse 'Polygon' mit einem Konstruktor, der die Anzahl der Seiten in einem Argument erhalten kann und eine Methode 'eingabeSeiten', die die Längen der Seiten bei Eingabe über die Konsole einliest. 10 Punkte

class Polygon:

    def __init__(self, seitenanzahl):
        self.seitenanzahl = seitenanzahl

    def eingabeSeiten(self):
        self.seitenlänge = [float(input("Gib die Länge der " + str(seite + 1) + "- Seite ein: ")) for seite in range(self.seitenanzahl)]
        for x in range(self.seitenanzahl):
            print(x + 1,"- Seitenlänge beträgt: ",self.seitenlänge[x])
    
Ausgabe4 = Polygon(5)
Ausgabe4.eingabeSeiten()