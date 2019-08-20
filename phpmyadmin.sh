#!/bin/bash 
sudo su - root -c "echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' | debconf-set-selections" 
sudo su - root -c "echo 'phpmyadmin phpmyadmin/dbconfig-install boolean false' | debconf-set-selections" 
sudo apt-get -y install phpmyadmin 
