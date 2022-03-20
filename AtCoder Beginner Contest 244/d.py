# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:44:26 2022

@author: terad
"""

S = list(map(str,input().split()))
T = list(map(str,input().split()))
check = 0

for i in range(3):
    if S[i] == T[i]:
        check += 1
        
if check == 3:
    print('Yes')
elif check == 1:
    print('No')
else:
    print('Yes')
        
