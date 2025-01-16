#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 20:55:05
# @Author  : flying
from day5.Atm.core import auth,accounts,transaction
# from core import accounts
# from core import logger
# from core import accounts
# from core import transaction
# from core.auth import login_required
import time


#access logger
access_logger = logger.logger('access')

#临时帐户数据，仅将数据保存在内存中
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}
def repay(acc_data):
    '''
    打印当前余额，让用户偿还账单
    :param acc_data:
    :return:
    '''
    accout_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = '''----------BALANCE INFO--------
        Credit : %s
        Balabce: %s'''%(account_data['credit'],accout_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount)>0 and repay_amount.isdigit():
#            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,accout_data,'repay',repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

            if withdraw_amount == 'b':
                back_flag = True

def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True

def interactive(acc_data):
    '''
    与用户互动
    :param acc_data:
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
         else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    '''
    当程序启动时，这个函数将被调用，这里处理用户交互的东西
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)  #交互


