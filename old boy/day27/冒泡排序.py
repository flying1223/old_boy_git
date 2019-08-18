#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-18
# @Author  : flying
import random
import time

# 装饰器
def cal_time(func):
    def wrapper(*args,**kwargs):
        ti = time.time()
        x = func(*args,**kwargs)
        ti2 = time.time()
        print('%s Time cost: %s secs' %(func.__name__,ti2 - ti))
        return x
    return wrapper

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

# 优化
@cal_time
def bubble_sort_2(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if not exchange:
            break


data = list(range(10))
#data_2 = list(range(100))

random.shuffle(data)
bubble_sort(data)
bubble_sort_2(data)
#bubble_sort_2(data_2)


