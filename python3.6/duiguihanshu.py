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


# http://www.cnblogs.com/linhaifeng/articles/6113086.html#_lable1

# 递归特性:
# 1.必须有一个明确的结束条件
# 2.每次进入更深一层递归时,问题规模相比上次递归都应有所减少
# 3.递归效率不高,递归层次过多会导致栈溢出(在计算机中,函数调用是通过栈(stack)这种数据结构实现的,每当进入一个函数调用,栈就会加一层栈帧,每当函数返回,栈就会减少一层栈帧.由于栈的大小
# 不是无限的,所以,递归调用的次数过多,会导致栈溢出)

#堆栈扫盲 http://www.cnblogs.com/lln7777/archive/2012/03/14/2396164.html
# 尾递归优化 http://egon09.blog.51cto.com/9161406/1842475


# import time
#
# def calc(n):
#     print(n)
#
#     calc(n)
#
# calc(10)



# def calc(n):
#     print(n)
#     if int(n / 2) == 0:
#         return  n           #必须有一个明确的结束条件
#     return calc(int(n / 2))
#
# calc(10)



import  time

percon_list=['alex','weipeiqi','yuanhao','linhaifeng']

def ask_way(percon_list):
    print('-'*60)

    if len(percon_list) == 0:
        return '根本没人知道'
    percon=percon_list.pop(0)
    if percon == 'linhaifeng':
        return  '%s 说: 我知道,老男孩教育就在沙河汇得商厦,下地铁就是' %percon

    print('hi 美男[%s],敢问路在何方' % percon)
    print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' %(percon,percon_list))
    time.sleep(3)
    res=ask_way(percon_list)
    print('%s问的结果是: % res' %(percon,res))
    return  res


res=ask_way(percon_list)
print(res)
