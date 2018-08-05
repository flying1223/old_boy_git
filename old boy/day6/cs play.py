#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-05
# @Author  : flying

class Role(object):
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        '''
        构造函数
        在实例化是做了一些类的初始化的工作

        '''
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,i got shot...")

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))

r1 = Role("alex","police","ak47")       #把一个类变成一个距离对象的过程 实例化（初始化一个类，造了一个对象）
r2 = Role("jack","terrorist","B22")     #实例化（初始化一个类，造了一个对象）

r1.buy_gun("ak47")
















