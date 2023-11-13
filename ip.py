
import sqlite3


connection = sqlite3.connect("ip.sl3", 5)

cur = connection.cursor()

cur.execute("CREATE TABLE ip_list (ip TEXT);")

connection.commit()
connection.close()
