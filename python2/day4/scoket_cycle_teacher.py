#!/usr/bin/env puython3
import socket
import re
host=''             #服务监听在0.0.0.0
port=1234          #服务的端口号，自定义端口号应大于1024
addr=(host,port)    #
s = socket.socket() #创建套接字，默认使用TCP
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)        #为套接字绑定地址
s.listen(1)         #启动侦听过程，1表示允许多少个客户端连接，可设置多少都没有

while True:
    try:
        client_sock,client_addr=s.accept()
    except KeyboardInterrupt:
        break
    print('hello',client_addr)

    while True:
        try:
            data = client_sock.recv(1024).decode()  #bytes-->str
        except UnicodeDecodeError:
            break
        print(data)
        sdata=input('>') + '\r\n'
        client_sock.send(sdata.encode())  #str-->bytes
        if data.strip()=='quit':
            break
    print(data)

    client_sock.close()

s.close()
