#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-16
# Author   : flying

class Dog(object):

    def __init__(self,name):
        self.name = name

    @property #属性
    def eat(self):
        print("%s is eating %s" %(self.name,'food'))

    def talk(self):
        print("%s is talking..."%self.name)

d = Dog("jack")
d.eat


class Dog(object):

    def __init__(self,name):
        self.name = name

    @property #属性
    def eat(self):
        print("%s is eating %s" %(self.name,'ddd'))

    @eat.setter
    def eat(self,food):
        print("set to food:",food)

    def talk(self):
        print("%s is talking..."%self.name)

d = Dog("jack")
d.eat
d.eat = '饺子'










