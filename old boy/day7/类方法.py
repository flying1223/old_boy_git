#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-16
# Author   : flying

class Dog(object):

    n = 777

    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating %s" %(self.n,'food'))

    def talk(self):
        print("%s is talking..."%self.name)

d = Dog("jack")
d.eat()
d.talk()

















