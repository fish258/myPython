#!/user/bin/env python
import os
os.system("ssh -i /C:/Users/10902/Desktop/XINcan.pem ubuntu@ec2-34-205-141-231.compute-1.amazonaws.com")
os.system("sudo apt-get update")
os.system("sudo apt-get install vim")
os.system("sudo apt -y install apache2 mysql-client mysql-server php libapache2-mod-php")
os.system("sudo apt -y install graphviz aspell ghostscript clamav php7.2-pspell php7.2-curl php7.2-gd php7.2-intl php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-ldap php7.2-zip php7.2-soap php7.2-mbstring")
os.system("sudo service apache2 restart")
os.system("sudo apt -y install git")
os.system("cd /opt")
os.system("sudo git clone git://git.moodle.org/moodle.git")
os.system("cd moodle")
os.system("sudo git branch -a")
os.system("sudo git branch --track MOODLE_37_STABLE origin/MOODLE_37_STABLE")
os.system("sudo git checkout MOODLE_37_STABLE")
os.system("sudo cp -R /opt/moodle /var/www/html/")
os.system("sudo mkdir /var/moodledata")
os.system("sudo chown -R www-data /var/moodledata")
os.system("sudo chmod -R 777 /var/moodledata")

