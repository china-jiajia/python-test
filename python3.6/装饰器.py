#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/22'
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

"""
装饰器(本质就是函数,功能为其他函数添加附加功能):
www.cnblogs.com/linhaifeng/articles/6140395.html


原则:
    1.不修改被修饰函数的源代码
    2.不修改被修饰函数的调用方式

"""

# import time
#
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('函数运行时间 %s' % (stop_time-start_time))
#         return res
#     return wrapper
#
#
# @timmer
# def cal(n):
#     res=0
#     for i in n:
#         res+=i
#     return res
#
# print(cal(range(100)))




"""
不合格,多运行了一次
import time

def foo():
    time.sleep(3)
    print('来自于foo')

# 不修改foo源代码
# 不修改foo调用方式


def timer(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print('函数运行时间是 %s' % (stop_time-start_time))
    return func

foo=timer(foo)
foo()
"""




"""
装饰器储备知识:
    装饰器=高阶函数+函数嵌套+闭包

        1.高阶函数
                a.函数接收的参数是一个函数名
                b.函数的返回值是一个函数名
                c.满足上述条件任意一个,都可称为高阶函数
                
                
    嵌套 + 闭包
     
def father(name):
    def son():
        # name='A'  #这里注释了之后,后面的name找的都是函数开头传入进来的name
        print('我的爸爸是%s' % name)
        def grandson():
            print('我的爷爷是%s' % name)
        grandson()
    son()

father('B')
"""

"""
简单装饰器

import time

#装饰器框架
def timmer(func):
    def wrapper():
        # print(func)
        start_time=time.time()
        func()      #此刻运行的就是test()
        stop_time=time.time()
        print('函数运行时间%s' % (stop_time-start_time))
    return wrapper()

@timmer
def test():
    time.sleep(3)
    print('test函数运行完毕')

# res=timmer(test)        #返回的是wrapper的地址
# res()           #执行的是wrapper()

# test=timmer(test)
# test()


#语法糖
    # @timmer     #就相当于test=timmer(test)

"""



"""
加上返回值

import time


def timmer(func):
    def wrapper():
        start_time=time.time()
        res=func()
        stop_time=time.time()
        print('函数运行时间%s' % (stop_time-start_time))
        return res
    return wrapper

@timmer
def test():
    time.sleep(3)
    print('test函数运行完毕')
    return '这是test的返回值'


res = test
print(res)
"""




#加上参数
import time


def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('函数运行时间%s' % (stop_time-start_time))
        return res
    return wrapper

@timmer
def test(name,age):
    time.sleep(3)
    print('test函数运行完毕,名字是 【%s】 年龄是【%s】' % (name,age))
    return '这是test的返回值'


@timmer
def test1(name,age,gender):
    time.sleep(3)
    print('test函数运行完毕,名字是 【%s】 年龄是【%s】性别 【%s】' % (name,age,gender))
    return '这是test的返回值'

res = test('A',18)
# print(res)
test1('B',19,'male')



"""
解压序列(在终端下测试)

>>> a,b,c=[1,2,3]
>>> a
1
>>> b
2
>>> c
3

>>> l=[10,3,2,5,1,2,3,5,8,9]        #这里是取值开头和结尾不使用索引
>>> a,*_,c=l
>>> a
10
>>> c
9

>>> a=1
>>> b=2
>>> a,b=b,a
>>> a
2
>>> b
1

"""