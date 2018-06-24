#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 17:54:15
# @Author  : flying

def test(x,y):  #x,y形参   2,5实参  形参和实参是一一对应 多了少了都不行
    print(x,y)

test(2,5)
test(y=1,x=7)  #关键字调用与形参顺序无关
test(2,y=3)
#test(x=1,3)    #关键字调用一定在位置参数调用后面












