#CLIENT LOGIC

#setup
import socket 

server_ip_address = '192.168.1.12'

server_port_number = 9999

#create and connect socket 
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((server_ip_address, server_port_number))

#send data 
message = 'Hello, Server!'

client_socket.send(message.encode('utf-8'))

#receive response 
decoded_response = client_socket.recv(1024).decode('utf-8')

print(f'Received response from server: {decoded_response}')

#close connection
client_socket.close()