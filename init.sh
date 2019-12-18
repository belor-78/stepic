sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo apt update                     # готовимся скачивать питон
sudo apt install python3.5          # скачиваем питон
sudo rm /usr/bin/python3                         # удалить питон 3.4.3 из системы
sudo ln -s /usr/bin/python3.5 /usr/bin/python3   # поставить на его место питон 3.5
sudo pip3 install django==2.1
sudo pip3 install gunicorn
sudo pip3 install mysqlclient
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
cd /home/box/web/ask
gunicorn --bind=0.0.0.0:8000 --workers=2 --timeout=15 --log-level=debug ask.wsgi:application