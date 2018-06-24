#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 16:59:35
# @Author  : flying

def func1():   #定义函数
    """testing"""
    print('in the func1')
    return 0

def func2():   #定义过程   过程就是没有返回值的函数   在Python中过程也当做函数
    '''testing2'''
    print('in the func2')

x = func1()
y = func2()

print('from fun1 return is %s' %x)
print('from fun2 return is %s' %y)

