#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-04 20:54:45
# @Author  : flying

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

DATABASE = {
    'engine':'file_storage', #支持mysql、postgresql
    'name':'accont',
    'path':'%s/db'%base_dir
}



