#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 17:37:41
# @Author  : flying
'''
def test1():
    print('in the test1')
    return 0
#    print('test end')  return 后面的语句不会运行
print(test1())
'''
#函数返回值的作用后面的程序可能需要前面函数返回值的结果来进行不同的操作
def test1():
    print('in the test1')

def test2():
    print('in the test2')
    return 0
def test3():
    print('in the test3')
    return 1,'hello',['alex','wupeiqi'],{'name':'alex'}

def test4():
    print('in the test4')
    return test2

def test5():
    print('in the test5')
    return test2()

print(test1())
print(test2())
print(test3())
print(test4())
print(test5())





