#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-05 21:08:27
# @Author  : flying
import os

from core import db_handler
from conf import settings
from core import logger
import json

import time

def acc_auth(account,password):
    '''
    帐户验证功能
    :return:
    '''
    db_path = db_handler.dbhandler(settings.DATABASE)
    account_file = '%s/%s.json'%(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_file['expire_data'],"%Y-%m-%d"))
                if time.time()>exp_time_stamp:
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else:
                    return account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)

def acc_login(user_data,log_obj):
    '''
    帐户登录功能
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count <3:
        account = input("\003[32;1maccount:\003[0m").strip()
        password = input("\003[32;1mpassword:\003[0m").strip()
        auth = acc_auth(account,password)
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
    else:
        log_obj.error('account [%s] too many login attempts'% account)
        exit()



