#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 21:11:32
# @Author  : flying

user,passwd = 'flying','123'

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("Username:").strip()
        password = input("Password:").strip()

        if user == username and passwd == password:
            print("\033[32;1mUser has passed authentication\033[0m")
            func(*args,**kwargs)
        else:
            exit("\033[32;1mInvalid username or password\033[0m")
    return wrapper()


def index():
    print('welcome to index page')
@auth
def home():
    print('welcome to home page')
    return 'from home'
@auth
def bbs():
    print('welcome to bbs page')

index()
#home()
print(home())
bbs()
