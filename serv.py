from socket import *

sock = socket(AF_INET,SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(15)

while True:
    connection, address = sock.accept()
    print('connected', address)
    while True:
        data = connection.recv(1024)
        if data:
            print(data)
        if data.decode() == 'close':
            break
        if not data:
            break
        connection.send(data)
    connection.close()