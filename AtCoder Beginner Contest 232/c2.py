# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 22:03:35 2021

@author: terad
"""

N,M = map(int,input().split())
takahasi = []
sunuke = []
sunuke2 = []
check = 0

for m in range(M):
    A,B = map(int,input().split())
    if A <= B:
        takahasi.append([A-1,B-1])
    else :
        takahasi.append([B-1,A-1])
        
    takahasi.sort()
    
for m in range(M):
    A,B = map(int,input().split())
    sunuke.append([A-1,B-1])
    
for a in range(N):
    for b in range(N):
        sunuke2 = []
        for m in range(M):
            A,B = sunuke[m]
            A = (A + a) % 4
            B = (B + b) % 4
            if A <= B:
                sunuke2.append([A,B])
            else:
                sunuke2.append([B,A])
        sunuke2.sort()
        if takahasi == sunuke2:
            check = 1

print('Yes' if check == 1 else 'No')
    
            
        
