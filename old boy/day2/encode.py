#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 16:29:07
# @Author  : flying

msg = "喜欢一个人"

#msg = "肝病防治"
msg_1 = msg.encode(encoding='utf-8')
msg_2 = msg_1.decode(encoding='utf-8')

print(msg_1,msg_2)
s = "你好"
s = s.encode("utf-8").decode("gbk") #encode 编码成unicode 之后解码成gbk
print(s,type(s))
