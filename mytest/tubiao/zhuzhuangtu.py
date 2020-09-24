#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2020-09-14
# Author   : flying

from pyecharts import Bar #导入bar模块

attr = ["音响", "电视", "相机", "Pad", "手机", "电脑"] #设置x轴数据
v1 = [5, 20, 36, 10, 75, 90] #第一组数据
v2 = [10, 25, 8, 60, 20, 80] #第二组数据
bar = Bar("1.1.柱状图数据堆叠示例","我是副标题") #实例一个柱状图#
bar.use_theme("macarons")  # 指定图表显示的主题风格，后面会讲
bar.add("京东", attr, v1, mark_point=['average'], is_stack=True) #用add函数往图里添加数据并设置is_stack为堆叠
bar.add("淘宝", attr, v2, mark_point=['max'], is_stack=True) #mark_point标记min,max,average, mark_line标记线

bar.render("1.1.柱状图数据堆叠示例.html") #保存为html类型






