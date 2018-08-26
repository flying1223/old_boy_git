#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-22
# Author   : flying

'''

'''
'''
静态方法
    与类无关，不能访问类里的任何属性和方法

类方法
    只能访问类变量
属性@property
    把一个方法变成一个静态属性
    flight.status
    @status.setter
    flight.status = 3
    @status.delter
反射
    getattr(obj,str)
    setattr(obj,str,val)
    hasattr(obj,str)
    delattr(obj,str)

__new__ 先于__init__执行
__call__
class Foo(object):

    def __call__():
        print("call")

Foo()() #执行call方法

__metaclass__   用来定义这个类以怎样的形式被创建

try
    ...
except(ValueError,KeyError) as e:
except(ValueError,KeyError),e: #in 2.7
except Exception as e ： 放在异常处理的最后面
else:   #没发生异常，就执行
finally，无论如何都执行

raise ValueError

断言
assert type(obj.name) is str
print('fff')

socket
    tcp/ip send,recv
    udp
    family address
        AF.INET IPV4
        AF.INET6
        AF.UNIX  local
    socket protocol type
        sock.SOCK_STREAM tcp/ip
        sock.SOCK_DGRAM 数据报式socket for UDP

    server:
    server = socket.socket(AF,INET,sock,SOCK_STREAM)
    server.bind(localhost,9999)
    server.listen()

    while True:
        conn,addr = server.accept() #阻塞
        while True:
            print("new conn",addr)
            data = conn,recv(1024) #官方建议，不超过8192
            print(data)
            if not data:
                break #客户端已断开，conn.recv收到的都是空数据
            conn.send(data.upper())

    client:
    client = socket.socket()
    client.connect(serverip,9999)
    client.send(data)
    client.recv(data)

'''














