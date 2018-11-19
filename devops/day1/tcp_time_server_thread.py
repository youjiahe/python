#!/usr/bin/env python3
import time
import socket
import os
class TcpSer:
    def __init__(self,host='',port=12345):
        self.addr=(host,port)
        self.serv=socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)
    def chat(self,client_sock):
        while True:
            data=client_sock.recv(1024).decode()
            if data.strip()=='quit':
                break
            data='[%s] %s'  % (time.strftime('%R'),data)
            try:
                client_sock.send(data.encode())
            except BrokenPipeError:
                break

    def mainloop(self):
        while True:
            try :
                client_sock,client_addr=self.serv.accept()
            except KeyboardInterrupt:
                print()
                break
            pid=os.fork()
            if pid:
                client_sock.close()
                while True:
                    result = os.waitpid(-1, 1)
                    print(result)
                    if result[0]==0:
                        break
            else:
                self.chat(client_sock)
                client_sock.close()
                exit()

        self.serv.close()

if __name__ == '__main__':
    s=TcpSer()
    s.mainloop()
