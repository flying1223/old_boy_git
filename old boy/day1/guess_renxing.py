#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-09 17:29:00
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
	if count == 3:
		countine_confirm = input("do you want to keep guessing...?")
		if countine_confirm != 'n':
			count = 0 
