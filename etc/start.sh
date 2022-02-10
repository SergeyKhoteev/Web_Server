#!/bin/bash



if [[ `pwd` != '/home/box/web/etc' ]]
then
	cp -r /home/box/Web_Server /home/box/web
fi 

ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx start

sudo ln -s /home/box/web/etc/gunicorn/gunicorn.service /etc/systemd/system/gunicorn.service
sudo ln -s /home/box/web/etc/gunicorn/gunicorn.socket /etc/systemd/system/gunicorn.socket

cd /home/box/web
gunicorn -b 127.0.0.1:8080 -w=2 hello:app
