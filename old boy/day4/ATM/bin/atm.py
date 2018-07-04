#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 20:54:22
# @Author  : flying

import os
import sys
# print(__file__) #相对路径>>>D:/77old_boy/old boy/day4/ATM/bin/atm.py
# print(os.path.abspath(__file__))    #返回绝对路径>>>D:\77old_boy\old boy\day4\ATM\bin\atm.py
#print(os.path.dirname(os.path.abspath(__file__)))   #dirname返回目录名不要文件名>>>D:\77old_boy\old boy\day4\ATM\bin
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #>>>D:\77old_boy\old boy\day4\ATM

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)   #添加环境变量
#print(sys.path)     #>>>['D:\\77old_boy\\old boy\\day4\\ATM\\bin', 'D:\\77old_boy', 'D:\\python\\python36.zip',
#  'D:\\python\\DLLs', 'D:\\python\\lib', 'D:\\python', 'D:\\python\\lib\\site-packages',
# 'D:\\python\\lib\\site-packages\\easygui-0.98.0_unreleased-py3.6.egg', 'D:\\77old_boy\\old boy\\day4\\ATM']

from conf import settings
from core import main

main.login()


