#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
data = bytes(input('Enter text to echo: '),'UTF-8')
s.send(data)
print (s.recv(1024))
s.close()
