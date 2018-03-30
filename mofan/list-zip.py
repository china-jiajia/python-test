#!/usr/bin/env python
# -*- coding utf8 -*-

a = [1,2,3]
b = [4,5,6]

# zip(a,b)
# list(zip(a,b))
#
# for i,j in zip(a,b):
#     print(i/2,j*2)


def fun1(x,y):
    return(x+y)



fun1(2,3)

# lambda 定义一个简单的方程，简洁缩小代码行数
fun2 = lambda x,y:x+y

fun2(2,3)


# map 就已知的功能加上需要输入的参数一起，输入运算
map(fun1,[1],[2])       #这样显示的会是底层的存储位置信息
list(map(fun1,[1],[2]))     #这样才是可以看懂的，计算结果
