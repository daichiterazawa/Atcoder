# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 22:15:30 2021

@author: terad
"""
import itertools

N,M = map(int,input().split())

AB = [[False] * N for _ in range(N)]
CD = [[False] * N for _ in range(N)]

#高橋君
for m in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    AB[A][B] = AB[B][A] = True
    
#青木君
for m in range(M):
    C,D = map(int,input().split())
    C -= 1
    D -= 1
    CD[C][D] = CD[D][C] = True
    
 
#高橋と青木の組み合わせ全探索
ans = 'No'
for p in  itertools.permutations(range(N)):
    check = True
    for i in range(N):
        for j in range(N):
            if AB[i][j] != CD[p[i]][p[j]]:
                check = False
    if check:
        ans = 'Yes'
        
print(ans)
           

