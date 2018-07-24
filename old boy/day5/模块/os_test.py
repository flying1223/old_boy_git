#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-24 20:26:26
# @Author  : flying
import os
#获取当前目录
print(os.getcwd())  #>>>D:\77old_boy\old boy\day5\模块
#切换目录
os.chdir('D:\\77old_boy\\old boy\\day5')
print(os.getcwd())  #>>>D:\77old_boy\old boy\day5
os.chdir(r'D:\77old_boy\old boy\day5\模块')
print(os.getcwd())  #>>>D:\77old_boy\old boy\day5\模块
#返回当前目录
print(os.curdir)    #>>>.
#获取当前目录的父目录字符串名
print(os.pardir)    #>>>..
#可生成多层递归目录
os.makedirs(r'D:\a\b')
#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推     作用：清理空文件夹的
os.removedirs(r'D:\a\b')
#生成单级目录；相当于shell中mkdir dirname
os.mkdir(r'D:\f')
#删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.rmdir(r'D:\f')
#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.listdir(r'\77old_boy\old boy'))    #>>>['day1', 'day2', 'day3', 'day4', 'day5']
print(os.listdir('.'))  #>>>['os_test.py', 'random_test.py', 'random_验证码.py', 'time_test.py', '__pycache__']
#os.remove()  删除一个文件
#os.rename("oldname","newname")  重命名文件/目录
#获取文件/目录信息
print(os.stat(r'os_test.py'))
#输出操作系统特定的路径分隔符
print(os.sep)   #>>>\
#输出当前平台使用的行终止符
print(os.linesep)   #>>>\r\n
#输出用于分割文件路径的字符串
print(os.pathsep)   #>>>;
#获取系统环境变量
print(os.environ)
#输出字符串指示当前使用平台  win->'nt'; Linux->'posix'
print(os.name)  #>>>nt
#运行shell命令，直接显示
print(os.system('dir'))
#返回path规范化的绝对路径
print(os.path.abspath(__file__))    #>>>D:\77old_boy\old boy\day5\模块\os_test.py
#将path分割成目录和文件名二元组返回
print(os.path.split(r'D:\a\b\c\f.txt')) #>>>('D:\\a\\b\\c', 'f.txt')
#返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname(r'D:\a\b\c\f.txt'))   #>>>D:\a\b\c
#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.basename(r'D:\a\b\c\f.txt'))   #>>>f.txt
#如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(r'D:\f\f'))    #>>>False
#如果path是绝对路径，返回True
print(os.path.isabs(r'D:\a\b\c\f.txt')) #>>>True
#如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile(r'D:\77old_boy\old boy\day5\模块\os_test.py'))   #>>>True
#如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(r'D:\77old_boy\old boy\day5\模块\os_test.py'))    #>>>False
#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join(r'D:',r'\a.txt'))    #>>>D:\a.txt
#返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime(r'D:\77old_boy\old boy\day5\模块\os_test.py')) #>>>1532438565.369549
#返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime(r'D:\77old_boy\old boy\day5\模块\time_test.py')) #>>>1532000198.4529188




