# -*- coding: utf-8 -*-

from functools import reduce 

def row(x):
	# return ' '.join(list(map(str,reduce(lambda x,y:list(map(sum,zip([0]+x,x+[0]))),range(x),[1]))))
	return ' '.join(list(map(str,reduce(lambda x,y:list(map(sum,zip([0]+x,x+[0]))),range(x),[1]))))

# def pascal(x):
# 	return '\n'.join(row(i).center(len(row(x-1)))for i in range(x))

def pascal(x):
    return '\n'.join(row(i).center(len(row(x-1))) for i in range(x))

print(pascal(10))
	
	