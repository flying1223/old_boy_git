#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 16:29:07
# @Author  : flying

#msg = "喜欢一个人"
msg = "肝病防治"
msg_1 = msg.encode(encoding='utf-8')
msg_2 = msg_1.decode(encoding='utf-8')

print(msg_1,msg_2)