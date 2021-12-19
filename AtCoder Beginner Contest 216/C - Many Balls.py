# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:34:23 2021

@author: terad
"""

N = int(input())
ans = []

#奇数ならa 偶数ならb
while N != 0:
    if N % 2 == 0:
        ans.append('B')
        N = N//2
    else :
        ans.append('A')
        N = N - 1
        
for i in range(len(ans)):
    print(ans[len(ans)-i-1],end='')