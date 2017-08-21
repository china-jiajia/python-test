#!/usr/bin/env python
# -*- coding utf8 -*-

# 全局变量
APPLE = 100
a = None

def fun():
#    a = 10
#    a = APPLE

# 全局变量声明
    global a
    a = 20
    print(a)
    return a+100

# 这个只能输出函数本身不能输出 return值
#fun()

# 这样做会输出函数定义的值，和return值
# print(fun())


print('a past=',a)
print(fun())
print('a now=',a)