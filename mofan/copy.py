#!/usr/bin/env python
# -*- coding utf8 -*-

# import copy
#
# a = [1,2,3]
# b = a
#
# # id(a)
# # id(b)
#
# # 浅的copy
# c = copy(a)


import copy
a = [1,2,3]
b = a
id(a)

id(b)

print(id(a) == id(b))

c = copy.copy(a)
print(id(c) == id(a))

# 完完全全copy(没有任何内存空间是相同的)
e = copy.deepcopy(a)