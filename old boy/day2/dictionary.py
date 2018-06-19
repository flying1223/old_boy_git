#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-14 19:28:30
# @Author  : flying

#key=>>value
info = {
    'stu1101':"Zhangsan",
    'stu1102':'Lisi',
    'stu1103':'Wangwu',
    'stu1106':'Flying'
}

print(info)
print(info["stu1102"])   #查找value>>>Lisi
info["stu1102"] = "李四"
print(info)          #修改value>>>{'stu1101': 'Zhangsan', 'stu1102': '李四', 'stu1103': 'Wangwu'}
info["stu1104"] = "马六"
print(info)          #增加key-value>>>{'stu1101': 'Zhangsan', 'stu1102': '李四', 'stu1103': 'Wangwu', 'stu1104': '马六'}
del info['stu1101']
print(info)        #删除key-value>>>{'stu1102': '李四', 'stu1103': 'Wangwu', 'stu1104': '马六'}
info.pop("stu1102")   #标准删除
print(info)        #删除key-value>>>{'stu1103': 'Wangwu', 'stu1104': '马六'}
info.popitem()
print(info)       #随机删除key-value>>>{'stu1103': 'Wangwu'}

print(info.get('stu1103'))  #查找》》》Wangwu or None
print("stu1105" in info)   #判断是否在字典里》》》False   info.has_key("stu1105") python2
print(info.items())  #把字典转换成列表》》》dict_items([('stu1103', 'Wangwu'), ('stu1106', 'Flying')])
print("---------------------------")
c = dict.fromkeys([8,9,10],"fly")  #初始化一个新的字典》》》{8: 'fly', 9: 'fly', 10: 'fly'}
print(c)

b = {
    "stu1103":5,
    2:4,
    6:8,
}
info.update(b) #两个字典合并，有重合的key把value覆盖》》》{'stu1103': 5, 'stu1106': 'Flying', 2: 4, 6: 8}
print(info)

for i in info:
    print(i,info[i]) #此方法比较高效         stu1103 5    stu1106 Flying    2 4    6 8

print("------------------")

for k,v in info.items():
    print(k,v)             #stu1103 5    stu1106 Flying    2 4    6 8





