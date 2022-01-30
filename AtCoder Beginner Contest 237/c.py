# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:55:51 2022

@author: terad
"""

import sys
S = list(input())[::-1]

for i in range(len(S)):
    if S[i] != 'a':
        A = S[i:]
        break
    
    if i == len(S)-1:
        print('Yes')
        sys.exit()
        
B = A[::-1]

for j in range(len(S)):
    if B[j] != 'a':
        C = B[j::]
        break
        
print('Yes' if C == C[::-1] else 'No')