#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 19:43:01
# @Author  : flying

import json

def sayhi(name):
    print('hello,',name)

info = {
    'name':'flying',
    'age':18,
}

f = open("test.txt",'w')

f.write(json.dumps(info))
info['age'] = 20
f.write(json.dumps(info))
f.close()







