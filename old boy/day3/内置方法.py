#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-02 20:45:04
# @Author  : flying

print(abs(-5))  #>>>5   取绝对值
print(all([0,-5,3]))    #>>>False   都为真返回为真   print(all([1,2,3]))  >>>True
print(any([0,-5,3]))    #>>>True    有一个为真就是真    print(any([]))  >>>False 为空返回False
print(bin(8))   #>>>0b1000  十进制转二进制
print(bool(0))  #>>>0是False 1是True  [1]{1}是True  []{}是False
a = bytes("flying",encoding='utf-8')
print(a.capitalize(),a)    #>>>b'Flying' b'flying'  字符串不可以修改
b = bytearray("flying",encoding='utf-8')
b[1] = 50
print(b)    #>>>bytearray(b'f2ying')    把二进制变成一个列表的形式并修改




