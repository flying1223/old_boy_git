#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-18
# Author   : flying

'''
def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s" %(self.name,food))


d = Dog("jack")

choice = input(">>").strip()

getattr(d,choice)

'''

name = ['fly','cuzn']
data = {}

try:
    name[3]
    # data['name']
    #open("t.txt")
    a = 1
    print(a)
except KeyError as e:
    print("没有这个key",e)
except IndexError as e:
    print('列表操作错误',e)
except Exception as e:
    print("未知错误",e)
else:
    print('一切正常')

finally:
    print("不管有没有错都执行")

'''
name = ['fly','cuzn']
data = {}

try:
    name[3]
    data['name']
# except (IndexError,KeyError) as e:
#     print("没有这个key",e)
except Exception as e:
    print("出错了",e)
'''

