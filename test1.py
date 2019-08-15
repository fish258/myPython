import os
import MySQLdb
db = MySQLdb.connect("localhost","root","1stgroup","mysql",charset = "utf8")
sursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)
db.close()
