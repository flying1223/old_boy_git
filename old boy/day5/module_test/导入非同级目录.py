#!/usr/bin/Python
# -*- coding: utf-8 -*-
# Author:flying

#import p_test   #>>>ModuleNotFoundError: No module named 'p_test'
import sys,os

print(sys.path)

print(os.path.abspath(__file__))    #>>>D:\77old_boy\old boy\day5\module_test\导入非同级目录.py
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   #>>>D:\77old_boy\old boy\day5
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(dir)
# print(sys.path) #导入到列表的最后一个
sys.path.insert(0,dir)  #导入到列表的第一位
print(sys.path)







