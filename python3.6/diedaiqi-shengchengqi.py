#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/14'
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


# 1.迭代器协议
# l=[1,2,3]
# # for i in l:     #i_l=l.__iter__()    i_l.__next__()
# #     print(i)
#
# print(l[0])
# iter_l=l.__iter__()     #遵循迭代器协议,生成可迭代对象
# print(iter_l.__next__())
#
#
# index=0
# while index < len(l):
#     print(l[index])
#     index+=1
#
#
# x='hello'
# iter_test=x.__iter__()
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())


# dic={'a':1,'b':2}
# iter_dic=dic.__iter__()
# print(iter_dic.__next__())
# print(iter_dic.__next__())


# f=open('test.txt','r+')
# iter_f=f.__iter__()
# print(iter_f)
# print(iter_f.__next__(),end='')
# print(iter_f.__next__(),end='')


# l=[1,2,3,4,5]
# diedai_l=l.__iter__()
# while True:
#     try:
#         print(diedai_l.__next__())
#     except StopIteration:
#         print('迭代完毕了,循环终止了')
#         break


# 备注:只要遵循迭代器协议,就是可以迭代对象
#     1.怎么把一个类型转换成可迭代对象,调用__iter__()





#2.生成器
    # 生成器就是可迭代对象

    # 1.生成器函数:常规函数定义,但是,使用yield语句而不是return语句返回结果.yield语句一次返回一个结果,在每个结果中间,挂起函数的状态,以便下次从它离开的地方继续执
    # 2.生成器表达式:类似于列表推导,但是,生成器返回按需要产生结果的一个对象,而不是一次构建一个结果列表


#三元表达式
# name='alex'
# name='linhaifeng'
# res='SB' if name == 'alex' else '帅哥'
# print(res)



#列表解析
# egg_list=[]
# for i in range(10):
#     egg_list.append('鸡蛋%s' %i)
# print(egg_list)
#
# l=[ '鸡蛋%s' %i for i in range(10)]
# # l1=[ '鸡蛋%s' %i for i in range(10) if i > 5 else i]  #没有四元表达式
# l1=[ '鸡蛋%s' %i for i in range(10) if i > 5]
# print(l)
# print(l1)



#函数是表达式,通过yield获得生成器对象
# def test():
#     yield 1
#     yield 2
#     yield 3
# g=test()
# print('来自函数',g)
#
#
# #生成器表达式
# laomuji=('鸡蛋%s' %i for i in range(10))
# print(laomuji)
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(next(laomuji))
#


# 总结:
#     1.把列表解析[]替换成()得到的就是生成器表达式
#     2.列表解析与生成器表达式是一种便利的编程方式,只不过生成器表达式更节省内存
#     3.Python不但使用迭代器协议,让for循环变得更加通用.大部分内置函数,也是使用迭代器协议访问对象的.例如,sum函数是Python的内置函数,该函数使用迭代器协议访问对象,而生成器实现了
#     迭代器协议,所以,我们可以直接这样计算一系列值的和:

    # sum(x ** 2 for x in range(4))       #xrange只存在python2.X当中
    # sum([x ** 2 for x in range(4)])


print(sum(i for i in range(10000000000)))