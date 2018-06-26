#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-26 20:14:16
# @Author  : flying

# def foo():
#     print('in the foo')
#     bar()
#
# foo()       #报错》》》NameError: name 'bar' is not defined

# def bar():
#     print('in the bar')
#
# def foo():
#     print('in the foo')
#     bar()
#
# foo()  #>>>in the foo in the bar

# def foo():
#     print('in the foo')
#     bar()
# def bar():
#     print('in the bar')
# foo()   #>>>in the foo in the bar

def foo():
    print('in the foo')
    bar()
foo()
def bar():
    print('in the bar')  #>>>NameError: name 'bar' is not defined