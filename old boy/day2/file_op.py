#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-20 20:50:23
# @Author  : flying

#data = open("yesterday",'r',encoding="utf-8").read()  #r是只读
'''
f = open("yesterday",'r',encoding="utf-8")  #文件句柄
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
'''
f = open("yesterday",'r',encoding="utf-8")

for i in range(4):
        print(f.readline())
'''
#f = open("yesterday",'r')
#for line in f.readlines():
#        print(line.strip())
'''
#不打印第十行    这种方法直接读到内存中  只适合小文件   low
f = open("yesterday",'r',encoding="utf-8")
for index.html_test,line in enumerate(f.readlines()):
        if index.html_test == 9:
                print("---------------")
                continue
        print(line.strip())
'''
'''
#high  没在内存中
f = open("yesterday",'r',encoding="utf-8")
count = 0
for line in f:
        if count == 9:
                print("----------------------------------------")
                count += 1
                continue
        print(line.strip())
        count += 1
'''
f = open("yesterday",'r',encoding="utf-8")
#print(f.tell())  #文件句柄打印当前位置》》》0
#print(f.read(5)) #只读五个字符》》》Someh
#print(f.tell())  #文件句柄》》》5
'''
print(f.readline())  #>>>Somehow, it seems the love I knew was always the most destructive kind
print(f.readline())  #>>>不知为何，我经历的爱情总是最具毁灭性的的那种
print(f.readline())  #>>>Yesterday when I was young
print(f.tell())      #>>>146
f.seek(0)            #回到那个位置
print(f.tell())      #>>>0
print(f.readline())  #回到第一位>>>Somehow, it seems the love I knew was always the most destructive kind
'''
print(f.encoding)

#f.truncate(20) #截断从头开始20个字节
f = open("yesterday2","r+")  #r+ 读写是读和末尾追加
#f = open("yesterday2","a+")  #r+ 追加读写
#f = open("yesterday2","rb")  #rb 以二进制来进行读文件   网络传输只用二进制   二进制文件用二进制打开

#f = open("yesterday2","wb")  #wb 以二进制来进行写文件
#f.write("hello world\n".encode())

print(f.readline())
f.write("=========")
print(f.readline())
'''
#没什么用
f = open("yesterday3","w+")  #w+ 写读 先创建一个文件在写也是追加
f.write("=========\n")
f.write("=========\n")
f.write("=========\n")
print(f.tell())
print(f.seek(10))
print(f.tell())
f.write("6666666666666")
print(f.readline())
f.close()
'''

