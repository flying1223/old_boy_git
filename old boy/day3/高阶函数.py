#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-25 19:52:56
# @Author  : flying
'''
把一个函数当作参数传给另个函数
'''

def add(a,b,f):
    return f(a) + f(b)

res = add(3,-6,abs)
print(res)

