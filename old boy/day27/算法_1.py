#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06- 
# @Author  : flying

'''
递归函数
1.
调用自身
2.
结束条件
'''

# 非递归函数，调用无穷
'''
def func1(x):
    print(x)
    func1(x-1)

x = int(input('请输入数字：'))
func1(x)
'''
# 非递归函数，调用无穷
'''
def func2(x):
    if x > 0 :
        print(x)
        func2(x+1)
x = int(input('请输入数字：'))
func2(x)
'''


# def func3(x):
#     if x > 0:
#         print(x)
#         func3(x-1)
# x3 = int(input('请输入x3数字：'))
# func3(x3)


def func4(x):
    if x > 0:
        func4(x - 1)
        print(x)
x4 = int(input('请输入x4数字：'))
func4(x4)




