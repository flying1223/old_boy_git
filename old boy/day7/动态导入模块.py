#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-22
# Author   : flying



modname = "lib.aa"


# import lib
# mod = __import__('lib.aa')  #lib
# obj = mod.aa.C()
# print(obj.name)


import importlib    #官方建议使用的方法

mod = importlib.import_module("lib.aa")

obj = mod.C()
print(obj.name)

assert type(obj.name) is str
print('fff')










