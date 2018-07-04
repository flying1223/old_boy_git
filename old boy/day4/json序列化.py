#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 19:43:01
# @Author  : flying
'''
import json

def sayhi(name):
    print('hello,',name)

info = {
    'name':'flying',
    'age':18,
    'func':sayhi    #报错，json只处理简单的数据类型
}

f = open("test.txt",'w')
#f.write(info)   #>>>write() argument must be str, not dict
#f.write(str(info))  #把内存的数据对象变成字符串

#print(json.dumps(info)) #>>>{"name": "flying", "age": 18}
f.write(json.dumps(info))
f.close()
'''
import pickle

def sayhi(name):
    print('hello,',name)

info = {
    'name':'flying',
    'age':18,
    'func':sayhi    #
}

f = open("test.txt",'wb')   ##rb 以二进制来进行读文件   网络传输只用二进制   二进制文件用二进制打开
#f.write(info)   #>>>write() argument must be str, not dict
#f.write(str(info))  #把内存的数据对象变成字符串

print(pickle.dumps(info))   #变成二进制了
f.write(pickle.dumps(info))
f.close()








