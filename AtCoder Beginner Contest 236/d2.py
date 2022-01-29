# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:23:20 2022

@author: terad
"""
import copy
 
N = int(input())
A = [[-1] * (2*N) for i in range(2*N-1)]
hito = list(range(2*N))
ans = 0
 
for i in range(2*N-1):
    A[i][i+1:] = map(int,input().split())
 
def  dfs(hito,B):
    global ans
    
    #葉に到達した場合ansを更新
    if hito == []:
        ans = max(B,ans)
        return
    
    #hitoとpairを更新    
    p1 = hito.pop(0)
    for i,p in enumerate(hito):
        tmp_hito = copy.deepcopy(hito)
        tmp_hito.pop(i)
        dfs(tmp_hito,B^(A[p1][p]))
 
        
dfs(hito,0)
print(ans)


    