sudo ln -sf etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart -D
sudo gunicorn -c etc/config.py hello:app -D

