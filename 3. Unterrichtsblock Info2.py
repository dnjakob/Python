# Iterator & Iterable Übung

# Aufgabe 1

obst = ['Apfel', 'Birne', 'Banane', 'Orange', 'Melone']

for x in obst:
    print(x)

print('\n')

# Aufgabe 2


def fibonacci(anzahl):

    zahl1, zahl2 = 0, 1

    for x in range(anzahl):
        print(zahl1)
        zahl1, zahl2 = zahl2, zahl1 + zahl2


fibonacci(int(input("Wie oft soll die Fibonacci-Zahl berechnet werden? ")))
print('\n')

# Aufgabe 3

wort = 'Python'

for x in reversed(wort):
    print(x)

print('\n')

# Aufgabe 4


class Quadrate:
    def __iter__(self):
        self.term = 1
        return self

    def __next__(self):
        if self.term <= 10:
            quadrat = self.term * self.term
            self.term += 1
            return quadrat
        else:
            raise StopIteration


rechnung = Quadrate()

for quadrat in rechnung:
    print(quadrat)

print('\n')

# Aufgabe 5

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def geradeZahlen(array):
    for x in array:
        if x % 2 == 0:
            print(x)


geradeZahlen(zahlen)
print('\n')


# try & except Übung

# Aufgabe 1

wert1 = int(input("Geben Sie eine Zahl ein: "))
wert2 = int(input("Geben Sie noch eine Zahl ein: "))

try:
    ergebnis = wert1 / wert2
    print(ergebnis)

except ZeroDivisionError:
    print("Man kann nicht durch null teilen!")

print('\n')

# Aufgabe 2

