# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:12:22 2022

@author: terad
"""
"""
ARC教訓：　乗算は使わない、//と%とうまく実装する
"""


N,L,W = map(int,input().split())
A = list(map(int,input().split())) + [L]

ans = A[0]//W + min(A[0] % W, 1)

for i in range(N):
    if A[i+1] > A[i] + W:
        ans += (A[i+1]-A[i]-W)//W + min((A[i+1]-A[i]-W) % W,1)
        
        
print(ans)


