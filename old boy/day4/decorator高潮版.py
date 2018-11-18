#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 21:11:32
# @Author  : flying

user,passwd = 'flying','123'

def auth(auth_type):
    def outer_wapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'local':
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args,**kwargs)
                    return res
                else:
                    exit("\033[32;1mInvalid username or password\033[0m")
            elif auth_type == 'ldap':
                print(">>>666ldap")
        return wrapper
    return outer_wapper


def index():
    print('welcome to index.html_test page')
@auth(auth_type="local")
def home():
    print('welcome to home page')
    return 'from home'
@auth(auth_type = 'ldap')
def bbs():
    print('welcome to bbs page')

index()
#home()
print(home())
bbs()
