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
    for x in range(1, 4):
        cur.execute("INSERT INTO erstetabelle VALUES("")