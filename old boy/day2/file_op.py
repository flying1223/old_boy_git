#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-20 20:50:23
# @Author  : flying

#data = open("yesterday").read()  #r是只读
'''
f = open("yesterday")  #文件句柄
data = f.read()

print(data)
'''
'''
f = open("yesterday2",'w')   #w只写
f.write("我爱北京天安门,\n")
f.write("天安门上太阳升")   #》》》我爱北京天安门,天安门上太阳升   \n换行符

f.close()
'''
'''
f = open("yesterday2",'a')   #a不能读，往后面追加不覆盖原来文件 append追加
f.write("i love you,\n")

f.close()
'''

f = open("yesterday",'r')

for i in range(2,4):
        print(f.readline())














