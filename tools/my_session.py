# -*- coding: utf-8 -*-
# @time     : 2020/12/23 17:00
# @Author   : 王永琪
# @Site     : 
# @File     : my_session.py
# @Software : PyCharm

import requests      # requess是第三方的，所以需要导入
import json

login_url='http://192.168.0.105:9999/futureloan/mvc/api/member/login'  #登录接口地址
login_data={'mobilephone':'13417467890','pwd':'123456'} #请求的数据是字典格式
recharge_url='http://192.168.135.128:9999/futureloan/mvc/api/member/withdraw'  #登录接口地址
recharge_data={'mobilephone':'13417467890','amount':'100'} #请求的数据是字典格式
print(json.dumps(login_data))
print(type(json.dumps(login_data)))
s=requests.Session()