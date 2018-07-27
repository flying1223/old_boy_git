#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-27 21:12:32
# @Author  : flying

import sys
# 命令行参数List，第一个元素是程序本身路径
print(sys.argv) #>>>['D:/77old_boy/old boy/day5/模块/sys_模块.py']
#获取Python解释程序的版本信息
print(sys.version)  #>>>3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
#返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path) #>>>['D:\\77old_boy\\old boy\\day5\\模块', 'D:\\77old_boy', 'D:\\python\\python36.zip', 'D:\\python\\DLLs', 'D:\\python\\lib', 'D:\\python', 'D:\\python\\lib\\site-packages', 'D:\\python\\lib\\site-packages\\easygui-0.98.0_unreleased-py3.6.egg']
#返回操作系统平台名称
print(sys.platform) #>>>win32

print(sys.stdout.write('please:'))  #>>>please:7


