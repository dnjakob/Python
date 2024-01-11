import mariadb as mdb
import sys

try:
    conn = mdb.connect(
        user="daniel",
        password="daniel",
        host="localhost",
        port=3306

    )

except mdb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

def eingabe():
    tabellenauswahl = int(input("Welche Tabelle (1, 2, 3) soll ausgewählt werden? "))
    suchbegriff = input("Wonach soll gesucht werden? ")
    matching(tabellenauswahl, suchbegriff)

def matching(zahl, suchbegriff):
    if zahl == 1:
        suchergebnis = f"""SELECT * FROM erstetabelle WHERE ID LIKE '%{suchbegriff}%'
                        OR tier LIKE '%{suchbegriff}%' OR age LIKE 
                        '%{suchbegriff}%' OR farbe LIKE '%{suchbegriff}%'"""
        ausfuehren(suchergebnis, suchbegriff)
    elif zahl == 2:
        suchergebnis = f"""SELECT * FROM zweitetabelle WHERE ID LIKE '%{suchbegriff}%'
                        OR vorname LIKE '%{suchbegriff}%' OR nachname LIKE 
                        '%{suchbegriff}%' OR age LIKE '%{suchbegriff}%'"""
        ausfuehren(suchergebnis, suchbegriff)
    elif zahl == 3:
        suchergebnis = f"""SELECT * FROM drittetabelle WHERE ID LIKE '%{suchbegriff}%'
                        OR Hochschule LIKE '%{suchbegriff}%' OR Ort LIKE 
                        '%{suchbegriff}%' OR studentenzahl LIKE '%{suchbegriff}%'"""
        ausfuehren(suchergebnis, suchbegriff)
    else:
        print("Die Tabelle existiert nicht!")
        eingabe()
    
def ausfuehren(suchergebnis, suchbegriff):
    cur.execute(suchergebnis)
    resultate = cur.fetchall()

    if resultate:
        print(f"Ergebnisse für '{suchbegriff}':")
        for r in resultate:
            print(r)
    else:
        print(f"Der Begriff '{suchbegriff}' ist nicht vorhanden!")