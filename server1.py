import socket
import time
HOST = '192.168.1.12'
PORT = 1234
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))
server_socket.listen(5)
print('Server is listening...')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')
    
    while True:
        message = f'Hello, Client..you are conected for..{time.ctime()}s'
        client_socket.send(message.encode('utf-8'))
        time.sleep(2)