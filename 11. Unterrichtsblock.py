class Taschenrechner:
    def __init__(self, zahl1, zahl2):
        self.zahl1 = zahl1
        self.zahl2 = zahl2

    def plus(self):
        self.ergebnis = self.zahl1 + self.zahl2
        print("Das Ergebnis dieser Rechnung lautet",self.ergebnis)

    def minus(self):
        self.ergebnis = self.zahl1 - self.zahl2
        print("Das Ergebnis dieser Rechnung lautet",self.ergebnis)

    def mal(self):
        self.ergebnis = self.zahl1 * self.zahl2
        print("Das Ergebnis dieser Rechnung lautet",self.ergebnis)

    def geteilt(self):
        self.ergebnis = self.zahl1 / self.zahl2
        print("Das Ergebnis dieser Rechnung lautet",self.ergebnis)

eingabe1 = int(input("Bitte geben Sie ihre erste Zahl ein: "))
eingabe2 = int(input("Bitte geben Sie ihre zweite Zahl ein: "))

r1 = Taschenrechner(eingabe1, eingabe2)

operator = input("Wählen Sie einen entsprechenden Operator (+, -, *, /) aus: ")

match operator:
    case "+":
        r1.plus()
    
    case "-":
        r1.minus()

    case "*":
        r1.mal()

    case "/":
        r1.geteilt()
