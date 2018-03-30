# -*- coding: utf-8 -*-

print('hello world!')


for i in range(1,10):
	for j in range(1,i+1):
			print('{}x{}\t'.format(i,j,i*i),end='')
	print()