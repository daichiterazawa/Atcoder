# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 22:53:31 2022

@author: terad
"""

H,W,X,Y = map(int,input().split())
S = []
ans = 1

for h in range(H):
    S.append(list(input()))

x,y = X-1,Y-1

for i in range(1,101):
    if x-i>=0 and S[x-i][y] == '.':
        ans += 1
    else:
        break
    
for i in range(1,101):
    if x+i <= H-1 and S[x+i][y] == '.':
        ans += 1
    else:
        break
    
for i in range(1,101):
    if y-i>=0 and S[x][y-i] == '.':
        ans += 1
    else:
        break
    
for i in range(1,101):
    if y+i <= W-1 and S[x][y+i] == '.':
        ans += 1
    else:
        break
    
print(ans)
    
        