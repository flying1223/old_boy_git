#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11
# @Author  : flying
import copy

persion = ['name',['saving',100]]
'''
#几种浅copy方法
p1 = copy.copy(persion)

p2 = persion[:]

p3 = list(persion)
'''

p1 = persion[:]
p2 = persion[:]
p1[0] = 'tongxin'
p2[0] = 'flying'
p1[1][1] = 50
print(p1,p2)
