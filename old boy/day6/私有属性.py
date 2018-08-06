#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-06
# Author:flying

class Role(object):

    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value  #私有属性，只有内部加上一个方法才可以方问
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
    #def __got_shot(self):  #私有方法
        self.__life_value -= 50
        print("ah...,i got shot...")

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))

    def show_status(self):
        print('name:%s weapon:%s life_value:%s' %(self.name,self.weapon,self.__life_value))

r1 = Role('jack',"police","ak47")
r1.got_shot()
r1.show_status()    #>>>name:jack weapon:ak47 life_value:100














