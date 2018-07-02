#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-29 19:10:03
# @Author  : flying

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("flying")
# c.__next__()   #next只是在调用yield，不传值
# b1 = "韭菜馅"
# c.send(b1)  #调用yield同时传值
# #c.__next__()


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)    #send唤醒并给yield传值   next只唤醒不传值
        c2.send(i)

producer("flying")



