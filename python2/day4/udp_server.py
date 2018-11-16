#!/usr/bin/env python3
import socket
import time
host=''
port=12345
addr=(host,port)
s=socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

while True:
    try:
        data,cli_addr=s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    data='[%s] %s' % (time.strftime('%R'),data)
    s.sendto(data.encode(),cli_addr)
s.close()

