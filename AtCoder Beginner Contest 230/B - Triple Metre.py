# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:19:59 2021

@author: terad
"""

S = list(input())
S_size = len(S)

check = list("oxxoxxoxxoxx")

if S == check[:S_size] or S == check[1:S_size+1] or S == check[2:S_size+2]:
    print("Yes")
    
else:
    print("No")
    




