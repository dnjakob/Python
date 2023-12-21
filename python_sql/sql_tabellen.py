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

def createDatabaseAndTables():
    cur.execute("CREATE DATABASE IF NOT EXISTS pythondatenbank")
    cur.execute("USE pythondatenbank")
    cur.execute("CREATE TABLE IF NOT EXISTS erstetabelle (id SMALLINT NOT NULL, tier TINYTEXT, age SMALLINT, farbe TINYTEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS zweitetabelle (id SMALLINT NOT NULL, vorname TINYTEXT, nachname TINYTEXT, age SMALLINT)")
    cur.execute("CREATE TABLE IF NOT EXISTS drittetabelle (id SMALLINT NOT NULL, Hochschule TINYTEXT, Ort TINYTEXT, studentenzahl SMALLINT)")
    insertDataIntoTables()

def insertDataIntoTables():
    ersteTabelleInsert = [(1, 'katze', 4, 'braun'),
                          (2, 'hund', 2, 'schwarz'),
                          (3, 'maus', 6, 'grau')]
    
    zweiteTabelleInsert = [(1, 'David', 'Wagner', 38),
                          (2, 'Samuel', 'Droc', 16),
                          (3, 'Daniel', 'Jakob', 24)]
    
    dritteTabelleInsert = [(1, 'TH Rosenheim', 'Rosenheim', 3500),
                          (2, 'LMU München', 'München', 5000),
                          (3, 'TU Zürich', 'Zürich', 4000)]
    
    insertQueryOne = """INSERT INTO erstetabelle (id, tier, age, farbe)
                        VALUES (%s, %s, %s, %s) """
    
    insertQueryTwo = """INSERT INTO zweitetabelle (id, vorname, nachname, age)
                        VALUES (%s, %s, %s, %s) """

    insertQueryThree = """INSERT INTO drittetabelle (id, Hochschule, Ort, studentenzahl)
                        VALUES (%s, %s, %s, %s) """
    
    cur.executemany(insertQueryOne, ersteTabelleInsert)
    conn.commit()
    print(cur.rowcount, "Record inserted successfully into erstetabelle")
    cur.executemany(insertQueryTwo, zweiteTabelleInsert)
    conn.commit()
    print(cur.rowcount, "Record inserted successfully into zweitetabelle")
    cur.executemany(insertQueryThree, dritteTabelleInsert)
    conn.commit()
    print(cur.rowcount, "Record inserted successfully into drittetabelle")