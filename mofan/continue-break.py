#!/usr/bin/env python
# -*- coding utf8 -*-

# a = True
#
# while a:
#     b = input('type something')
#     if b == '1':
#         a = False
#     else:
#         pass
#
# print('finsh run')



# break continue

# break 当条件满足时候，直接跳出循环
# while True:
#     b = input('type something')
#     if b == '1':
#         break
#     else:
#         pass
#     print('still in while')
#
# print('finsh run')


# continue 当条件满足时，接着执行下一个循环
while True:
    b = input('type something')
    if b == '1':
        continue
    else:
        pass
    print('still in while')

print('finsh run')