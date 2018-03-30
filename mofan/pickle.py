#!/usr/bin/env python
# -*- coding utf8 -*-

import pickle

a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

file = open('pickle_example.pickle','web')
pickle.dump(a_dict,file)
file.close()

file = open('pickle_example.pickle','rb')
a_dict1 = pickle.load(file)
file.close()

print(a_dict1)


with open('pickle_example.pickle','rb') as file:
a_dict1 = pickle.load(file)

print(a_dict1)