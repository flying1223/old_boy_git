#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-02 19:34:47
# @Author  : flying

from collections import Iterable

print(isinstance([],Iterable))  #>>>True
print(isinstance('abc',Iterable))   #>>>True
print(isinstance('{}',Iterable))    #>>>True
print(isinstance(100,Iterable))     #>>>False

#可以直接作用于for循环的对象统称为可迭代的对象：Iterable
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#
from collections import Iterator

print(isinstance((x for x in range(5)),Iterator))   #>>>True    生成器一定是迭代器  迭代器不一定是生成器

a = [1,2,3]
print(isinstance(a,Iterator))   #>>>False
b=iter(a)   #通过iter方法变成迭代器
print(isinstance(b,Iterator))   #>>>True
print(b.__next__())
print(b.__next__())
print(b.__next__())
