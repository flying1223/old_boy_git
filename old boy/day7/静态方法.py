#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-16
# Author   : flying

'''
class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d = Dog("jack")
d.eat("包子")
'''
class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod   #实际上跟类没什么关系，eat只是一个函数，不是类的方法
    def eat(self):
        print("%s is eating %s" %(self.name,'food'))

    def talk(self):
        print("%s is talking..."%self.name)

d = Dog("jack")
d.eat(d)
d.talk()











