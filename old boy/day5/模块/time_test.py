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

#元组（struct_time）共九个元素
print(time.localtime()) #>>>UTC+8时区time.struct_time(tm_year=2018, tm_mon=7, tm_mday=17, tm_hour=20, tm_min=43, tm_sec=6, tm_wday=1, tm_yday=198, tm_isdst=0)

#睡几秒
#time.sleep(1)

#时间戳==>元组
print(time.gmtime())    #>>>转换UTC时区，和北京差8小时time.struct_time(tm_year=2018, tm_mon=7, tm_mday=17, tm_hour=12, tm_min=52, tm_sec=28, tm_wday=1, tm_yday=198, tm_isdst=0)

x = time.localtime()
print(x.tm_year)    #>>>2018

#元组==>时间戳
print(time.mktime(x))   #>>>1531833116.0

#格式化的时间字符串
#元组==>格式化字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",x)) #>>>2018-07-19 19:14:04

#格式化字符串==>元组
print(time.strptime("2018-07-19 19:14:04","%Y-%m-%d %H:%M:%S")) #>>>time.struct_time(tm_year=2018, tm_mon=7, tm_mday=19, tm_hour=19, tm_min=14, tm_sec=4, tm_wday=3, tm_yday=200, tm_isdst=-1)

#元组==>str
print(time.asctime())   #>>>Thu Jul 19 19:25:58 2018

#时间戳==>str
print(time.ctime()) #>>>Thu Jul 19 19:25:58 2018


import datetime

print(datetime.datetime.now())  #>>>2018-07-19 19:31:52.285304

print(datetime.datetime.now()+datetime.timedelta(3))    #>>>2018-07-19 19:31:52.285304  三天后
print(datetime.datetime.now()+datetime.timedelta(-3))    #>>>2018-07-16 19:31:52.285304  三天前
print(datetime.datetime.now()+datetime.timedelta(hours = 3))    #>>>2018-07-16 22:31:52.285304  三小时后
print(datetime.datetime.now()+datetime.timedelta(hours = -3))    #>>>2018-07-16 16:31:52.285304  三小时前




