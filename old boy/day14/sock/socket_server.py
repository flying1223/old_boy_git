#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-27
# @Author  : flying

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8')) #python3 需要转换成bytes类型
    f = open('index.html','rb')
    data = f.read()
    f.close()
    #client.send(bytes("<h1 style='background-color:red;'>Hello,Seven<h1>",encoding='utf-8'))
    client.send(data)
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()
