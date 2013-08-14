#!/usr/bin/python

import socket 

host = socket.gethostname()
port = 12345
size = 1024

print ('''
Main Menu
---------
c -> Connect to a client
w -> Wait for incoming connections
---------''')
choice = str(input('Select an option: '))

if choice == 'c' or choice == 'C':
    user = str(input('Enter a username: '))

    client_socket = socket.socket()
    client_socket.connect((host,port))
    while True:
        data = input('['+user+'] : ')
        data = data.encode(encoding='UTF-8')
        client_socket.send(data)
        print (client_socket.recv(size).decode('UTF-8'))
    client_socket.close()

elif choice == 'w' or choice == 'W':
    server_socket = socket.socket()
    server_socket.bind((host,port))

    server_socket.listen(5)
    while True:
        client_socket, address = server_socket.accept()
        print ('Got connection from', address)
        data = client_socket.recv(size)
        if data:
            client_socket.send(data.decode('UTF-8').upper().encode('UTF-8'))
        client_socket.close()
