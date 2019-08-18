#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-13
# @Author  : flying
import time

# 装饰器
def cal_time(func):
    def wrapper(*args,**kwargs):
        ti = time.time()
        x = func(*args,**kwargs)
        ti2 = time.time()
        print('Time cost:',func.__name__,ti2 - ti)
        return x
    return wrapper

@cal_time
def bin_search(data_set,val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return


def _binary_search(dataset,find_num):
    #print(dataset)

    if len(dataset) > 1:
        mid = int(len(dataset)/2)
        if dataset[mid] == find_num:
            pass
            #print('找到数字',dataset[mid])
        elif dataset[mid] > find_num:
            #print('\033[31;1m找到的数在mid[%s]左面\033[0m' % dataset[mid])
            return binary_search(dataset[0:mid],find_num)
        else:
            #print('\033[31;1m找到的数在mid[%s]右面\033[0m' % dataset[mid])
            return binary_search(dataset[mid+1:],find_num)
    else:
        if dataset[0] == find_num:
            #print('找到数字了',dataset[0])
            pass
        else:
            pass
            #print('没得分了，要找的数字[%s]不在列表里' % find_num)

@cal_time
def binary_search(dataset,find_num):
    return _binary_search(dataset,find_num)

data = list(range(10000))

bin_search(data,156)
binary_search(data,156)



