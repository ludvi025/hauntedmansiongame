#!/usr/bin/python

import select
import socket
import sys

#host = socket.gethostname()
host = input('Enter your ip address: ')
port = 12345
size = 1024

server = socket.socket()
server.bind((host,port))

print ('Starting server...')
server.listen(5)
inputs = [server,sys.stdin]
running = True
print ('Done')

while running:
    inputready, outputready, exceptready = select.select(inputs,[],[])

    for insock in inputready:

        if insock == server:
            client, address = server.accept()
            print ('Got connection from', address)
            inputs.append(client)

        elif insock == sys.stdin:
            dump = sys.stdin.readline()
            running = False

        else:
            data = client.recv(size).decode('UTF-8').upper().encode('UTF-8')
            if data:
                client.send(data)
            else:
                client.close()
                inputs.remove(insock)
server.close()
