#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2020-09-14
# Author   : flying

from pyecharts import Bar

movieName = ["战狼2","速度","功夫瑜伽","西游伏妖篇","变形金刚5","摔跤吧"]
movieMoney = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96]

print(len(movieName), len(movieMoney))
bar1 = Bar(title="某年内地电影票房前20的电影", subtitle="这是一个子标题")
# 添加图表的数据, 或者配置信息
bar1.add("电影信息",movieName, movieMoney)

# 默认情况下会生成一个render.html文件
bar1.render()






