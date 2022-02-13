# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:25:07 2022

@author: terad
"""
import sys
from collections import Counter

S = list(input())
l = len(S)
syu = set()

if len(S) == 1:
    num = int(S[0])
    if num % 8 == 0:
        print('Yes')
        sys.exit()
        
elif len(S) == 2:
    num1 = int(S[1])+int(S[0])*10
    num2 = int(S[0])+int(S[1])*10
    if num1 % 8 == 0 or num2 % 8 == 0:
        print('Yes')
        sys.exit()
        
else:
    check = Counter(S)
    
    for i in ['1','2','3','4','5','6','7','8','9']:
        for j in ['1','2','3','4','5','6','7','8','9']:
            for k in ['1','2','3','4','5','6','7','8','9']:
                target = Counter([i,j,k])
                x = 0
                for l in ['1','2','3','4','5','6','7','8','9']:
                    if check[l] < target[l]:
                        x = 1
                        break
                if x == 0 and int(''.join([i,j,k]))%8==0 :
                    print('Yes')
                    sys.exit()
print('No')
    

