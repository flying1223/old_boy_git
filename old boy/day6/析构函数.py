#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-06
# Author:flying

class Role(object):

    def __init__(self,name,role,weapon,life_value=100,money=15000):

        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def __del__(self):  #析构函数   在实例释放、销毁的时候执行，通常用于做一些收尾工作
        print("%s 彻底死了。。。" %self.name)

    def shot(self): #类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("%s ah...,i got shot..."%self.name)

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))


r1 = Role('jack',"police","ak47")

r1.buy_gun("AK")
r1.got_shot()

r2 = Role('tom',"terrorist","qiang")
r2.got_shot()
'''
程序结束收尾

jack just bought AK
jack ah...,i got shot...
tom ah...,i got shot...
jack 彻底死了。。。
tom 彻底死了。。。
'''

r3 = Role('alex',"police","ak47")
r3.got_shot()
del r3
'''
实例释放收尾

jack just bought AK
jack ah...,i got shot...
tom ah...,i got shot...
alex ah...,i got shot...
alex 彻底死了。。。
jack 彻底死了。。。
tom 彻底死了。。。
'''





