#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-12 19:39:23
# @Author  : flying
#包：用来从逻辑上组织模块的，本质就是一个目录（必须带有一个__init__.py文件）

'''
import module_alex
#import本质 导入模块的本质就是把Python文件解释一遍
#相当于module_alex = module_alex中的所有代码
#import module_1,module_2   #导入多个模块 不建议

print(module_alex.name)
module_alex.say_hello()
module_alex.logger()
'''
'''
from module_alex import *  #导入这个模块所以代码
# from module_alex import module_1,module_2
say_hello()
logger()
running()
'''
'''
from module_alex import logger

def logger():
    print('in the main')    #覆盖了module_alex中的logger函数

logger()    #>>>in the main
'''

from module_alex import logger as logger_alex

def logger():
    print('in the main')

logger()
logger_alex()