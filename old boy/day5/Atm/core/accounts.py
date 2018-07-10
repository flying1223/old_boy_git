#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-10 20:13:23
# @Author  : flying

def load_current_balance(accout_id):
    '''
    返还帐户余额和其他基本信息
    :param accout_id:
    :return:
    '''
    db_path = db_handler.dbhandler(settings.DATABASE)
    accout_file = "%s/%s"%(db_path,accout_id)
    with open(accout_file) as f:
        acc_data = json.load(f)
        return acc_data


