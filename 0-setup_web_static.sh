#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.
if ![ -x "$(command nginx -v)" ];
then
        sudo apt-get update
        sudo apt-get install nginx -y
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
test_web = "<html><head></head><body>Holberton School</body></html>" 
echo "$test_web" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
