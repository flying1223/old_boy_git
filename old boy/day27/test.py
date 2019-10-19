#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06- 
# @Author  : flying

import random

def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                print(li)
    print('排序后的列表',li)


# data = list(range(10))
# print(data)
# print(len(data))

n = 10
list = []
for i in range(n):
    data2 = random.randint(0,n)
    list.append(data2)
print('生成的随机列表',list)

bubble_sort(list)