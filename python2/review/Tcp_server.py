#!/usr/bin/env python3
import socket
class TcpServ:
    def __init__(self,addr=('',12345)):
        self.addr=addr
    def link(self):
        while True:
            s=socket.socket()
            cli_sock,cli_addr=s.accept()
            s.listen(1)
            s.bind(self.addr)
        while True:
            pass

if __name__ == '__main__':
    host=''
    port=12345
    addr=(host,port)
    t=TcpServ(addr)

