# Aufgabe 1
import json

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def convertToJSON(self):

        person = {
            "name": self.name,
            "alter": self.alter
        }
        
        convertedPerson = json.dumps(person, indent= 2)
        print(convertedPerson)
        personenListe.append(convertedPerson)

personenListe = []

p1 = Person("Daniel", 25)
personenListe.append(p1)
p1.convertToJSON()
p2 = Person("David", 55)
personenListe.append(p2)
p2.convertToJSON()
p3 = Person("Sammy", 16)
personenListe.append(p3)
p3.convertToJSON()
