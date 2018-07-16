#!/usr/bin/Python
# -*- coding: utf-8 -*-
# Author:flying

print("from package_test")

#import test1    #test1 = 'test1.py all code'.test1()   此方法不可用

from  . import test1    #从当前目录下导入test1
