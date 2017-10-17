#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

# socket udp server端
BUF_SIZE = 1024
HOST = '127.0.0.1'
PORT = 9999
server_address = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(server_address)
print('waiting for messages ....')

while True:
    data, address = s.recvfrom(BUF_SIZE)
    print('data:', data.decode())
    print('address', address)
    s.sendto(data.decode().upper().encode(), address)
s.close()
