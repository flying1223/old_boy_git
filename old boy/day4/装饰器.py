#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-26 19:47:41
# @Author  : flying
'''
装饰器：本质是函数，{装饰其他函数）就是为其他函数添加附加功能
原则：1.不能修改被装饰的函数的源代码
    2.不能修改被装饰的函数的调用方式
实现装饰器的知识储备
1.函数即“变量”   2.高阶函数  3.嵌套函数      高阶函数+嵌套函数=》装饰器
'''

'''
def logger():
    print("logging")

def test1():
    pass
    logger()

def test2():
    pass
    logger()

test1()
test2()
'''

# test3()
# def test3():
#     print("this is test3")
#报错》》》name 'test3' is not defined    在调用test3函数的时候，test3未定义   必须先定义，在调用