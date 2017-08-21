#!/usr/bin/env python
# -*- coding utf8 -*-

# def function():
#     print('This is a funcation')
#     a = 1 + 2
#     print(a)

#function()

# def fun(a,b):
#     c = a*b
#     print('this c is',c)
#
# fun(a=2,b=5)

# 函数没有预先定义好的值需要放在，已经定义好值的前面不不然输出函数的时候会报错
# def sale_car(price,brand,colour='red',is_second_hand=True):
def sale_car(price,colour='red',brand='carmy',is_second_hand=True):
    print('price:',price,
        'colour:',colour,
        'brand:',brand,
        'is_second_hand:',is_second_hand,)

#在函数尾部定义输出的值
# sale_car(1000,'red','carmy',True)

#在定义函数的时候定义好值
# sale_car(1400)

#函数开始已经定义好值，后期需要对值进行更改(直接在函数输出的时候做更改即可)
sale_car(1500,colour='blu')