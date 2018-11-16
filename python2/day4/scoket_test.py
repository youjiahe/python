#!/usr/bin/env puython3
import socket
host=''             #服务监听在0.0.0.0
port=12345          #服务的端口号，自定义端口号应大于1024
addr=(host,port)    #
s = socket.socket() #创建套接字，默认使用TCP
#加上下面的语句，就无需等待一分钟，才能再次访问
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)        #为套接字绑定地址
s.listen(1)         #启动侦听过程，1表示允许多少个客户端连接，可设置多少都没有
client_sock,client_addr=s.accept()  #接受客户端的访问，返回客户端的套接字和地址
print('hello',client_addr) #接收客户端连接后，打印hello
data=client_sock.recv(1024)  #最多接收1024字节数据
client_sock.send(b'I meet you!\r\n')  #向客户端发送数据
client_sock.close()
s.close()
