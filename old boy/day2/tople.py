#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11
# @Author  : flying

names = ("1zhangsan","李xiaofei","@lisi","wangwu","maliu","xiaofei")

print(names.count('xiaofei'))

print(names.index('xiaofei'))

a=list(names)
print(a)

b = tuple(a)
print(b)

c = {'apple':1, 'banana':2, 'orange':3}
print(tuple(c))
print(tuple(c.values()))
print(list(c))
print(list(c.values()))


