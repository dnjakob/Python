Fruechte = ["Apfel", "Banane", "Kirsche", "Orange", "Kiwi", "Melone", "Mango"]

zahl = int(input("Geben Sie eine Zahl von 0 - 6 ein: "))

if zahl <= 6 and zahl >= 0:
    print("Ja,",Fruechte[zahl],"ist in der Liste")
else:
    print("Sie haben eine ungültige Zahl eingegeben!")

meineListe1 = ["Apfel", "Banane", "Zwetschge"]
meineListe1[1] = "Kirsche"
print(meineListe1)

meineListe2 = ["Apfel", "Banane", "Kirsche", "Orange", "Kiwi", "Melone", "Mango"]
meineListe2[1:3] = ["Himbeere", "Wassermelone"]
print(meineListe2)

meineListe3 = ["Apfel", "Banane", "Zwetschge"]
meineListe3[1:2] = ["Himbeere", "Wassermelone"]
print(meineListe3)

meineListe4 = ["Apfel", "Banane", "Zwetschge"]
meineListe4.insert(2, "Wassermelone")
meineListe4.insert(3, "Erdbeere")
meineListe4.insert(4, "Zitrone")
print(meineListe4)

meineListe5 = ["Apfel", "Banane", "Zwetschge"]
meineListe5.append("Orange")
print(meineListe5)

meineListe6 = ["Apfel", "Banane", "Zwetschge"]
tropisch = ["Mango", "Ananas", "Papaya"]
meineListe6.extend(tropisch)
print(meineListe6)

meineListe7 = ["Apfel", "Banane", "Zwetschge"]
meinTupel = ("Kiwi", "Orange")
meineListe7.extend(meinTupel)
getränke = ["Cola", "Wasser", "Sprite", "Orangensaft"]
meineListe7.extend(getränke)
print(meineListe7)