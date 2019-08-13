#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06- 
# @Author  : flying
import random

def random_list(n):
    result = []
    ids = list(range(1001,1001+n))
    a1 = ['赵','钱','孙','李']
    a2 = ['丽','强','飞','']
    a3 = ['梦','天','鑫','田','国','安','成']
    for i in range(n):
        age = random.randint(18,60)
        id = ids[i]
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)
        dir = {id,age,name}
        result.append(dir)
    print(result)
    return result

random_list(60)





