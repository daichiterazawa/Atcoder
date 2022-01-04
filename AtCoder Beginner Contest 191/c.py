# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:08:21 2022

@author: terad
"""

H,W = map(int,input().split())
S = [['.'] * W  for i in range(H)]
ans = 0

for i in range(H):
    S[i] = list(input())
    

for i in range(0,H-1):
    for j in range(0,W-1):
        check = 0
        
        
        if S[i][j] == '#':
            check += 1 
        
        if S[i+1][j] == '#':
            check += 1
        
        if S[i][j+1] == '#':
            check += 1
            
        if S[i+1][j+1] == '#':
            check += 1
                
        if check == 1 or check == 3:
            ans += 1
    
print(ans)
