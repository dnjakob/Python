# Aufgabe 1
import json

class Person:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def conversion(list):
        personenListe = []

        for eintrag in list:

            person = {
                "name": eintrag.name,
                "alter": eintrag.alter
            }
            personenListe.append(person)

        with open("letztePerson.json", "w") as datei:
            json.dump(personenListe, datei, indent=2)

personen = [Person("Daniel", 18), Person("David", 60), Person("Sammy", 10)]
Person.conversion(personen)

# Aufgabe 2
with open("letztePerson.json", "r") as leseDatei:
    auszulesendeDatei = json.load(leseDatei)

    for eintrag in auszulesendeDatei:
        person = Person(eintrag['name'], eintrag['alter'])
        print(person.name, "-", person.alter)

# Aufgabe 3
personTxt = []

with open("letztePerson.txt", "r") as txtDatei:
    for zeile in txtDatei:
        name, alter = zeile.strip().split(', ')
        personTxt.append({"name": name, "alter": alter})
    
with open("letztePersonTeil2.json", "w") as nochEineDatei:
        json.dump(personTxt, nochEineDatei, indent=2)

# Aufgabe 4

class JsonConverter:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile

    def nameConverter(self, oldName, newName):

        with open(self.inputFile, "r") as oldFile:
            alteListe = json.load(oldFile)

        neueListe = []

        for eintrag in alteListe:
            personObjekt = Person(eintrag['name'], eintrag['alter'])
            if personObjekt.name == oldName:
                personObjekt.name = newName
            neueListe.append({"name": personObjekt.name, "alter": personObjekt.alter})

        with open(self.outputFile, "w") as newFile:
            json.dump(neueListe, newFile, indent=2)

converter = JsonConverter("letztePerson.json", "letztePersonTeil3.json")
converter.nameConverter("David", "Michi")

# Aufgabe 5

import importlib

class dynamichesModul:
    def modulUsage(modulName, functionName, *functionParameters):
        modul = importlib.import_module(modulName)

        function = getattr(modul, functionName)
        function(*functionParameters)

dynamichesModul.modulUsage("gruss", "sage_hallo")