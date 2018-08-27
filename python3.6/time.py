#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/26'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


import time
#
# #时间戳 #计算
# print(time.time())      #1535216809.9195
#
#
# #结构化时间----当地时间
# print(time.localtime(1431242343))
# t=time.localtime()
# print(t.tm_year)
# print(t.tm_wday)
#
#
#
#
# #-----将结构化时间转换成时间戳
# print(time.mktime(time.localtime()))


#------将结构化时间转换成字符串时间strftime
# print(time.strftime("%Y-%m-%d %X",time.localtime()))

#----将字符串时间转换成结构化时间strptime
# print(time.strptime("2016:12:24:17:50:36","%Y:%m:%d:%X"))


# print(time.asctime())
# print(time.ctime())



# import datetime
#
# print(datetime.datetime.now())





#随机模块
import random

# ret=random.random()
# ret=random.randint(1,3)
# ret=random.randrange(1,3)
# ret=random.choice([11,22,33,44,55])
# ret=random.sample([11,22,33,44,55],2)
# ret=random.uniform(1,4)
# print(ret)
#
# ret=[1,2,3,4,5]
# random.shuffle(ret)
# print(ret)




def v_code():

    ret=""
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,122))
        s=str(random.choice([num,alf]))
        ret+=s
    return ret

print(v_code())


