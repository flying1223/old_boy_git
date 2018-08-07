#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-06
# Author:flying

#class People:  经典类
class People(object):   #新式类    多继承上的顺序问题

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
#对构造函数进行重构，添加一个属性
    def __init__(self,name,age,money):

        super(Man,self).__init__(name,age)  #新式类的写法
        #People.__init__(self,name,age)
        self.money = money
        print("%s 一出生就有%s money" %(self.name,self.money))

    def piao(self):
        print("%s is piaoing...2h...done" %self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class Woman(People):

    def get_birth(self):
        print("%s is born a boby..." %self.name)

m1 = Man('cuzn',18,10)
m1.eat()
m1.piao()
m1.sleep()

w1 = Woman("flying","17")
w1.get_birth()










