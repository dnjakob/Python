l = open("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\loremipsum.txt", "r", encoding="utf-8")
print(l.read())

print("\n")

eingabe = input("Schreibe einen Satz: ")

if eingabe == "Was geht am Wochenende?":
    mm = open("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\maxundmoritz.txt", "r", encoding="utf-8")
    for x in mm:
        if "Menschen necken, Tiere quälen," in x or "Äpfel, Birnen, Zwetschen stehlen" in x:
            print(x)

print("\n")

bt = open("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispieltext.txt", "a", encoding="utf-8")
bt.write("Wenn ein Schwan singt, lauschen die Tiere.")
bt.close()

bt = open("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispieltext.txt", "r", encoding="utf-8")
print(bt.read())
bt.close()

print("\n")

import os

einwilligung = input("Wollen Sie den Ordner löschen? (Ja/Nein): ")

if einwilligung == "Ja":
    if os.path.exists("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispielordner"):
        os.remove("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispielordner\\textdatei1.txt")
        os.remove("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispielordner\\textdatei2.txt")
        os.remove("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispielordner\\textdatei3.txt")
        os.rmdir("C:\\Users\\jakob\\Desktop\\Workspaces\\Python\\beispielordner")
    else:
        print("Es existiert der angegebene Pfad nicht!")

else:
    print("Es wurde nix verändert!")