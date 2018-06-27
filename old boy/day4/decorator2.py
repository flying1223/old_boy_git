#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 20:26:49
# @Author  : flying

'''
1.把一个函数名当作实参传给另一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
2.返回值中包含函数名
3.嵌套函数
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
'''
#把一个函数名当作实参传给另一个函数
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
'''
import time
def bar():
    time.sleep(3)
    print('in the bar')

def test2(func):
    print(func)
    return func

#print(test2(bar))  #>>><function bar at 0x000000000230CA60>    <function bar at 0x000000000230CA60>
#t = test2(bar)
# print(t)          #>>><function bar at 0x000000000230CA60>    <function bar at 0x000000000230CA60>
#t()                 #运行bar函数>>><function bar at 0x000000000291CA60>    in the bar

bar = test2(bar)
bar()



