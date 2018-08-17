#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-16
# Author   : flying

def bulk(self):
    print("%s is yelling...")

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
    setattr()













