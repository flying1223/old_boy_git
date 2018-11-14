#!/usr/bin/Python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-27
# Author   : flying

import paramiko

#创建ssh对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='c1.salt.com',port=22,username='fff',password='111')

#执行命令
stdin,stdout,stdeer = ssh.exec_command('df')

#获取命令结果
result = stdout.read()

#关闭连接
ssh.close()