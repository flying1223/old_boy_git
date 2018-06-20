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
print(list_1 & list_2)
#并集
print(list_1.union(list_2))#>>>{0, 1, 2, 3, 4, 5, 6, 7, 66, 9, 8, 22}
print(list_1 | list_2)
#差集
print(list_1.difference(list_2))#1有2没有》》》{1, 3, 5, 7, 9}
print(list_1 - list_2)
#子集
l3 = [1,3,7]
list_3 = set(l3)
print(list_1.issubset(list_2)) #>>>False
print(list_3.issubset(list_1)) #>>>True

#父集
print(list_1.issuperset(list_2)) #>>>False
print(list_1.issuperset(list_3)) #>>>True

#对称差集
print(list_1.symmetric_difference(list_2)) #吧交集抠出去》》》{0, 1, 2, 66, 3, 5, 7, 8, 9, 22}
print(list_1 ^ list_2)

l4 = [5,6,8]
list_4 = set(l4)
print(list_3.isdisjoint(list_4))#没有交集返回True 》》》True
print(list_3.isdisjoint(list_1))#没有交集返回True 》》》False
print('---------')

#增
l7 = [1,4,5,7,3,6,7,9]
list_7 = set(l7)
list_7.add(999)
list_7.update([888,777,555])
print(list_7) #>>>{1, 3, 4, 5, 6, 7, 999, 9, 777, 555, 888}

#使用remove()删除一项
list_7.remove(999)
print(list_7) #>>>{1, 3, 4, 5, 6, 7, 9, 777, 555, 888}

print(len(list_7)) #长度》》》10

print(777 in list_7) #判断777是否在集合中》》》True

print(0 not in list_7) #判断0不在集合中》》》True

print(list_7.pop())  #删除任意的
print(list_7)

#list_7.remove(000) 删除，remove删除不存在的元素会报错，discard不会报错
list_7.discard(000)


