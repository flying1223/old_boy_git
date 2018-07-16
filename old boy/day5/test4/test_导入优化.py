#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-16 20:58:32
# Author   : flying
'''
次方法效率较低，需要重复找到module_test文件
import module_test

def logger():
    module_test.test()
    print('in the logger')

def search():
    module_test.test()
    print('in the search')

logger()
search()
'''
#此方法效率高
from module_test import test

def logger():
    test()
    print('in the logger')

def search():
    test()
    print('in the search')

logger()
search()
