#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 19:04:01
# @Author  : flying

priduct_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120),
]
shoping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
#        for item in priduct_list:
#            print(priduct_list.index(item),item)
        for index,item in enumerate(priduct_list):
            print(index,item)
        user_choice = input("选择要买啥：》》》:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(priduct_list) and user_choice >= 0:
                p_item = priduct_list[user_choice]
                if p_item[1] <= salary:#买的起
                    shoping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦 \033[0m" %salary)
            else:
                print("product code [%s] is not exist!" %user_choice)

        elif user_choice == 'q':
            print("-------shopping list-------")
            for p in shoping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print("请输入数字:")
else:
    print(">>>工资请输入数字！")




