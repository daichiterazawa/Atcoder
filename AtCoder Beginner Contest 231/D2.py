# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:20:41 2022

@author: terad
"""

def dfs(x,y):
    global ans,check
    
    if 0<=x<=W-1 and 0<=y<=H-1 and C[y][x] != '#':
        C[y][x] = '#'
        check += 1
        
    else :
        return
    
    dfs(x+1,y)
    dfs(x,y+1)
    
    if ans <= check:
        ans = check
    check -= 1 
    
H,W = map(int,input().split())
C = [list(input()) for _ in range(H)]
ans = 0
check = 0
sx,sy = 0,0

dfs(sx,sy)

print(ans)

    
    
        
    