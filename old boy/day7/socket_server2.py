#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-03
# Author   : flying

#服务端
import socket

server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听的端口

server.listen() #监听

print('我在等电话')
while True:
    conn,addr = server.accept() #等电话打进来
    #conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn,addr)
    print('电话来了')

    while True:
        data = conn.recv(1024)
        print("recv",data.decode())
        if not data:
            print("client has lost...")
            break
        conn.send(data.upper())

server.close()



