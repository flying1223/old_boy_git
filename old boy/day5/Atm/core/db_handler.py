#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-06 20:11:43
# @Author  : flying
'''
处理所有数据库交互
'''
from conf import settings

def file_db_handle(conn_parms):
    '''
    解析db文件路径
    :return:
    '''
    print('file db:',conn_parms)
    db_path = '%s/%s'%(conn_parms['path'],conn_parms['name'])
    return db_path

def db_handler(conn_parms):
    '''
    连接数据库
    :return:
    '''
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)




