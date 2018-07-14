#!/bin/env python
# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# Purpose:     txt转换成Excel
# Author:      zhoujy
# Created:     2013-05-07
# update:      2013-05-07
#-------------------------------------------------------------------------------
import datetime
import time
import os
import sys
import xlwt #需要的模块
import csv



# file = open('file.txt','r')
# content = file.readlines()
# # second_read_time = file.readline()
# print(content)


with open('file1.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    # 读要转换的txt文件，文件每行各词间以@@@字符分隔
    with open('file.txt', 'rb') as filein:
        for line in filein:
            line_list = line.strip('\n').split(',')
            # spamwriter.writerow(line_list)
            #print(line_list)
            l_list=line_list[0].replace('\t',',').split(',')
            # print(l_list)
            spamwriter.writerow(l_list)








# import csv
#
#
# def get_lines(filepath):
#     with open(filepath) as file_object:
#         lines = set(file_object.readlines())
#         return lines
#
#
# def new_csv(lines):
#     fileindex = 0
#     count = len(lines)
#     print("总行数" + str(count))
#     for index, line in enumerate(lines):
#         index += 1
#         # print(str(index)+'_'+line)
#         oneline = line.strip()  # 逐行读取，剔除空白
#         if (index - 1) % 1000 + 1 == 1:
#             data = []
#             if len(oneline) == 11:
#                 data.append([oneline])
#         elif index % 1000 == 0 or index == count:
#             fileindex += 1
#             if len(oneline) == 11:
#                 data.append([oneline])
#             with open(str(fileindex) + '.csv', 'w') as csvfile:
#                 csv_writer = csv.writer(csvfile, dialect='excel')
#                 # csv_writer=csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                 csv_writer.writerows(data)
#         else:
#             if len(oneline) == 11:
#                 data.append([oneline])
#
#
# if __name__ == "__main__":
#     filepath = "file.txt"
#     lines = get_lines(filepath)
#     new_csv(lines)