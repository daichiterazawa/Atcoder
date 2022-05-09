# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:31:32 2022

@author: terad
"""

N = int(input())
A = [1]+[1]+[0 for i in range(10**6-1)]
sosu = []
ans = 0
for i in range(2,10**6+1):
    for j in range(2,(10**6)//i+1):
        A[i*j] = 1
        
for x,a in enumerate(A[:int(N**(1/3))]):
    if a != 1:
        sosu.append(x)
        

for i in range(1,len(sosu)):
    if sosu[i-1] * sosu[i]**3 <= N:
        ans += i
        
    else:
        for j in range(1,i):
            if sosu[j] + sosu[i]**3 <= N:
                ans += 1
                
print(ans)
    
        
    