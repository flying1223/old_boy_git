#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 19:55:30
# @Author  : flying

#只dumps一次、只loads一次

import json

f = open('test.txt','r')



data = json.loads(f.read()) #>>>flying
print(data) #json.decoder.JSONDecodeError: Extra data: line 1 column 30 (char 29)


