Liste1 = ["BMW", "Audi", "Volkswagen"]
Liste2 = ["Nissan", "Toyota", "Honda"]

def fusionieren(x, y):
    z = x + y
    print(z)

fusionieren(Liste1, Liste2)


def namenspaare(vorname):
  print(vorname + " Maier")

namenspaare("Emil")
namenspaare("Emilia")
namenspaare("Franz")


def paarnamen(vorname, nachname):
  print(vorname,nachname)

paarnamen("Herbert","Weberknecht")


def tierisch(*tiere):
  print("Das kleinste Tier ist " + tiere[4])

tierisch("das Pferd", "der Elefant", "der Hund", "die Katze", "der Igel", "Samuel")

def ausgabe(x):
  print("\n",x[1])

JDM = ["Nissan", "Toyota", "Honda"]
USDM = ["Ford", "Chevrolet", "Chrysler", "Dodge"]
EDM = ["BMW", "VW", "Audi", "Porsche", "Opel"]
i = 0

if len(USDM) > len(EDM):
  Newmarket = USDM + JDM
elif len(EDM) > len(USDM):
  Newmarket = EDM + JDM
else:
  pass
while len(Newmarket) > i:
   print(Newmarket[i])
   i += 1

ausgabe(Newmarket)