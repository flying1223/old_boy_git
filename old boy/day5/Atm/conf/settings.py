#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 20:54:45
# @Author  : flying
import os
import sys
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASE = {
    'engine':'file_storage', #支持mysql、postgresql
    'name':'accont',
    'path':'%s/db'%BASE_DIR
}

TRANSCTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05},
    'consume':{'action':'minus','interest':0},
}

