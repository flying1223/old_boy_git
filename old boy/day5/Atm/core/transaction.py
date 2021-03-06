#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-10 20:33:10
# @Author  : flying

from conf import settings
from core import accounts
from core import logger

def make_transaction(log_obj,account_data,tran_type,amount,**others):
    '''
    处理所有用户交易
    :param log_obj:
    :param account_data:
    :param tran_type:
    :param amount:
    :param others:
    :return:
    '''
    amount = float(amount)
    if tran_type in settings.TRANSCTION_TYPE:

        interest = amount*settings.TRANSCTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSCTION_TYPE[tran_type]['action]' == 'plus':
            new_balance = old_balance + amount +interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0 :
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s], your current balance is
                [%s]''' %(account_data['credit'],(amount + interest), old_balance ))
                return
        account_data['balance'] = new_balance
        accounts.dump_account(account_data)
        log_obj.info("account:%s   action:%s    amount:%s   interest:%s" %
                          (account_data['id'], tran_type, amount,interest))
        return account_data
    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)




