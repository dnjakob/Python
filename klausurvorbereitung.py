# Aufgabe 1
import json

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def convertToJSON(list):

        convertedList = []
        for eintrag in list:

            person = {
                "name": eintrag.name,
                "alter": eintrag.alter
            }
            convertedList.append(person)

        with open("personen.json", "w") as file:
            json.dump(convertedList, file, indent=2)

personenListe = [Person("Daniel", 25), Person("David", 55), Person("Sammy", 16)]
Person.convertToJSON(personenListe)


# Aufgabe 2

with open("personen.json", "r") as file:
    auszulesendeDatei = json.load(file)

    for eintrag in auszulesendeDatei:
        person = Person(eintrag['name'], eintrag['alter'])
        print(person.name,"-", person.alter)

# Aufgabe 3

personenTxt = []

with open("personen.txt", "r") as textDatei:
    for zeile in textDatei:
        name, alter = zeile.strip().split(", ")
        personenTxt.append({"name": name, "alter": int(alter)})
    
with open("konvertierteDatei.json", "w") as file:
    json.dump(personenTxt, file, indent=2)

# Aufgabe 4

class JsonBearbeiter:
    def __init__(self, alteDatei, neueDatei):
        self.alteDatei = alteDatei
        self.neueDatei = neueDatei

    def alterBearbeiten(self,suchenderName, neuesAlter):

        with open(self.alteDatei, "r") as oldFile:
            alteListe = json.load(oldFile)

        neueListe = []

        for eintrag in alteListe:
            personObjekt = Person(eintrag['name'], eintrag['alter'])
            if personObjekt.name == suchenderName:
                personObjekt.alter = neuesAlter
            neueListe.append({"name": personObjekt.name, "alter": personObjekt.alter})
        
        with open(self.neueDatei, "w") as newFile:
            json.dump(neueListe, newFile, indent=2)

datenBearbeiten = JsonBearbeiter("personen.json", "neuePersonen.json")
datenBearbeiten.alterBearbeiten("Daniel", 24)

# Aufgabe 5

import importlib
 
class dynamicModule:
    def modulVerwendung(modulName, functionName, *functionsparameter):
        modul = importlib.import_module(modulName)

        function = getattr(modul, functionName)
        function(*functionsparameter)

dynamicModule.modulVerwendung("gruss", "sage_hallo")