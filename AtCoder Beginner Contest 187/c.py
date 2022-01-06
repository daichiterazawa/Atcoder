# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:15:59 2022

@author: terad
"""

N = int(input())
A = set()
B = set()
check = 0
for _ in range(N):
    s = list(input())
    if s[0] != '!':
        A.add(''.join(s))
    else:
        B.add(''.join(s[1:]))
    
for a in A:
    if a in B:
        print(a)
        exit()

print('satisfiable')
    
            
            