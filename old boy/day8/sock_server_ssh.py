#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-26
# @Author  : flying

import socket,os

server = socket.socket()
server.bind(('localhost',9999))

server.listen()

while True:
    print('等待新指令')
    conn,addr = server.accept()
    print('new conn',addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        print('执行指令：',data)
        cmd_res = os.popen(data.decode()).read()    #os接收字符串，执行结果也是字符串
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output ...'
        conn.send(cmd_res.encode('utf-8'))

server.close()