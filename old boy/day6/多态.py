#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-08
# Author   : flying

class Animal(object):

    def __init__(self,name):
        self.name = name

    def talk(self):
        pass
        #raise NotImplementedError("Subclass must implement abstract meth")

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):

    def talk(self):
        print("%s Meow!"%self.name)

class Dog(Animal):

    def talk(self):
        print("%s woof! woof!"%self.name)
'''
def animal_talk(obj):
    obj.talk()
'''
d = Dog('tom')
#d.talk()

c = Cat('jack')
#c.talk()

Animal.animal_talk(c)
Animal.animal_talk(d)








