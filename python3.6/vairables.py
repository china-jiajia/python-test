#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao



# http://www.cnblogs.com/linhaifeng/articles/6113086.html#_lable1

#局部变量与全局变量

# name = '帅的一逼咋地啦'
#
#
# def change_name():
#     name = '帅的一笔'
#     print('change_name', name)
#
#
# change_name()
# print(name)


# global
# NAME='杠娘'
#
#
# def yangjian():
#     global NAME
#     print("我要挖", NAME)
#     NAME = "小东北"
#     print("我要挖", NAME)
#
#
# def qupengfei():
#     print("我要搞", NAME)

#如果函数的内部无,global关键字;优先读取局部变量如果没有局部变量那就只能读取全局变量,无法重新赋值
# 但是对于可变类型,可以对内部元素进行操作
#如果函数中有global关键字,变量本质上市全的变量,可读取可赋值
# yangjian()
# qupengfei()



# NAME = ['产品经理','廖波湿']


# def yangjian():
#     global NAME
#     print("我要挖", NAME)
#     NAME = "小东北"
#     print("我要挖", NAME)


# def qupengfei():
#     # NAME = "搞基"
#     # global NAME
#     # NAME = "天斩龙"
#     NAME.append('天斩龙')
#     print("我要搞", NAME)
#
# # yangjian()
# qupengfei()


#如果函数内无global关键字
# - 有声明局部变量
# - 无声明局部变量

#如果函数内有global关键字
# - 有声明局部变量
# - 无声明局部变量


#*全局变量全部大写;局部变量都小写




# NAME = '海风'
#
#
# def huangwei():
#     name = "黄伟"
#     print(name)
#
#     def liuyang():
#         name = "刘洋"
#         print(name)
#
#         def nulige():
#             name = "护指花"
#             print(name)
#
#         print(name)
#         nulige()
#
#     liuyang()
#
#     print(name)
#
#
# huangwei()



#三层
# name = '杠娘'
#
# def weihou():
#     name = "陈卓"
#     def weiweihou():
#         global name
#         name = "冷静"
#     weiweihou()
#     print(name)
#
# print(name)
# weihou()
# print(name)




# name = '杠娘'
#
# def weihou():
#     name = "陈卓"
#     def weiweihou():
#         nonlocal name   #指定上一级变量
#         name = "冷静"
#     weiweihou()
#     print(name)
#
# print(name)
# weihou()
# print(name)

# 杠娘
# 冷静
# 杠娘

