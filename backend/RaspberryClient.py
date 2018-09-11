#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket               
      
#host = socket.gethostname() 
host = '127.0.0.1'
port = 12345               

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print s.recv(1024)
