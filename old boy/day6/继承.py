#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-06
# Author:flying

class People(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." %self.name)

    def talk(self):
        print("%s is talking..." %self.name)

    def sleep(self):
        print("%s is slepping..." %self.name)

class Man(People):

    def piao(self):
        print("%s is piaoing...2h...done" %self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(People):

    def get_birth(self):
        print("%s is born a boby..." %self.name)

m1 = Man('cuzn',18)
m1.eat()
m1.piao()
m1.sleep()

w1 = Woman("flying","17")
w1.get_birth()










