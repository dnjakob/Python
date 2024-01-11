import mariadb as mdb
import sys
import sql_tabellen as sqlT
import sql_check as sqlC

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

sqlT.createDatabaseAndTables()
sqlC.eingabe()

conn.close()