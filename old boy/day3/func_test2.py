#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 17:13:11
# @Author  : flying

'''
1.代码重用
2.保持一致性
3.可扩展性
'''

import time
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write("%s end action\n" %time_current)

def test1():
    print('test1 starting action...')
    logger()

def test2():
    print('test2 starting action...')
    logger()

def test3():
    print('test3 starting action...')
    logger()

test1()
test2()
test3()




