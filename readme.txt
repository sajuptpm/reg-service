
###Install mysql: ubuntu 13.10 ###
#sudo apt-get install mysql-server
#apt-get install python-mysqldb
#sudo apt-get install libmysqlclient-dev
#easy_install MySQL-python

### How to install dependencies ###
#virtualenv env
#. env/bin/activate
#pip install requirements.txt

###How to run the service ###
#python deploy.py

###You can change following settings in config_settings.py####
KEYSTONE_HOST = "127.0.0.1"
KEYSTONE_ADMIN_TOKEN = "tokentoken"
KEYSTONE_ADMIN_PORT = 35357
KEYSTONE_PUBLIC_PORT = 5000

DEFAULT_PROJECT_NAME = "demo"
DEFAULT_ROLE_NAME = "Member"
DEFAULT_DOMAIN_NAME = "Default"

###You can change Hostname and Port of this service in deploy.py###
SECURITY_SERVICE_HOST = "127.0.0.1"
SECURITY_SERVICE_PORT = 8080

###DB Settings###
#Create new user and db
mysql>> CREATE USER 'jio'@'localhost' IDENTIFIED BY 'jio';
mysql>> create database jiocloud;
mysql>> grant all privileges on jiocloud.* to jio@localhost;
#sqlalchemy settings
e = create_engine("mysql://jio:jio@localhost/jiocloud", echo='debug')
 
