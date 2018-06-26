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

'''
1.把一个函数名当作实参传给另一个函数
2.返回值中包含函数名
'''
'''
def bar():
    print('in the bar')

def test1(func):
    print(func)
#test1(bar)   #>>><function bar at 0x000000000234CA60>
    func()
test1(bar)   #>>>function bar at 0x000000000234CA60>    in the bar
'''
import time
def bar():
    time.sleep(3)
    print('in the bar')

def test1(func):
    start_time = time.time()
    func()  #运行的是bar函数
    stop_time = time.time()
    print("the func run time is %s" %(stop_time-start_time))
test1(bar)






