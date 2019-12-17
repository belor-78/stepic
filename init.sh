sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo cd ask
sudo cd ask
sudo cd ask
sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind='0.0.0.0:8000' wsgi:application
