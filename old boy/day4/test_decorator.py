#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 18:15:55
# @Author  : flying
import time

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("run time %s" %(stop_time - start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print("in the test1")

@timer  ##-->test1 = timer(test1)  = deco    test2(name) = deco(name)
def test2(name,age):
    time.sleep(2)
    print("my %s %s"%(name,age))

test1()
test2("flying",18)



