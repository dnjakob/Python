# Daniel Jakob Info 2

# Aufgabe 1

class Tier:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# Aufgabe 2

    def ausgabe(self):
        print("Die",self.name,"ist",self.alter,"Jahre alt.")

# Aufgabe 3        

    def geburtstag(self):
        self.alter = self.alter + 1
        self.ausgabe()

# Aufgabe 4        

    def __str__(self):
        return print(f"Name: {self.name}, Alter: {self.alter}")        

# Aufgabe 2 - 4

Tier1 = Tier("Katze Rudi", 5)
Tier1.ausgabe()
Tier1.geburtstag()
Tier1.__str__()

# Aufgabe 5

Tier2 = Tier("Katze Maya", 9)
Tier2.ausgabe()

# Aufgabe 6

freundesliste = ["Dominik", "David", "Sammy", "Marko", "Karim"]

for freunde in range(0, len(freundesliste)):
    print(freundesliste[freunde])

# Aufgabe 7

freundesliste[2] = "Michi"

for freunde in range(0, len(freundesliste)):
    print(freundesliste[freunde])

# Aufgabe 8

freundesliste.append("Raphael")
freundesliste.append("Dani")

print(len(freundesliste))

# Aufgabe 9

freundesliste.pop(4)
for freunde in range(0, len(freundesliste)):
    print(freundesliste[freunde])

# Aufgabe 10

freundesliste.reverse()

for freunde in range(0, len(freundesliste)):
    print(freundesliste[freunde])

# Daniel Jakob Info 2