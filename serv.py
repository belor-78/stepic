from socket import *
import _thread as thread

sock = socket(AF_INET,SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(15)

def handleClient(connection):
    while True:
        data = connection.recv(1024)
        if len(data) > 1024:
            print('breaking',data)
            break
        if data.decode() == 'close':
            break
        if not data:
            break
        connection.send(data)
    connection.close()

while True:
    connection, address = sock.accept()
    print('connected', address)
    thread.start_new_thread(handleClient, (connection,))
    
