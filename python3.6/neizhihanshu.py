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


#www.cnblogs.com/linhaifeng/articles/6113086.html#_labe8


#绝对值
# print(abs(-1))
# print(abs(1))

#所有把所有元素拿来做布尔运算
# print(all([1,2,'1']))
# print(all([1,2,'']))
# print(all('hello'))


#任意一个
# print(any([0,'']))
# print(any([0,'',1]))
#
# print(bin(3))       #十进制转换成二进制

#空,None,O的布尔值为False,其余为True
# print(bool(''))
# print(bool(None))
# print(bool(0))
#
#
# print(bytes('你好',encoding='utf-8'))
# print(bytes('你好',encoding='utf-8').decode('utf-8'))
#
# print(bytes('你好',encoding='gbk'))
# print(bytes('你好',encoding='gbk').decode('gbk'))



#ascii编码
# print(chr(49))


# dict()      #字典
#
# print(dir(all))     #打印某一个对象下面都有哪些方法
#
# print(divmod(10,3))     #做分页功能,'10' 总的有多少条记录,'3'一页存放多少条记录


# enumerate()

# eval报字符串当中的字段提取出来;如下是在python的交互界面下操作的
# >>> dic={"name":"alex"}
# >>> dic_str=str(dic)
# >>> dic_str
# "{'name': 'alex'}"
# >>> eval(dic_str)
# {'name': 'alex'}

#eval可以把字符串当中的算数运算,做一遍
# >>> express='1+2*(3/3-1)-2'
# >>> express
# '1+2*(3/3-1)-2'
# >>> eval(express)
# -1.0

# dic={'name':'alex'}
# dic_str=str(dic)
# print(dic_str)

#可hash的数据类型即不可变数据类型,不可hash的数据类型即可变数据类型
# 1.无论字符串或者数字串多长,hash的值都是同一个长度不变呢
# 2.无法通过hash值推导出具体的字符串或者数据串
# print(hash('adfjaiowhgioehfkldsnaklfnksadfs'))
# print(hash('bej3rgho3qhgjnskaldjfo3i2quhg2uo23r675106you2fhjasNFLKD'))

#打印函数使用帮助
# print(help(all))
# print(help(dir(all)))


# print(bin(10))      #十进制转二进制
# print(hex(12))      #十进制转十六进制
# print(oct(12))      #十进制转八进制

#
# print(isinstance(1,int))
# print(isinstance('abc',int))
# print(isinstance([],list))
# print(isinstance({},dict))



#打印全局变量信息
# name='哈哈哈哈哈哈'
# # print(globals())
# # print(__file__)
#
# def test():
#     age='234325435'
#     # print(globals())
#     print(locals())         #打印局部变量信息
#
# test()


# l=[1,3,100,-1,2]
# print(max(l))
# print(min(l))

#zip()传递两个参数都是序列
# print(list(zip(('a','b','n','c'),(1,2,3))))
# print(list(zip(('a','b','n'),(1,2,3))))
# print(list(zip(('a','b','n'),(1,2,3,4))))
#
# p={'name':'alex','age':18,'gender':'none'}
# print(list(zip(p.keys(),p.values())))



# 1.max()比较传入的是一个可迭代对类型对象
# 2.max()比较的时候是从第一个元素开始进行比较,第一个元素已经区分出大小后面就不会进行比较
# age_dic={'age1':18,'age2':20,'age3':100,'age4':30}
#
# print(max(age_dic.values()))
# print(max(age_dic))
# print(list(zip(age_dic.values(),age_dic.keys())))
# print(max(list(zip(age_dic.values(),age_dic.keys()))))


# l=[
#     (5,'e'),
#     (1,'b'),
#     (3,'a'),
#     (4,'d'),
# ]
#
# # l1=['a10','b12','c10',100]  #不同类型间不能进行比较
# # l1=['a10','b12','c10']
# l1=['a10','a2','a10']
#
# print(list(max(l)))
# print('----->',list(max(l1)))


# l=[1,3,100,-1,2]
# print(max(l))
#
# dic={'age1':18,'age2':10}
#
# print(max(dic))             #只能比较key值的大小
# print(max(dic.values()))    #这个能比较values值的大小,但是不能知道对应的是哪个key
# print(max(zip(dic.values(),dic.keys())))    #把key和value对调位置进行比较输出,可以显示出全部信息


# 最终效果:
# people=[
#     {'name':'alex','age':1000},
#     {'name':'wupeiqi','age':10000},
#     {'name':'yuanhao','age':9000},
#     {'name':'linhaifeng','age':18},
#
# ]

# print(max(people))      #字典没办法进行比较
# max(people,key=lambda dic:dic['age'])

# print(max(people,key=lambda dic:dic['age']))

# ret=[]
# for item in people:
#     ret.append(item['age'])
# print(ret)
# max(ret)






# print(ord('a'))
#
# print(pow(2,3))         #具体函数的次方
# print(pow(3,3,2))       #3的3次方取余
#
# l=[1,2,3,4]
# print(list(reversed(l)))
# print(l)
#
#
# print(round(3.5))
#
#
# print(set('hello'))
#
# l='hello'
# # print(l[3:5])
# s1=slice(3,5)
# s2=slice(1,4,2)
# print(l[s1])
# print(l[s2])



# people=[
#     {'name':'alex','age':1000},
#     {'name':'wupeiqi','age':10000},
#     {'name':'yuanhao','age':9000},
#     {'name':'linhaifeng','age':18},
#
# ]
#
#
# # l=[3,1,6,7,4,2]
# # l1=[3,1,'a',7,4,2]
# # print(sorted(l))
# # print(sorted(l1))       #排序本质就是在比较大小,不同类型之间不可以比较大小
#
# print(sorted(people,key=lambda dic:dic['age']))


# name_dic={
#     "abyuanhao":11900,
#     "alex":1200,
#     "wupeiqi":300
# }
#
# print(sorted(name_dic,key=lambda key:name_dic[key]))
# print(sorted(zip(name_dic.values(),name_dic.keys())))


print(str('1'))
print(type(str({'a':1})))
dic_str=str({'a':1})
print(type(eval(dic_str)))


tuple()     #元祖

l=[1,2,3,4]
print(sum(l))
print(sum(range(5)))
print(type(l))


msg='123'

if type(msg) is str:
    msg=int(msg)
    res=msg+1
    print(res)



def test():
    msg='和我符合欧我环境佛ID回家我集合分'
    print(locals())
    print(vars())

test()


print(vars(int))


# import----->sys------->__import__()
# import  'test'  #会报错,不能导入字符串类型
module_name='test'
m=__import__(module_name)   #调用的是字符串类型