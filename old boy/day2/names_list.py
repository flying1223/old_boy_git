#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 16:39:46
# @Author  : flying
import copy

names = ["1zhangsan","李xiaofei","@lisi",["1","2"],"wangwu","maliu","xiaofei"]
'''
#查
print(names[1])
print(names[1:3]) #顾头不顾尾,切片
print(names[:3])
print(names[-1])    #>>>xiaofei
print(names[-3:-1]) #>>>['wangwu', 'maliu']
print(names[-3:])   #>>>['wangwu', 'maliu', 'xiaofei']
'''
'''
#增
names.append('xiaofei') #添加到末尾
names.insert(1,"666") #插入到具体位置，不能批量插入
print(names)  #>>>['1zhangsan', '666', '李xiaofei', '@lisi', ['1', '2'], 'wangwu', 'maliu', 'xiaofei', 'xiaofei']
'''
'''
#改
names[2]='777'
print(names)
'''
'''
#删
names.remove("lisi")
del names[1]
names.pop(1)
print(names)
'''
#索引index
#print(names[names.index.html("xiaofei")])   #>>>xiaofei

'''
print(names.count("xiaofei"))
#names.clear()#清空列表
names.reverse()#反转列表顺序
names.sort()#排序
print(names)

names2 = [1,2,3,4]
names.extend(names2)#扩展
#del names2 #删除列表
print(names,names2)
'''
'''
#name2 = names.copy() #只copy第一层
name2 = copy.deepcopy(names)#深copy
print(name2)
names[-1] = "晓飞"
names[3][0] = "fff"
print(names,name2)
'''
print(names[::2])
for i in names:
    print(i)

#列表生成式
L = [i*2 for i in range(10)]
print(L)    #>>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]



















