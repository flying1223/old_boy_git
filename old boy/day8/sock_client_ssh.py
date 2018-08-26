#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-03
# @Author  : flying

import socket
client = socket.socket()

client.connect(('localhost',9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode('utf-8'))    #写b只能支持ascii里的，所以只能encode
    cmd_res = client.recv(1024)

    print(cmd_res.decode())

client.close()
