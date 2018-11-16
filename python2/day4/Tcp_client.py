#!/usr/bin/env python3
import socket
from sys import argv
def communicate(cs):
    while True:
        try:
            data=input('>')
            cs.send(data.encode())
        except KeyboardInterrupt:
            break
        else:
            if data.strip()=='quit':
                break
            data=cs.recv(1024).decode()
            print(data)

if __name__ == '__main__':
    host=argv[1]
    port=int(argv[2])
    addr=(host,port)
    cs=socket.socket()
    cs.connect(addr)
    communicate(cs)
    cs.close()