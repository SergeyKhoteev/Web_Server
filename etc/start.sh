#!/bin/bash

if [[ `pwd` != '/home/box/web/etc' ]]
then
	cd ../
	cp -r ./ ../web
fi 
#mv ../Web_server ../web
#ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
