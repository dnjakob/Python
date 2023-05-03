a = 33
b = 32
if b > a:
  print("b ist größer als a\n")
elif b == a:
  print("b ist gleich a\n")
else:
  print("b ist kleiner als a\n")

c = 330
d = 330
print("C\n") if c > d else print("=\n") if c == d else print("D\n")

x = 41

if x > 10:
  print("Größer als 10\n")
  if x > 20:
    print("und auch größer als 20.\n")
  else:
    print(", aber nicht größer als 20.\n")


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
   print(Newmarket[i],"\n")
   i += 1

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Beendet!")

Adj = ["rot", "groß", "lecker"]
Fruechte = ["Apfel", "Banane", "Kirsche"]

for x in Adj:
  for y in Fruechte:
    print(x, y)

