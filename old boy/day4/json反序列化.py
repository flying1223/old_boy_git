#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 19:55:30
# @Author  : flying

# import json
#
# f = open('test.txt','r')
#
# # data = f.read()
# # f.close()
# # print(data['name'])   #>>>TypeError: string indices must be integers
# '''
# data = eval(f.read())
# f.close()
# print(data['name'])     #>>>flying
# '''
#
# data = json.loads(f.read()) #>>>flying
# print(data['name'])
import pickle

def sayhi(name):

f = open('test.txt','rb')
data = pickle.loads(f.read())
print(data)
print(data['func']("flying"))