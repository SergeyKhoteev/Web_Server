#!/bin/bash



if [[ `pwd` != '/home/box/web/etc' ]]
then
	cd /home/box
	cp -r /home/box/web /home/box/Web_Server/
fi 

ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
