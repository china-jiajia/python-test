#!/usr/bin/env python
# -*- coding utf8 -*-
#

# 往文件中写入内容
# text = 'This is my first test.\nThis is next line.\nThis is last line.'
#
# print(text)
#
# my_file = open('my file.txt','w')
# my_file.write(text)
# my_file.close()


# 往文件中追加内容'a'为追加 'append'
append_text = '\nThis is append file.'

my_file = open('my file.txt','a')
my_file.write(append_text)
my_file.close()
