sudo apt update                     # готовимся скачивать питон
sudo apt install python3.5          # скачиваем питон
sudo pip3 install django==2.1
sudo pip3 install gunicorn
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
sudo cd ask
sudo cd ask
sudo gunicorn -c /home/box/ask/ask/wsgi.py wsgi:application