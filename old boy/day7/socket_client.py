#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-20
# Author   : flying

#客户端
import socket

client = socket.socket() #默认就是ipv4  TCP/IP   声明socket类型同时声称socket链接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
#    client.send(b"hello word")  #变成byte类型
    client.send(msg.encode("utf-8"))  #变成byte类型
    data = client.recv(1024)    #收1024字节
    print("recv:",data.decode())

client.close()










