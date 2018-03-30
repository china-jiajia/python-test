#!/usr/bin/env python
# -*- coding utf8 -*-

a = [1,2,3,4,2,3,1,1]
# a.insert(1,0)

#去掉一个值(不是去除key， 这里去除的是第一个出现的'2')
# a.remove(2)

# print(a)

# 指数打印
# print(a[0])
# print(a[-1])
# print(a[0:3])
# print(a[:3])
# print(a[3:5])

# 打印一个value的索引值
# print(a.index(3))

# 统计
# print(a.count(2))

# 正向排序
# a.sort()
# print(a)

# 反向排序
a.sort(reverse=True)
print(a)