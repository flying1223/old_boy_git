#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-03
# Author   : flying
'''

'''


'''

静态方法：只是名义上归类管理，实际上在静态方法访问不了类或实例中的任何属性

类方法：只能访问类变量，不能访问实例变量

属性方法：把一个发法变成一个静态属性

hasattr(obj,name_str):判断一个对象里是否有对应的字符串的方法
getattr(obj,name_str):根据字符串去获取obj对象里的对应的方法的内存地址
setattr(obj,'y',z) is equivalent to 'x.y = v'
delattr
'''
'''
异常
    try:
        code
    except (error1,error2) as e:
        print(e)
    except Exception as e:#抓住所有错误

Socket网络编程
    OSIq层
        应用
        表示
        会话
        传输
        网络 ip
        数据链路 mac
        物理层

TCP/IP 三次握手，四次断开
A--syn---B
B--ayn ack ---A
A--ack---B

UDP

socket：对所有上层协议的底层封装
实现一个socket至少要分以下几步，(伪代码)

Socket socket = getSocket(type = "TCP")  #设定好协议类型
connect(socket, address = "1.2.3.4", port = "80") #连接远程机器
send(socket, "Hello, world!") #发送消息
close(socket) #关闭连接
'''











