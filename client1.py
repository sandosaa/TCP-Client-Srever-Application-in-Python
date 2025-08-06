import socket 

server_ip_address = '192.168.1.12'

server_port_number = 1234

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((server_ip_address, server_port_number))
while True:
    message = client_socket.recv(1024).decode('utf-8')
    print(message)
    client_socket.send('Message received'.encode('utf-8'))