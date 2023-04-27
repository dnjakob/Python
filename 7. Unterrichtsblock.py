meineListe = ["Apfel", "Zwetschge", "Birne"]
listenKopie = meineListe.copy()
print(listenKopie)

liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

liste3 = liste1 + liste2
print(liste3)


liste3 = ["a", "b", "c"]
liste4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in liste4:
  liste3.append(x)

print(liste1)

liste5 = ["a", "b", "c"]
liste6 = [1, 2, 3]
liste7 = ["Apfel", "Birne", "Banane"]

liste5.extend(liste5)
liste5.extend(liste6)
liste5.extend(liste7)
print(liste5)

liste8 = ["a", "b", "c"]
liste9 = [1, 2, 3]

liste9.pop(1)

print(liste9)