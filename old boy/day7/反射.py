#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-16
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

if hasattr(d,choice):
    func = getattr(d,choice)
    func("包子")
else:
    setattr(d,choice,bulk)  #相当于d.talk = bulk

    d.talk(d)
'''
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

if hasattr(d,choice):
    attr = getattr(d,choice)
    setattr(d,choice,'fff')
else:
    setattr(d,choice,None)
print(d.name)

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

if hasattr(d,choice):
    delattr(d,choice)   #删除属性
else:
    setattr(d,choice,None)
print(d.name)












