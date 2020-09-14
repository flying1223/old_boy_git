#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2020-09-07
# Author   : flying

from pyecharts import Bar

# 绘制多个条形图
x_movies_name = ["猩球崛起", "敦刻尔克", "蜘蛛侠", "战狼2"]
y_16 = [15746, 312, 4497, 319]
y_15 = [12357, 156, 2045, 168]
y_14 = [2358, 399, 2358, 362]
bar2 = Bar(title="某年内地电影票房前20的电影", subtitle="子标题")
bar2.add('14号',x_movies_name,y_14)
bar2.add('15号',x_movies_name,y_15)
bar2.add('16号',x_movies_name,y_16)

bar2.render()


