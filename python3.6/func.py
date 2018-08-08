#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


# 使用函数的好处:
#     1.代码重用
#     2.保持一致性,易维护
#     3.可扩展性


#数学意义函数
'''
y=2*x+1
'''


#python代码函数

# def test(x):
#     "The function definitions"  #注释功能
#     x += 1
#     return x
#
# print(test(1))


# while True：
# if cpu利用率 > 90 %:
#     # 发送邮件提醒
#     连接邮箱服务器
#     发送邮件
#     关闭连接
#
# if 硬盘使用空间 > 90 %:
#     # 发送邮件提醒
#     连接邮箱服务器
#     发送邮件
#     关闭连接
#
# if 内存占用 > 80 %:
#     # 发送邮件提醒
#     连接邮箱服务器
#     发送邮件
#     关闭连接


# def 发送邮件(内容)
#     # 发送邮件提醒
#     连接邮箱服务器
#     发送邮件
#     关闭连接
#
#
# while True：
#
# if cpu利用率 > 90 %:
#     发送邮件('CPU报警')
#
# if 硬盘使用空间 > 90 %:
#     发送邮件('硬盘报警')
#
# if 内存占用 > 80 %:
#     发送邮件('内存报警')





#函数和过程
    # 函数:
    # 过程:过程就是没有返回值的函数(没有return)


# def test01():
#     msg = 'hello The little green frog'
#     print(msg)
#
# def test02():
#     msg = 'hello WuDaLang'
#     print(msg)
#     return msg
#
# def test03():
#     msg = 'hello WuDaLang1'
#     print(msg)
#     return 0,10,'hello',['alex','lb'],{'WuDaLang','lb'}
#
# t1=test01()
# t2=test02()
# t3=test03()
#
# print(t1)
# print(t2)
# print(t3)

# 总结:
#     1.返回值数=0 返回None
#     2.返回值数=1 返回object
#     3.返回值数>1 返回tuple




#函数参数:
    # 1.形参:在被调用时才分配你内存单元,调用结束时,即刻释放所分配的内存单元;因此形参只在函数内部有效,函数调用结束返回主调用函数后则不能再用该形参变量
    # 2.实参:实参可以是常量、变量、表达式、函数等,无论实参是何种类型的量,在进行函数调用时,他们都必须有确定的值,以便把这些值传送给形参.因此应用预先用赋值,输入等办法使参数获得确定值
    # 3.位置参数和关键字(标准调用:实参与形参位置一一对应;关键字调用:位置无需固定)
    # 4.默认参数
    # 5.参数组

#位置参数(必须一一对应,缺一不行)
# def test(x,y,z):
#     print(x)
#     print(y)
#     print(z)
#
# test(1,2,3)


#关键字参数(无需一一对应,缺一不行)
# def test(x,y,z):
#     print(x)
#     print(y)
#     print(z)
#
# test(y=1,x=2,z=3)       #关键字参数(位置不是固定)


#位置参数必须在关键字参数左边(混合使用)
# def test(x,y,z):
#     print(x)
#     print(y)
#     print(z)
#
# test(1,3,z=4)



#默认参数
# def headle(x,type=None):
#     print(x)
#     print(type)
#
# headle('hello')
# headle('hello',type='sqlite')
# headle('hello','sqlite')        #这里没有"type="就变成位置参数了



#参数组: **字典, *列表
def test(x,**kwargs):
    print(x)
    # print(args)     #这里接收的是列表,只能使用位置参数
    # print(kwargs[0])
    print(kwargs)


# test(1,2,3,4,5,6)
# test(1,{"name":"alex"})
# test(1,['x','y','z'])
# test(1,*['x','y','z'])
# test(1,*('x','y','z'))

# test(1,y=2,z=3)     #关键字参数对应**kwargs
# test(1,y=2,z=3,z=4)    #会报错,一个参数不能传两个值



# def test(x,*args,**kwargs):
#     print(x)
#     print(args)
#     print(kwargs)
#
# test(1,1,2,1,1,11,y=2,z=3)


# def test(x,*args,**kwargs):
#     print(x)
#     print(args,args[-1])
#     print(kwargs,kwargs.get('y'))
#
# test(1,*[1,2,3],**{"y":1})

