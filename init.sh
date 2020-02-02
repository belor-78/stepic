sudo /etc/init.d/nginx stop
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/ngix.conf /etc/nginx/sites-enabled/test.conf
gunicorn -b 0.0.0.0:8080 hello:application
sudo /etc/init.d/nginx start
