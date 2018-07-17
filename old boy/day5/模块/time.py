#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-17 20:09:14
# @Author  : flying
'''
模块分为内置模块、开源模块、自定义模块
'''
#内置模块 time与datatime

#时间戳
import time
print(time.time())  #>>>1531829590.1815534  时间戳

#格式化的时间字符串

#元组（struct_time）共九个元素
print(time.localtime()) #>>>UTC+8时区time.struct_time(tm_year=2018, tm_mon=7, tm_mday=17, tm_hour=20, tm_min=43, tm_sec=6, tm_wday=1, tm_yday=198, tm_isdst=0)

#睡几秒
#time.sleep(1)

#时间戳==>元组
print(time.gmtime())    #>>>转换UTC时区，和北京差8小时time.struct_time(tm_year=2018, tm_mon=7, tm_mday=17, tm_hour=12, tm_min=52, tm_sec=28, tm_wday=1, tm_yday=198, tm_isdst=0)

x = time.localtime()
print(x.tm_year)    #>>>2018
print(time.mktime(x))   #>>>1531833116.0

