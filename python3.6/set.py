#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


#集合内置方法

# s=set('hello')
#
# v=set(['alex','alex','sb'])
#
#
# print(s,v)


#集合的内置方法

# s={'sb',1,2,3,4,5,6}

#添加元素
# s.add('s')
# print(s)

#清空
# s.clear()
# print(s)

#随机删
# s.pop()
# print(s)

#指定删(如果集合当中元素不存在会报错)
# s.remove('sb')
# print(s)

#指定删除(如果集合当中元素不存在不会报错)
# s.discard('sbbb')
# print(s)


# python_l=['lcg','szw','zjw',]
# linux_l=['lcg','szw','sb']
#
# p_s=set(python_l)
# l_s=set(linux_l)
#
# #求交集
# print(p_s,l_s)
# print(p_s.intersection(l_s))
# print(p_s&l_s)
#
# #求并集
# print(p_s.union(l_s))
# print(p_s|l_s)
#
#
# #求差集
# print('差集: ',p_s-l_s)
# print(p_s.difference(l_s))
# print('差集: ',l_s-p_s)
# print(l_s.difference(p_s))




#交叉补集
# python_l=['lcg','szw','zjw','lcg']
# linux_l=['lcg','szw','sb']
#
# p_s=set(python_l)
# l_s=set(linux_l)
#
# # p_s=p_s-l_s
# p_s.difference_update(l_s)
# print(p_s)


#无交集
# s1={1,2}
# s2={3,5}
# print(s1.isdisjoint(s2))


#父集子集
# s1={1,2}
# s2={1,2,3}
# print(s1.issubset(s2))  #s1 是 s2 的子集
# print(s2.issubset(s1))  #False
#
# print(s2.issuperset(s1)) #s1 是s2 的父集


#更新值
# s1={1,2}
# s2={1,2,3}
#
# # s1.update(s2)   #更新多个值
# # s1.add(1,2,3,4) #只能更新一个值
# s1.union(s2)    #不更新
# print(s1)


# 1.集合是可变类型
#定义不可变集合
#s=frozenset('hello')
#print(s)

# 2.简单去重
# names = ['alex','alex','wupeiqi']
# s = set(names)
# print(s)
# names=list(s)
# print(names)