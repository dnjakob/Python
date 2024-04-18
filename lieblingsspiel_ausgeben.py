class Lieblingsspiel:
    def __init__(self):
        self.spiel = input("Wie lautet dein Lieblingsspiel: ")
        self.hersteller = input("Wie lautet der Hersteller des Spiels: ")

    def message(self):
        print("Mein Lieblingsspiel lautet", self.spiel," welches von", self.hersteller, "veröffentlicht worden ist.")

meinLieblingsspiel = Lieblingsspiel()
meinLieblingsspiel.message()