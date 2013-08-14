#!/usr/bin/python

import socket

client_socket = socket.socket()
#host = socket.gethostname()
host = input('Enter ip address to connect to: ')
port = 12345
size = 1024

user = str(input('Enter a username: '))

client_socket = socket.socket()
client_socket.connect((host,port))

running = True
while running:
    data = input('['+user+'] : ')
    if data == "/quit":
        running = False
    else:
        data = data.encode(encoding='UTF-8')
        client_socket.send(data)
        print (client_socket.recv(size).decode('UTF-8'))
client_socket.close()
