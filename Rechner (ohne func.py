import math

zahl1 = int(input("Bitte geben Sie die erste Zahl ein: "))
zahl2 = int(input("Bitte geben Sie die zweite Zahl ein: "))
operator = input("plus, minus, mal oder geteilt? ").lower()
ergebnis = 0

if operator == "plus":
    ergebnis = (zahl1 + zahl2)
elif operator == "minus":
    ergebnis = (zahl1 - zahl2)
elif operator == "mal":
    ergebnis = (zahl1 * zahl2)
elif operator == "geteilt":
    ergebnis = (zahl1 / zahl2)

print("Das Ergebnis der Rechnung lautet:",ergebnis)