#!/bin/bash

sudo /etc/init.d/mysql start

mysql -uroot -e "create database web;"

mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"

mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

cd ~/web/ask

python3 manage.py makemigrations qa

python3 manage.py migrate
