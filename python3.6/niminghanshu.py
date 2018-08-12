#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/12'
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


# http://www.cnblogs.com/linhaifeng/articles/6113086.html#_labe8
# 匿名函数的使用:
# 1.匿名函数是直接使用的不用重新命名
# 2.匿名函数具备复杂逻辑


name='alex'
def change_name(x):
    return  name+'_sb'

res=change_name(name)
print(res)


f=lambda x:name+'_sb'
f(name)


func=lambda x:x+'_sb'
res=func(name)
print('匿名函数的运行结果',res)

