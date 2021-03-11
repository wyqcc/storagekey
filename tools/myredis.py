#!/usr/bin/env python  
# -*- coding: utf-8 -*-


# 存放session会话
# from redis import StrictRedis

import redis
#阈值缓存
rd=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,db=0)
#传感器缓存
rd1=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,db=1)
#传感器安装
rd2=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,db=2)
#ip
rd3=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,db=3)
#电量预警
rd4=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,db=4)
#柜子预警
rd5=redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=1000,db=5)
