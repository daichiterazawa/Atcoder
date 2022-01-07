# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:06:14 2021

@author: terad
"""

N = int(input())
S = list(input())
Q = int(input())
cnt = 0

for _ in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        a -= 1
        b -= 1
        
        #反転してるときのa,bを求める
        if cnt:
            if a >= N :
                a -= N
            else:
                a += N
            
            if b >= N :
                b -= N
            else:
                b += N
                
        S[a],S[b] = S[b],S[a]
        
    else:
        cnt ^= 1
        
if cnt == 0:
    print(*S, sep='')
else:
    print(*(S[N:]+S[:N]), sep='')
        
            
    
