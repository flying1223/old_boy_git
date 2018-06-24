#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 14:23:57
# @Author  : flying
#f = open("yesterday_2","r")
with open("yesterday_2","r") as f: #自动关闭文件
    print(f.encoding)
    for line in f:
        print(line.strip())

'''
with open("log1") as obj1,open("log2") as obj2 :  #打开多个文件
    pass

#一行代码不超过80字节
with open("yesterday_2","r") as f,\
        open("yesterday_2","r") as f2:
'''