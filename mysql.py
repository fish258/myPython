#creat and setup mysql
import MySQLdb
db = MySQLdb.connect("localhost","root","1stgroup","mysql",charset = "utf8")
sursor = db.cursor()
cursor.execute("CREATE DATABASE moodle DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
cursor.execute("create user 'user1'@'localhost' IDENTIFIED BY '981204';")
cursor.execute("GRANT ALL ON moodle.* TO user1@localhost IDENTIFIED BY '981204';")
data = cursor.fetchone()
print(data)
db.close()
