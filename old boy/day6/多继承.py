#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-07
# Author   : flying


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

class Relation(object):

    def make_friends(self,obj):
        print("%s is making friends with %s" %(self.name,obj.name))

class Man(People,Relation):

    def __init__(self,name,age,money):

        super(Man,self).__init__(name,age)
        self.money = money
        print("%s 一出生就有%s money" %(self.name,self.money))

    def piao(self):
        print("%s is piaoing...2h...done" %self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(People,Relation):   #执行第一个类的构造函数，第二个就不执行了，如果第一个没有，则执行第二个

    def get_birth(self):
        print("%s is born a boby..." %self.name)

m1 = Man('cuzn',18,10)


w1 = Woman("flying","17")

m1.make_friends(w1)









