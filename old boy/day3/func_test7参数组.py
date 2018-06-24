#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-24 18:33:40
# @Author  : flying
'''
def test(*args):  #可接受多个实参，放在元组中
    print(args)

test(1,2,3,4,5)  #》》》(1, 2, 3, 4, 5)
test(*[1,2,3,4,5,6]) # *args = *[1,2,3,4,5,6]   args = tuple([1,2,3,4,5,6]) >>>(1, 2, 3, 4, 5, 6)
'''
'''
def test1(x,*args): # *args接收n位置参数转换成元组
    print(x)
    print(args)

test1(1,2,3,4,5,6,7) #>>>1    (2, 3, 4, 5, 6, 7)
'''
'''
def test2(**kwargs): #  **kwargs把n个关键字转换成字典
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['sex'])
    print(kwargs['age'])

test2(name='flying',sex='girl',age = 18) #>>>{'name': 'flying', 'sex': 'girl', 'age': 18}
test2(**{'name':'flying','sex':'girl','age' : 18}) #>>>{'name': 'flying', 'sex': 'girl', 'age': 18}
'''
'''
def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('flying',age = 18,sex = 'girl')  #>>>flying   {'age': 18, 'sex': 'girl'}

def test4(name,age = 18,**kwargs):
    print(name)
    print(age)
    print(kwargs)
test4('flying',3,sex = 'girl',hobby = 'tesla')#>>>flying  3   {'sex': 'girl', 'hobby': 'tesla'}
test4('flying',sex = 'girl',hobby = 'tesla',age = 3)#>>>flying  3   {'sex': 'girl', 'hobby': 'tesla'}
'''
def test5(name,age = 18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test5")
def logger(source):
    print("from %s" %source)
test5('flying',age = 3,sex = 'girl',hobby = 'tesla') #>>>flying 3   ()  {'sex': 'girl', 'hobby': 'tesla'}
test5('flying', 3,66,99,sex = 'girl',hobby = 'tesla')#>>>flying 3   (66, 99)    {'sex': 'girl', 'hobby': 'tesla'}
#关键字调用一定在位置参数调用后面
#test5('flying', age=3,66,99,sex = 'girl',hobby = 'tesla') #错误的


