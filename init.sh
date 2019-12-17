sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind='0.0.0.0:8080' hello:app
