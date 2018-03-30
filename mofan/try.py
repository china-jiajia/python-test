#!/usr/bin/env python
# -*- coding utf8 -*-

try:

    file = open('eee','r+')

except Exception as e:
    # print(e)
    print('there is no file named as eeee')
    response = input('do you want to create a new file: ')
    if response == 'y':
        file = open('eee','w')
    else:
        pass
else:
    file.write('ssss')
file.close()