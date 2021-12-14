# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:06:36 2021

@author: terad
"""

S = input()
N = len(S)
S_list = []

for i in range(N):
    S_list.append(S[i:N]+S[0:i])
    
print(min(S_list))
print(max(S_list))


    