#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-18
# @Author  : flying

class FlyException(Exception):
    def __init__(self,msg):
        self.message = msg


try:
    raise FlyException('我的异常')

except FlyException as e:
    print(e)






















