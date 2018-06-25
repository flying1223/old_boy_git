#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-25 19:14:04
# @Author  : flying

#最大递归次数999
'''
递归特性  1、必须有明确条件    2、每次进入更深一层递归是，问题规模相比上一次递归都应该有所减少
3.递归效率不高，层数过多会导致栈溢出
'''
'''
def calc(n):
    print(n)
    return calc(n+1)
calc(0)  '''


def calc(n):
    print(n)
    if int(n/2) >0:
        return calc(int(n/2))
    print(">>>",n)
calc(20)
