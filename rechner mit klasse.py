class Taschenrechner():

    try:
        zahl1 = int(input('Geben Sie ihre erste Zahl ein: '))
        zahl2 = int(input('Geben Sie ihre zweite Zahl ein: '))

        def operator(self):
            self.operator = input(
                "Welcher Operator soll verwendet werden (+, -, *, /): ")

        def rechnen(self):
            match(self.operator):
                case "+":
                    self.ergebnis = self.zahl1 + self.zahl2
                    return self.ergebnis
                case "-":
                    self.ergebnis = self.zahl1 - self.zahl2
                    return self.ergebnis
                case "*":
                    self.ergebnis = self.zahl1 * self.zahl2
                    return self.ergebnis
                case "/":
                    self.ergebnis = self.zahl1 / self.zahl2
                    return self.ergebnis

    except Exception as e:
        print(f'{e}')
        Taschenrechner()