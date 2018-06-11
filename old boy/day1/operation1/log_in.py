#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-09 18:22:57
# @Author  : flying

dict_username = {}
dict_locking = {}
list = []
with open('C://Users//My//Desktop//old boy//day1//operation1//文件//username.txt','r') as f:
	for line in f:
		(key, value) = line.strip().split(':') 
		dict_username[key] = value 

with open('C://Users//My//Desktop//old boy//day1//operation1//文件//locking.txt','r') as f:
	list=(f.read().strip().split('\n'))
	dict_locking = set(list)

while True:
	username = input("请输入用户名称：")
	if username not in dict_username:
		print("您输入的用户名不存在，请重新输入...")
	elif username in dict_locking:
		print("您输入的用户名已被锁定，请重新输入...")
	else:
		count = 0
		while count < 3:
				password = input("请输入密码：")
				if password == dict_username[username]:
					print("恭喜您登录成功！")
					break
					break
				else:
					print("输入有误请重新输入...")
				count += 1
		else:
			with open('C://Users//My//Desktop//old boy//day1//operation1//文件//locking.txt','w') as f:
				f.write(username)
			print("账号已被锁定...")




