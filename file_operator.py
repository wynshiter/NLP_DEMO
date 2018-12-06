# encoding: utf-8
'''
@author: season
@contact: seasonwang@insightzen.com

@file: file_operator.py
@time: 2018/11/23 15:24
@desc:
'''

import os

def all_pure_file_name_without_extension(file_dir,extension):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            print(os.path.splitext(file)[1])
            if os.path.splitext(file)[1] == extension:

                L.append(os.path.splitext(file)[0])
    return L


def all_file_name_with_extension(file_dir,extension):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            print(os.path.splitext(file)[1])
            if os.path.splitext(file)[1] == extension:

                L.append(os.path.splitext(file)[0]+os.path.splitext(file)[1])
    return L

# #获取当前集合在大集合中没有出现的
# def sub_list(big,small):
#     result = list(set(big).intersection(set(small)))
#     result = list(set(small)-set(result))
#
#     return  result



# l = file_name(r'./html/')
# print(l)