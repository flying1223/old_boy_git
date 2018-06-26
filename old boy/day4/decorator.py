#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-26 20:01:41
# @Author  : flying

import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return warpper()

@timmer
def test1():
    time.sleep(3)
    print("in the test1")

test1   #书写test1()报错




