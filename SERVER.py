#SERVER LOGIC

#setup
import socket

HOST = '192.168.1.12'

PORT = 9999

#create and configure socket 
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))

#listen for connections
server_socket.listen(5)

print('Server is listening for connections...')

#main loop to handle connections 
while True:
    #accept a connection
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')

    #communicate with the client
    message = client_socket.recv(1024).decode('utf-8')
    print(f'Received data: {message}')
    client_socket.send('Message received'.encode('utf-8'))
    #close client connection
    client_socket.close()
    print(f'Connection with {client_address} ended!')





