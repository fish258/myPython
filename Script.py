#!/user/bin/env python
#setup the LAMP
import os
os.system("sudo apt-get update")
os.system("sudo bash myPython/mysql.sh")

os.system("sudo apt -y install apache2 php7.2 libapache2-mod-php")
os.system("sudo apt -y install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring")
os.system("sudo service apache2 restart")
os.system("sudo apt -y install git")
os.system("sudo apt -y install python3-mysqldb")
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
#os.system("sudo python3 myPython/mysql.py")

#creat and setup mysql
import MySQLdb
db = MySQLdb.connect("localhost","root","1stgroup","mysql",charset = "utf8")
cursor = db.cursor()
cursor.execute("CREATE DATABASE moodle DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
cursor.execute("create user 'user1'@'localhost' IDENTIFIED BY '981204';")
cursor.execute("GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,CREATE TEMPORARY TABLES,DROP,INDEX,ALTER ON moodle.* TO user1@localhost IDENTIFIED BY '981204';")
db.close()

#create the config.php in moodle
os.chdir("/var/www/html/moodle")
os.system("sudo touch config.php")

#setup the config.php
import socket,struct,fcntl
# def get_ip(ifname):#get ip address
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])
# ownip = get_ip('eth0')
p = os.popen("curl ifconfig.me")
publicIP = p.read()
f = open('/var/www/html/moodle/config.php','w')
f.write("<?php  // Moodle configuration file \n"
         "\n"
        "unset($CFG);\n"
        "global $CFG;\n"
        "$CFG = new stdClass();\n"
        "\n"
        "$CFG->dbtype    = 'mysqli';\n"
        "$CFG->dblibrary = 'native';\n"
        "$CFG->dbhost    = 'localhost';\n"
        "$CFG->dbname    = 'mysql';\n"
        "$CFG->dbuser    = 'root';\n"
        "$CFG->dbpass    = '1stgroup';\n"
        "$CFG->prefix    = 'mdl_';\n"
        "$CFG->dboptions = array (\n"
         " 'dbpersist' => 0,\n"
          "  'dbport' => '',\n"
           "   'dbsocket' => ''\n,"
            "    'dbcollation' => 'utf8mb4_unicode_ci',\n"
             "   );\n"
              "   \n"
              "$CFG->wwwroot   = 'http://%s/moodle';\n"
                "$CFG->dataroot  = '/var/moodledata';\n"
                "$CFG->admin     = 'admin';\n"
                "\n"
                "$CFG->directorypermissions = 0777;\n"
                 "\n"
                "require_once(__DIR__ . '/lib/setup.php');\n"
                 "\n"
                "// There is no php closing tag in this file,\n"
                "// it is intentional because it prevents trailing whitespace problems!\n"%(publicIP))
f.close()
os.system("sudo php /var/www/html/moodle/install.php")





