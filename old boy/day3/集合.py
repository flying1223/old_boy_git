#!/usr/bin/Python
# -*- coding: utf-8 -*-
# Author:flying

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

print(list_1,type(list_1))  #>>>{1, 3, 4, 5, 6, 7, 9} <class 'set'>  集合是无序的

l = [2,6,0,66,22,8,4]
list_2 = set(l)
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))#>>>{4, 6}

#并集
print(list_1.union(list_2))#>>>{0, 1, 2, 3, 4, 5, 6, 7, 66, 9, 8, 22}

#差集
print(list_1.difference(list_2))#1有2没有》》》{1, 3, 5, 7, 9}

#子集
l3 = [1,3,7]
list_3 = set(l3)
print(list_1.issubset(list_2)) #>>>False
print(list_3.issubset(list_1)) #>>>True

#父集
print(list_1.issuperset(list_2)) #>>>False
print(list_1.issuperset(list_3)) #>>>True
