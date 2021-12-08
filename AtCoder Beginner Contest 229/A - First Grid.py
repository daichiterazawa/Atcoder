# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:29:10 2021

@author: terad
"""

S1 = list(input())
S2 = list(input())

if S1[0] == '#' and S1[1] == '.':
    if S2[0] == '.' and S2[1] == '#':
        print('No')
    else:
        print('Yes')
        
elif S1[0] == '.' and S1[1] == '#':
    if S2[0] == '#' and S2[1] == '.':
        print('No')
    else:
        print('Yes')
else :
    print('Yes')
    