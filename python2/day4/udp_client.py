#!/usr/bin/env python3
import socket
from sys import argv
host='127.0.0.1'
port=12345
addr=(host,port)
s=socket.socket(type=socket.SOCK_DGRAM)

while True:
    try:
        data=input('>')
    except KeyboardInterrupt:
        break
    if data=='quit':
        break
    s.sendto(data.encode(),addr)
    print(s.recvfrom(1024)[0].decode())

s.close()
