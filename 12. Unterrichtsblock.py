import math

class Polygon:
    def __init__(self, seitenzahl):
        self.n = seitenzahl
        self.seiten = [0 for i in range(seitenzahl)]

    def eingabeSeiten(self):
        self.seiten = [float(input("Gibt die Länge der "+str(i+1)+". Seite ein: ")) for i in range(self.n)]
    
    def anzeigeSeiten(self):
        for i in range(self.n):
            print("Seite",i+1,"is",self.seiten[i])

class Dreieck(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def ermittleFlaeche(self):
        a, b, c = self.seiten

        s = (a + b + c) / 2

        flaeche = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        flaeche = round(flaeche, 2)
        print('Die Fläche des Dreiecks ist ', flaeche, 'cm²')


class Rechteck(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)

    def ermittleFlaeche(self):
        a, b = self.seiten

        flaeche = a * b
        flaeche = round(flaeche, 2)
        print('Die Fläche des Rechtecks ist ', flaeche, 'cm²')


class Hexagon(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1)
    
    def ermittleFlaeche(self):
        s = self.seiten

        flaeche = (3 * math.sqrt(3) * math.pow(s[0], 2)) / 2
        flaeche = round(flaeche, 2)
        print('Die Fläche des Hexagons ist ', flaeche, 'cm²')

operator = input("Nennen Sie einen entsprechenden Polygon (Dreieck, Rechteck, Hexagon): ")

match operator:
    case "Dreieck":
        d = Dreieck()
        d.eingabeSeiten()
        d.anzeigeSeiten()
        d.ermittleFlaeche()

    case "Rechteck":
        r = Rechteck()
        r.eingabeSeiten()
        r.anzeigeSeiten()
        r.ermittleFlaeche()

    case "Hexagon":
        h = Hexagon()
        h.eingabeSeiten()
        h.anzeigeSeiten()
        h.ermittleFlaeche()