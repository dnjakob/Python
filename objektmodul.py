class Person:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        print("Name:",self.name,"\nAlter:",self.alter)

P = Person("Daniel", 24)
P.vorstellen()

class Tier:
    
    art = "Katze"
    laut = "miau"

    def machenLaut(self):
        print("Der Laut einer",self.art,"lautet:",self.laut)

T = Tier()
T.machenLaut()
    
class Student(Person):

    matrikelnummer = 6666666

    def vorstellen(self):
        print("Name:", self.name, "\nAlter:",self.alter, "\nMatrikelnummer:",self.matrikelnummer)

    def studieren(self):
        print("Ich studiere gerade...")

S = Student("Daniel", 24)
S.vorstellen()
S.studieren()

class Auto:
    
    marke = "Toyota"
    modell = "Mark II"

    def setKilometerstand(self):
        self._kilometerstand = 69000

    def inkrement(self):
        self._kilometerstand += 1
    
    def abfrageKilometerstand(self):
        print("Der Kilometerstand im",self.marke,self.modell,"beträgt:",self._kilometerstand)

A = Auto()
A.setKilometerstand()
A.inkrement()
A.abfrageKilometerstand()

class Buch:

    titel = "Meditations"
    autor = "Marcus Aurelius"
    seitenzahl = 256

    def buchVorstellung(self):
        print("Ich lese das Buch",self.titel+", welches vom Autor",self.autor,"verfasst worden ist mit einer Seitenzahl von ca.",self.seitenzahl)

B = Buch()
B.buchVorstellung()

class Dozent(Person):

    fachgebiet = "Informatik"

class Professor(Dozent):

    publikationen = ["Informatik1", "Informatik2", "Informatik3"]

    def vorstellen(self):
        super().vorstellen()
        print("Der Professor hat mittlerweile ", len(self.publikationen), " Publikationen im Bereich der ",self.fachgebiet,".")

P = Professor("Daniel", 24)
P.vorstellen()

class Doktorand(Student):

    forschungsgebiet = "Rumänien"

    def studieren(self):
        print("Ich forsche gerade ...")

D = Doktorand("Daniel", 24)
D.studieren()

class Forscher():

    forschungsfeld = "Vampire"

class Schriftsteller():

    veroeffentlicheBuecher = ["Vampir1", "Vampir2", "Vampir3"]

class Wissenschaftsautor(Forscher, Schriftsteller):

    def vorstellen(self):
        print("Der Forscher hat im Bereich",self.forschungsfeld,len(self.veroeffentlicheBuecher),"Werke veröffentlicht mit den Titeln",self.veroeffentlicheBuecher[0]+",",self.veroeffentlicheBuecher[1],"und",self.veroeffentlicheBuecher[2]+".")

W = Wissenschaftsautor()
W.vorstellen()

#Ab hier die rausgefilterten Aufgaben

