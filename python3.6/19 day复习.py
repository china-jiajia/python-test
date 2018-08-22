#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/19'
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

import copy

# 函数

# 模块

# 面向对象编程



# 1.深浅拷贝
# www.cnblogs.com/yuanchenqi/articles/5782764.html
# 深拷贝:两个独立的内存,相互没有关系;可以进行独立的操作
# s=[1,'alex','alvinn']
# s2=s.copy()
# print(s2)
#
# s2[0]=5
# print(s2)


# 浅拷贝:浅拷贝只拷贝第一层(应用场景,数据量很大的情况下可以避免重新复制生成一份数据浪费内存空间)
# a=[[1,2],3,4]
# b=a[:]  # b=a.copy()  这两个相同
# b[1]='abc'
# print(b)
# print(a)


# 实例(浅拷贝)
# husband = ['xiaohu',123,[15000,9000]]
# wife = husband.copy()
# wife[0] = 'xiaopang'
# wife[1] = 456
#
# husband[2][1] -= 4500
#
# print(wife)




# 深拷贝(需要import copy)克隆一份
# husband = ['xiaohu',123,[15000,9000]]
# wife = husband.copy()
# wife[0] = 'xiaopang'
# wife[1] = 456
#
#
# # xiaosan = copy.copy()   #shallow copy   (浅拷贝)
# xiaosan = copy.deepcopy(husband)
# xiaosan[0] = 'JinXin'
# xiaosan[1] = 666
#
#
# xiaosan[2][1] -= 1999
# husband[2][1] -= 4500
#
#
# print(wife)
# print(xiaosan)







# 2.set(集合)
# www.cnblogs.com/yuanchenqi/articles/5782764.html
#     1).set(集合)是无序,不重复的
#     2).set集合当中不能使用列表或者字典作为元素,唯一它们是不可哈希的
#     3).结合可以分可变集合和不可变集合

# 创建列表
# a=[2,4,6]
# b=list[6,8,10]

# 创建元祖
# a=(1,2,3)
# b=tuple([4,5,6])

# s=set('alex li')
# s1=['alvin','ee','alvin']
# s2=set(s1)
# print(s2,type(s2))
#
# s=list(s2)
# print(s,type(s))


# li=[[1,2],3,'alex']         #这里set集合当中不能使用列表或者字典作为元素,唯一它们是不可哈希的
# li = [1, 3, 'alex']
# s = set(li)
# print(s)


# d = {s:'123'}   #报错: unhashable type: 'set'

# print(1 in s)
# print(4 in s)

# #更新set(集合)
# s.add('x')
# print(s)
# s.add('xx')     #添加一个元素
# print(s)


# s.update([12,'alex'])
# print(s)

# s.remove(3)
# print(s)

# s.pop()
# print(s)

# s.clear()
# print(s)







# 3.函数
# www.cnblogs.com/yuanchenqi/articles/5828233.html
#     概念
# 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可

# 特性:
#     1.代码重用
#     2.保持一致性
#     3.可扩展性

#     创建
#         函数名的命名规则：
#             函数名必须以下划线或字母开头，可以包含任意字母、数字或下划线的组合。不能使用任何的标点符号；
#             函数名是区分大小写的。
#             函数名不能是保留字。

#     参数
#         形参和实参:
#             形参：形式参数，不是实际存在，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参（实参个数，类型应与实参一一对应）
#             实参：实际参数，调用函数时传给函数的参数，可以是常量，变量，表达式，函数，传给形参
#             区别：形参是虚拟的，不占用内存空间，.形参变量只有在被调用时才分配内存单元，实参是一个变量，占用内存空间，数据传送单向，实参传给形参，不能形参传给实参

# 内部参数:
#     位置参数:按顺序对应
#     关键字参数: 指定值 "="


# import time



# def logger(n):
#     time_format = '%Y-%m-%d %X'
#     time_current = time.strftime(time_format)
#     with open('日志记录', 'a') as f:
#         f.write('%s end action%s\n' % (time_current,n))
#
# def action1(n):
#     print('starting action1 ...')
#     logger(n)
#
# def action2(n):
#     print('starting action1 ...')
#     logger(n)
#
# def action3(n):
#     print('starting action1 ...')
#     logger(n)
#
#
# action1(11)
# action1(22)
# action1(33)



# 函数  != function()
# 计算机函数  == subroutine 子程序,procedures 过程
# 作用:
#     1.减少重复代码
#     2.方便修改,更易扩展
#     3.保持代码一致性





# def show_shopping_car():
#     saving = 1000000
#     shopping_car = [
#         ('Mac', 9000),
#         ('kindle', 800),
#         ('tesla', 100000),
#         ('Python book', 105),
#     ]
#
#     print('您已经购买的商品如下'.center(50, '*'))
#     for i, v in enumerate(shopping_car, 1):
#         print('\033[35;1m %s: %s \033[0m' % (i, v))
#
#     expense = 0
#     for i in shopping_car:
#         expense += [1]
#     print('\n\033[32;1m 您的余额为 %s \033[0m' % (saving - expense))
#
#
# show_shopping_car()





# def print_info(name,age):
#     print('Name: %s' % name)
#     print('Age: %d' % age)
#
# # print_info(39,'xiaohu')     #必须参数,会报错位置参数位置传反了
# print_info(name='xiaohu',age=39)    #2:关键字参数


# def print_sum(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# print_sum(1,2,3,34,57,8)


# def print_info(name,age,sex):
#     print('Name: %s' % name)
#     print('Age: %d' % age)
#     print('sex: %s' % sex)
#
# print_info('alex',18,'male')

#
# def print_info(*args):    #无命名参数
#     print(args)
#
# print_info('alex',18,'male')


# def print_info(**kwargs):     #有名参数
#     print(kwargs)
#     for i in kwargs:
#         print('%s:%s' %(i,kwargs[i]))
#
# print_info(job='IT',hobby='girls',height=188,)


# 不定长参数的位置:
#     *args：放在左边(无命名-元祖)
#     **kwargs: 放在右边(有命名-字典)
#     如果有默认参数,放左边




#     return        #返回什么内容,给谁呢?
#     作用:
#         1.结束函数
#         2.返回某个对象

# 注意点:
#     1.函数执行过程中遇到return语句,就会停止执行并返回结果;所以也可以理解为return语句代表着函数的结束
#     2.函数里如果没有return,会默认返回一个None
#     3.如果return多个对象,那么python会把多个对象封装成一个元祖返回






#作用域
    # Python中的作用域分4种情况:
    #     1.L:local,局部作用域,即函数中定义的变量
    #     2.E:enclosing,嵌套的父级函数的局部作用域,即包含此函数的上级函数的局部作用域,但不是全局的
    #     3.G:global,全局变量,就是模块级别定能定义的变量
    #     4.B:built-in,系统固定模块里面的变量,比如int,bytearray等.搜索变量的优先级顺序依次是:作用局部>外层作用域>当前模块中的全局>python内置作用域,也就是LEGB



# x = int(2.9)        #int built-in
#
# g_count = 0     #global
# def outer():
#     o_count = 1     # enclosing
#
#     def inner():
#         i_count = 2     # local
#         print(o_count)
#
#     # print(i_count)  找不到
#     inner()



# def outer():
#     count = 10
#     def inner():
#         nonlocal count  #使用nonlocal声明之后就可以对count进行修改了
#         count = 20
#         print(count)
#     inner()
#     print(count)
# outer()



# 小结:
#     1.变量查找顺序: LEGB,作用域局部>外部作用域>当前模块中的全局>python内置作用域
#     2.只有模块、类、及函数才能引入新作用域
#     3.对一个变量,内部作用域先声明就会覆盖外部变量,不声明直接使用,就会使用外部作用域的变量
#     4.内部作用域要修改外部作用域变量的值时,全局变量要使用global关键字,嵌套作用域变量要使用nonlocal关键字,nonlocal是python3新增加的关键字,有了这个关键字,就能完美的实现闭包了


