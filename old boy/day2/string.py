#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-13 22:04:03
# @Author  : flying

#name = "flying xiao fei"
name = "i love {name},{time}"
print(name.capitalize()) #首字母大写>>>I love {name},{time}
print(name.count('f')) #统计字母出现的次数#>>>0
print(name.center(50,"-"))#>>>---------------i love {name},{time}---------------
print(name.endswith("ei")) #判断字符串已什么结尾>>>False
print(name.expandtabs(tabsize=30)) #name = "flying \txiao fei"
print(name.find('l')) #字符索引2
print(name[name.find('l'):9])#字符串切片>>>love {n
print(name.format(name='flying',time='forever')) #name = "i love {name},{time}">>>i love flying,forever
print(name.format_map({'name':'flying','time':'forever'}))#name = "i love {name},{time}">>>i love flying,forever
print('flying1223'.isalnum())#包含数字>>>True
print('flying1223'.isalpha())#纯英文字符>>>False
print('1'.isdecimal())#10进制>>>True
print('11'.isdigit())#是否是整数>>>True
print('W11'.isidentifier())#判断是不是一个合法的变量名>>>True
print('W11'.islower())#是否是小写>>>False
print('F77'.isnumeric())#是否是数字>>>False
print('F77'.isspace())#是否是空格>>>False
print('I Love You'.istitle())#是否是title,每个字符第一个字母大写>>>True
print('I Love You'.isprintable())#tty file,drive file不能打印>>>True
print('I Love You'.isupper())#是否全是大写>>>False
print(','.join(['1','2','3']))#>>>1,2,3
print('+'.join(['1','2','3']))#>>>1+2+3
print(name.ljust(50,'*'))#长50，不够用*号补>>>i love {name},{time}******************************
print(name.rjust(50,'*'))#>>>******************************i love {name},{time}
print('FLYing'.lower())#把大写变成小写>>>flying
print('FLYing'.upper())#把小写变成大写>>>FLYING
print('\nflying\n'.lstrip())#从左边去掉空格和回车
print('\nflying\n'.rstrip())#从右边去掉空格和回车
print('\n   flying   \n'.strip())#去掉两边空格和回车
p = str.maketrans('fly','567')#把字符用数字代替    数字加密
print("flying".translate(p))#>>>567ing
print("flying love ".replace('l','f')) #>>>ffying fove
print("flying love ".replace('l','f',1)) #>>>ffying love
print("flying love ".rfind('l')) #从左往右数找到最右边的下标给返回>>>7
print("fly ing love".split())#把字符串按照空格分成一个列表.>>>['flying', 'love']
print("fly ing love".split('l'))#把字符串按照l分成一个列表.>>>['f', 'y ing ', 'ove']
print("fly in\ng love".splitlines())#换行分割>>>['fly in', 'g love']
print("Flying lovE".swapcase())#大小写转换>>>fLYING LOVe
print("flying lovE".title())#每个字符第一个字母变成大写>>>Flying Love
print("flying lovE".zfill(50))#>>>000000000000000000000000000000000000000flying lovE

