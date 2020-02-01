sudo /etc/init.d/nginx stop
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/ngix.conf /etc/nginx/sites-enabled/default
gunicorn -b 0.0.0.0:8080 hello
sudo /etc/init.d/nginx start
