sudo apt update                     # готовимся скачивать питон
sudo apt install python3.5          # скачиваем питон
sudo rm /usr/bin/python3                         # удалить питон 3.4.3 из системы
sudo ln -s /usr/bin/python3.5 /usr/bin/python3   # поставить на его место питон 3.5
sudo pip3 install django==2.1
sudo pip3 install gunicorn
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo gunicorn -c /home/box/web/etc/gunicorn-wsgi.conf wsgi:application