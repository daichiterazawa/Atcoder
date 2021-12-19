# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:10:53 2021

@author: terad
"""
N = int(input())
name_list = []
check = 0
for i in range(N):
    name = input()
    if name in name_list:
        check = 1
    name_list.append(name)    
print('Yes' if check == 1 else 'No')

    
    