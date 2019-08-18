#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-18
# @Author  : flying

import time
import random


# 装饰器
def cal_time(func):
    def wrapper(*args,**kwargs):
        ti = time.time()
        x = func(*args,**kwargs)
        ti2 = time.time()
        print('Time cost:',func.__name__,ti2 - ti)
        return x
    return wrapper

def random_list(n):
    result = []
    ids = list(range(1001,1001+n))
    a1 = ['赵','钱','孙','李','宋']
    a2 = ['丽','强','飞','','晓']
    a3 = ['梦','天','鑫','田','国','安','成','飞']
    for i in range(n):
        age = random.randint(18,60)
        id = ids[i]
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)
        dir = {'id':id,'name':name,'age':age}
        result.append(dir)
    return result

random_list(6)

@cal_time
def bin_search(data_set,val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid]['id'] == val:
            print(data_set[mid]['id'])
            return mid
        elif data_set[mid]['id'] < val:
            low = mid + 1
        else:
            high = mid - 1
    return

data = random_list(6)
bin_search(data,1002)