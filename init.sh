sudo /etc/init.d/nginx stop
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
gunicorn -b '0.0.0.0:8080' hello:application
#sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi:application  &
sudo /etc/init.d/nginx start
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi

sudo /etc/init.d/mysql start
sudo -uroot -e 'create database stepik;'
sudo -uroot -e "create user 'box'@'localhost';"
sudo -uroot -e "grant all privileges on stepik.* to box@localhost;"

