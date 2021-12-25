# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:08:16 2021

@author: terad
"""

A,B,C,D = map(int,input().split())
mizu = A + B
aka = C
ans = 1
if B/C < D:
    while mizu/aka > D:
        ans += 1
        mizu += B
        aka += C
else:
    ans = -1
    
print(ans)