# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:19:54 2021

@author: terad
"""

S = list(input())
T = list(input())
if ord(T[0]) >= ord(S[0]):    
    k = ord(T[0]) - ord(S[0])
else:
    k = ord(T[0])+26 - ord(S[0])
check = 0
for i in range(len(S)):
    if ord(T[i]) >= ord(S[i]):
        if ord(T[i]) - ord(S[i]) != k:
            check = 1
    else:
        if ord(T[i])+26 - ord(S[i]) != k:
            check = 1
        
print('Yes' if check == 0 else 'No')