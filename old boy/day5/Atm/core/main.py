#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 20:55:05
# @Author  : flying
import logger

#access logger
access_logger = logger.logger('access')

#临时帐户数据，仅将数据保存在内存中
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

def run():
    '''
    当程序启动时，这个函数将被调用，这里处理用户交互的东西
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)


