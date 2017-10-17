#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

# socket udp client端

HOST = 'localhost'
PORT = 9999
server_addr = (HOST, PORT)

s = socket(AF_INET, SOCK_DGRAM)
s.connect((HOST, PORT))

while True:
    message = input('Please input messages > ').strip()
    s.sendto(message.encode(), server_addr)
    data, addr = s.recvfrom(1024)
    print(data.decode())
    print(addr)
s.close()
