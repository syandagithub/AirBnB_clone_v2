#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://YoutTube.com;
    }

    error_page 404 /404.html;

    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
