#!/user/bin/env python
#setup the LAMP
import os
os.system("sudo apt-get update")
os.system("sudo sh mysql.sh")
os.system("sudo apt -y install python3-msqldb")
os.system("sudo apt -y install apache2 php7.2 libapache2-mod-php")
os.system("sudo apt -y install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring")
os.system("sudo service apache2 restart")
os.system("sudo apt -y install git")
os.chdir("/opt")
os.system("sudo git clone git://git.moodle.org/moodle.git")
os.chdir("moodle")
os.system("sudo git branch -a")
os.system("sudo git branch --track MOODLE_37_STABLE origin/MOODLE_37_STABLE")
os.system("sudo git checkout MOODLE_37_STABLE")
os.system("sudo cp -R /opt/moodle /var/www/html/")
os.system("sudo mkdir /var/moodledata")
os.system("sudo chown -R www-data /var/moodledata")
os.system("sudo chmod -R 777 /var/moodledata")

#modify the mysqld.conf file
fp = open('/etc/mysql/mysql.conf.d/mysqld.cnf','r')
lines = []
for line in fp:                  #内置的迭代器, 效率很高
    lines.append(line)
fp.close()

lines.insert(39, 'default_storage_engine = innodb\ninnodb_file_per_table = 1\ninnodb_file_format = Barracuda\n') #在第 LINE+1 行插入
s = ''.join(lines)
fp = open('/etc/mysql/mysql.conf.d/mysqld.cnf', 'w+')
fp.write(s)
fp.close()
del lines[:]
os.system("sudo service mysql restart")

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

