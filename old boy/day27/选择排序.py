#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-18
# @Author  : flying

def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in  range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
        




