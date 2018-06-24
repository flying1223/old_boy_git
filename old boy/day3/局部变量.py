#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 21:21:10
# @Author  : flying
'''
sex = 'girl'

def chang_name(name):
    sex = 'boy'
    print('before change:',name,sex)
    name = 'Flying'   #局部变量只在函数内部生效 这个函数就是变量的作用域
    print('after change:',name,sex)

name = "flying"
chang_name(name)#>>>before change: flying boy   after change: Flying boy
print(name,sex) #>>>flying girl
'''
'''
sex = 'girl'

def chang_name(name):
    global sex   #我要在函数中改变全局变量   尽量不用global
    sex = 'boy'
    print('before change:',name,sex)
    name = 'Flying'   #局部变量只在函数内部生效 这个函数就是变量的作用域
    print('after change:',name,sex)

name = "flying"
chang_name(name)#>>>before change: flying boy   after change: Flying boy
print(name,sex) #>>>flying boy
'''
#除了字符串和数字外   列表，字典，集合,类都可以局部变量改全局变量
names = ['zhangsan','lisi','flying']
names_t
def chang_name():
    names[0] = '777'
    print(names)

chang_name()    #>>>['777', 'lisi', 'flying']
print(names)    #>>>['777', 'lisi', 'flying']

