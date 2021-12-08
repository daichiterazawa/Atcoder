# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:40:15 2021

@author: terad
"""
A,B = map(int, input().split())

check = 0
for _ in range(19):
    
    target_A = A % 10
    target_B = B % 10
    A = A // 10
    B = B // 10
    
    if target_A + target_B >= 10:
        check = 1
    
    
print('Hard' if check == 1 else 'Easy')
    