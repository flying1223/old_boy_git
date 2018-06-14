#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-14 20:26:00
# @Author  : flying

av_catalog = {
    "欧美":{
        "www.youporn.com":["很多免费的，世界最大的","质量一般"],
        "www.pornhub.com":["很多免费的，也很大的","质量比porn高点"],
        "letmedothistoyou.com":["很多自拍，高质量图片很多","资源不多更新慢"],
        "x-art.com":["质量很高，真的很高","全部收费，屌丝绕行"]
    },
    "日韩":{
        "tokyo-hot":["质量怎么样不清楚，个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费，好人一生平安","服务器在国外，慢"]
    }
}
av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"

print(av_catalog)
print(av_catalog.values())
print(av_catalog.keys())

av_catalog.setdefault("台湾",{"www.baidu.com":[1,2]}) #如果存在key 则不增加新值》》》{'欧美': {'www.youporn.com': ['很多免
# 费的，世界最大的', '质量一般'], 'www.pornhub.com': ['很多免费的，也很大的', '质量比porn高点'], 'letmedothistoyou.com': ['
# 很多自拍，高质量图片很多', '资源不多更新慢'], 'x-art.com': ['质量很高，真的很高', '全部收费，屌丝绕行']}, '日韩':
# {'tokyo-hot': ['质量怎么样不清楚，个人已经不喜欢日韩范了', '听说是收费的']}, '大陆': {'1024': ['全部免费，好人一生平安',
#  '可以在国内做镜像']}, '台湾': {'www.baidu.com': [1, 2]}}

print(av_catalog)
