#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-09 16:52:49
# @Author  : flying

age_of_oldboy = 56


count = 0
while count < 3:
	guess_age = int(input("guess age:"))
	if guess_age ==age_of_oldboy:
		print("yes,you got it!")
		break
	elif guess_age < age_of_oldboy:
		print("think smaller...")
	elif guess_age > age_of_oldboy:
		print("think bigger...")
	count = count + 1  #count +=1
else:
	print("you have tried too many times..fuck off!")
	
