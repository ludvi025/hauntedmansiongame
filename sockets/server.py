#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
size = 1024
s.bind((host,port))

s.listen(5)
while True:
    client, addr = s.accept()
    print ('Got connectio from', addr)
    data = bytes(str(client.recv(size)).upper(),'UTF-8')
    if data:
        client.send(data)
    client.close()
