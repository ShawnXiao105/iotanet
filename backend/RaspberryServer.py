#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import socket              

s = socket.socket()         
#host = socket.gethostname() 

port = 12345                
s.bind(('127.0.0.1', port))        

s.listen(5)
           
while True:
    c, addr = s.accept()     
    print 'Connection Address: ', addr
    c.send('hello')
    c.close()               