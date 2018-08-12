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

# 编程逻辑方法:
# 面向过程
# 函数式
#     1.不可变数据
#     2.第一类对象
#     3.尾调用优化(尾递归)
# 面向对象

# 函数式编程
# www.cnblogs.com/linhaifeng/articles/6113086.html#_labe8

#高阶函数
# 满足两个特性任意即为高阶函数
# 1.函数的传入参数是一个函数名
# 2.函数的返回值是一个函数名




#函数式(把函数当做参数传递给另外一个函数):
# def foo(n):
#     print(n)
#
# def bar(name):
#     print('my name is %s' %name)
#
# foo(bar)            #这里是直接把bar()函数的内存地址传递给foo()函数
# # foo(bar())          #这个理bar()没有return返回值,所有foo()里面返回的值为None
# foo(bar('jiajia'))


#返回值中包含函数
# def bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#     return  bar
#
# n=foo()
# n()
# def hanle():
#     print('from hanle')
#     return hanle
# h=hanle
# h()



# num_l=[1,10,33,25,67]
#
# def map_test(array):
#     ret=[]
#     for i in num_l:
#         ret.append(i**2)
#     return ret
#
# res=map_test(num_l)
# print(res)



#使用匿名函数
# num_l=[1,10,33,25,67]
#
# def add_one(x):
#     return x+1
#
# def reduce_one(x):
#     return x-1
#
# def pf(x):
#     return  x**2
#
# def map_test(func,array):
#     ret=[]
#     for i in num_l:
#         res=func(i)
#         ret.append(res)
#     return ret
#
# print(map_test(add_one,num_l))
# print(map_test(lambda x:x+1,num_l))
# print(map_test(reduce_one,num_l))
# print(map_test(lambda x:x-1,num_l))
# print(map_test(pf,num_l))
# print(map_test(lambda x:x**2,num_l))



#1.函数式编程当中的map()方法
#备注:python2当中map()处理的结果就是一个list
# num_l=[1,10,33,25,67]
#
# def map_test(func,array):
#     ret=[]
#     for i in num_l:
#         res=func(i)
#         ret.append(res)
#     return ret
#
# print(map_test(lambda x:x+1,num_l))
# print('内置函数map,处理结果: ',map(lambda x:x+1,num_l))
#
# res=map(lambda x:x+1,num_l)
# # for i in res:         #可迭代
# #     print(i)
#
# print(list(res))



# 2.函数式编程filter函数
# movie_peple=['sb_alex','sb_wupeiqi','lihaifeng','sb_yuahao']
#
# def fileter_test(array):
#     ret=[]
#     for p in movie_peple:
#         if not p.startswith('sb'):
#             ret.append(p)
#     return ret
#
# res=fileter_test(movie_peple)
# print(res)


# movie_peple=['sb_alex','sb_wupeiqi','lihaifeng','sb_yuahao']
# movie_peple=['alex_sb','wupeiqi_sb','lihaifeng','yuahao_sb']
#
# def sb_show(n):
#     return n.endswith('sb')
#
# def fileter_test(func,array):
#     ret=[]
#     for p in array:
#         if not func(p):
#             ret.append(p)
#     return ret
#
# res=fileter_test(sb_show,movie_peple)
# print(res)


#最终形式
# movie_peple=['alex_sb','wupeiqi_sb','lihaifeng','yuahao_sb']
#
# def fileter_test(func,array):
#     ret=[]
#     for p in array:
#         if not func(p):
#             ret.append(p)
#     return ret
#
# res=fileter_test(lambda n:n.endswith('sb'),movie_peple)
# print(res)


#filter函数
# movie_peple=['alex_sb','wupeiqi_sb','lihaifeng','yuahao_sb']
# print(filter(lambda n:n.endswith('sb'),movie_peple))
# print(list(filter(lambda n:n.endswith('sb'),movie_peple)))      #filter()函数默认是取值的,没有上面的not 成员运算
# print(list(filter(lambda n:not n.endswith('sb'),movie_peple)))  #正确结果



# 3.reduce函数
# python2当中reduce函数直接使用就可以了,reduce()
# python3当中使用reduce函数,from fuctools import reduce

# num_1=[1,2,3,100]
#
# def multi(x,y):
#     return x*y
#
# def reduce_test(func,array,init=None):
#     if init is None:
#         res=array.pop(0)
#     else:
#         res=init
#     for num in array:
#         res=func(res,num)
#     return res
#
# print(reduce_test(lambda x,y:x*y,num_1))


#reduce函数
# from functools import reduce
# num_l=[1,2,3,100]
# print(reduce(lambda x,y:x+y,num_l))



# 4.总结
# 处理序列中的每个元素,得到的结果是一个"列表",该'列表'元素个数及位置与原来一样
# map()


# filter遍历序列中的每个元素,判断每个元素得到布尔值,如果是True则留下来
# 备注:filter处理的是序列
# people=[
#     {'name':'alex','age':10000},
#     {'name':'wipeiqi','age':10000},
#     {'name':'yuanhao','age':9000},
#     {'name':'linhaifeng','age':18},
# ]
#
#
# print(list(filter(lambda p:p['age']<=18,people)))


# reduce函数:处理一个序列,然后把序列进行合并操作
# from functools import reduce
# print(reduce(lambda x,y:x+y,range(100),100))
# print(reduce(lambda x,y:x+y,range(1,101)))