!/bin/bash



if [[ `pwd` != '/home/box/web/etc' ]]
then
	cp -r /home/box/Web_Server /home/box/web
fi 

ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default

sudo /etc/init.d/nginx start

sudo /etc/init.d/mysql start

sudo mysql -u root -e "CREATE DATABASE boxask1;"
sudo mysql -u root -e "CREATE USER 'askbox1'@'localhost' IDENTIFIED BY 'ord';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'askbox1'@'localhost' WITH GRANT OPTION;"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON \`boxask1\`.* TO 'askbox1'@'localhost';"
 
sudo ln -s /home/box/web/etc/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
sudo ln -s /home/box/web/etc/gunicorn/gunicorn.socket /etc/systemd/system/gunicorn.socket

cd /home/box/web

gunicorn -c gunicorn.hello.conf.py hello:app &
gunicorn -c gunicorn.django.conf.py ask.wsgi:application &
