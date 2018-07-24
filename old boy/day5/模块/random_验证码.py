#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-24 20:09:11
# @Author  : flying

import random

'''
checkcode = ''
for i in range(4):
    current = random.randint(1,9)
    checkcode += str(current)

print(checkcode)    #>>>7924
'''
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)

    checkcode += str(tmp)
print(checkcode)



