#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-09 17:24:39
# @Author  : flying

age_of_oldboy = 56

for i in range(0,3):
	guess_age = int(input("guess age:"))
	if guess_age ==age_of_oldboy:
		print("yes,you got it!")
		break
	elif guess_age < age_of_oldboy:
		print("think smaller...")
	elif guess_age > age_of_oldboy:
		print("think bigger...")
else:
	print("you have tried too many times..fuck off!")