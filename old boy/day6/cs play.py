#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-05
# @Author  : flying

class Role(object):
    n = 123 #类变量 存在类的内存里
    n_list = []
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        '''
        构造函数
        在实例化是做了一些类的初始化的工作

        '''
        self.name = name    #实例变量（静态属性），作用域就是实例本身
        self.role = role    #相当于r1.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self): #类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,i got shot...")

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))

r1 = Role("alex","police","ak47")  #把一个类变成一个距离对象的过程 实例化（初始化一个类，造了一个对象）
#相当于Role(r1,"alex","police","ak47")
r1.buy_gun("ak47")  #相当于Role.buy_gun(r1)    >>>alex just bought ak47
r1.bullet_prove = True  #新加的属性只用于r1
print(r1.n,r1.name,r1.bullet_prove) #>>>123 alex True
print(r1.weapon)
del r1.weapon   #删除属性
#print(r1.weapon)   #>>>'Role' object has no attribute 'weapon'
r1.name = 'flying'  #修改属性

r1.n = '修改类变量'
#在r1的内存中加了一个 n = '修改类变量'
print('r1:',r1.n,r1.name) #>>>r1: 修改类变量 flying
r1.n_list.append("from r1")
print(r1.n_list)    #>>>['from r1']


r2 = Role("jack","terrorist","B22")     #实例化（初始化一个类，造了一个对象）
r2.n_list.append("from r2")

print(r2.n_list)    #>>>['from r1', 'from r2']

print(Role.n)   #>>>123
print('r2:',r2.n,r2.name) #>>>r2: 123 jack

Role.n = "FLY"
print(Role.n,r1.n,r2.n) #>>>FLY 修改类变量 FLY













