#!/usr/bin/env python
# -*- coding utf8n -*-

class Calculator:
    name = 'Good calcuator'
    price = 18

# 初始的属性定义
    def __init__(self,name,price,hight,width,weight):
        self.name = name
        self.price = price
        self.hight = hgiht
        self.wi = width
        self.we = weight
        self.add(1,2)

    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)


# 外部调用
#   定义一个class的变量值
    calcul = Calculator

#   引用class内部的变量
    calcul.name
    calcul.price

    calcul.add(10,11)