#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 20:27:27
# @Author  : flying

#嵌套函数  在一个函数体内声明另一个函数
'''
def foo():
    print('in the foo')
    def bar():
        print('in the bar')

    bar()
foo()
'''

x = 0
def grandpa():
    x=1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()
