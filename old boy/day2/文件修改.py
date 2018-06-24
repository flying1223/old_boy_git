#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 13:55:47
# @Author  : flying
f = open("yesterday_2","r")
f_new = open("yesterday_2.bak","w")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等flying享受")
    f_new.write(line)
f.close()
f_new.close()

'''
import sys
f = open("yesterday_2","r")
f_new = open("yesterday_2.bak","w")

find_str = sys.argv[1]
replace_str = sys.argv[2]
for line in f:
    if "find_str" in line:
        line = line.replace("find_str","replace_str")
    f_new.write(line)
f.close()
f_new.close()
'''





