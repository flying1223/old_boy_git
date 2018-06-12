#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-11 21:27:17
# @Author  : flying

salay = int(input("请输入你的工资："))
shop_list = [[1,'Iphone',5800],[2,'Mac Pro',12000],[3,'Starbuck Latte',31],[4,'Alex python',81],[5,'Bike',800]]
bought_list = []
q =str()
while True :
    for i in shop_list:
        print("商品：",i)
    num = input("请输入想要购买商品的编号：")
    if num == 'q':
        break
    num = int(num) - 1
    merchandise_prize = shop_list[num][2]
    if salay >= merchandise_prize:
        print("add %s to your shopping cart" %shop_list[num][1])
        bought_list.append(shop_list[num][1])
        salay = salay - merchandise_prize
    else:
        print("你的余额不足，请重新挑选！")

print("you have bought %s" %bought_list)













