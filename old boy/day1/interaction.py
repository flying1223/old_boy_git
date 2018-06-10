#!/usr/bin/Python
# -*- coding: utf-8 -*-
# Author：flying

name = input("请输入你的名字：")
sex = input("请输入你的性别：")
tel = int(input("请输入你的电话："))


info = '''
------ info of %s------
name = %s
sex = %s
tel = %d
'''%(name,name,sex,tel)


info2 = '''
------ info2 of {_name}------
name = {_name}
sex = {_sex}
tel = {_tel}
'''.format(_name=name,
           _sex=sex,
           _tel=tel)

print(info2)