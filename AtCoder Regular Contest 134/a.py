# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:53:09 2022

@author: terad
"""

N,L,W = map(int,input().split())
A = list(map(int,input().split()))
x = 0
ans = 0

"""
if A[0] != 0:
    ans += 1
    x = W
""" 
   
for a in A:
    if a + W > x >= a:
        x = a + W
        
    elif x < a:
        ans += (int((a-x-0.001)//W)+1)
        x = a+W
        

if x != L:
    ans += (int((L-x-0.001)//W)+1)
      
print(ans)

    