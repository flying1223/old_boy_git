#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 14:18:10
# @Author  : flying

import getpass

_username = 'fly'
_password = '123'

user = input("请输入用户名：")
pwd = input("请输入密码：")

if user == _username and pwd == _password:
	print("welcome user %s login" % user)
else:
	print("wrong username or password")

