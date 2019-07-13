#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-09 17:44:42
# @Author  : flying
'''
for i in range(10):
	if i < 3:
		print("loop",i)
	else:
		continue
	print("hehe...")

'''
for i in range(10):
	print('-------',i)
	for j in range(10):
		print(j)
		if j > 5:
			break