#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# Author   : flying

'''
python3经典类和新式类都是广度优先  B——C——A
python2经典类是深度优先  B——A——C 新式类是按官渡优先B——C——A
'''

class A:

    def __init__(self):
        print('A')

class B(A):

    def __init__(self):
        print('B')
class C(A):

    def __init__(self):
        print('C')

class D(B,C):
    pass

    # def __init__(self):
    #     print('D')

m = D()













