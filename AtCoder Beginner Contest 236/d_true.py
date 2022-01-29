# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:03:38 2022

@author: terad
"""

 
N = int(input())
A = [[-1] * (2*N) for i in range(2*N-1)]
#2進数で残った人を管理(1:残っていない 0:残っている)
hito = 0
ans = 0
 
for i in range(2*N-1):
    A[i][i+1:] = map(int,input().split())
 
def  dfs(hito,B):
    global ans
    
    #葉に到達した場合ansを更新
    if hito == 2**(2*N)-1:
        ans = max(B,ans)
        return
    
    #残った人の最小値を求める
    for i in range(2*N):
        if hito | 1<<i != hito:
            p1 = i
            hito |= 1 << i
            break
            
    #ペアの人を求める
    for j in range(p1+1,2*N):
        if hito | 1<<j != hito:
            p = j
            dfs(hito | 1 << j, B^(A[p1][p]))
            
dfs(hito,0)
print(ans)