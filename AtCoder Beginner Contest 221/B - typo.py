# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 14:35:10 2021

@author: terad
"""
import copy
S = list(input())
T = list(input())
check = 0
if S==T:
    check += 1 
else:
    for i in range(len(S)-1):
        tmp = copy.copy(S)
        tmp[i] = S[i+1]
        tmp[i+1] = S[i]
        if tmp == T:
            check += 1
            
print('Yes' if check==1 else 'No')
        
    
        
        
        
        
    