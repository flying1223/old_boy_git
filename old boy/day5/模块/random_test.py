#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-19 20:03:20
# @Author  : flying
#随机模块
import random
#随机0-1的数字
print(random.random())  #>>>0.18196703915163215
#指定区间
print(random.uniform(1,2))  #>>>1.047793685709734
#随机整数
print(random.randint(0,10)) #>>>7   [0,10]
print(random.randrange(0,10)) #>>>7 [0,9]
#随机序列中的元素(str，list，tuple)
print(random.choice('flying'))
print(random.choice([1,2,3]))
print(random.choice(('tuple',1,2,3)))
print(random.sample('hello',3)) #>>>['h', 'o', 'e'] 取3个序列中的元素
#洗牌
l = [1,2,3,4,5]
random.shuffle(l)
print()    #>>>[2, 5, 1, 4, 3]


