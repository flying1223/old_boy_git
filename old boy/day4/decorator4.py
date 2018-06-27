#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 20:38:59
# @Author  : flying

import time

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print('the func run time %s' %(stop_time-start_time))
    return deco
@timer  #-->test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")
@timer  #-->test2 = timer(test2)  = deco    test2(name) = deco(name)
def test2(name,age):
    time.sleep(3)
    print("test2:",name,age)

# test1 = timer(test1)
# test2 = timer(test2)

test1()
test2("flying",18)
