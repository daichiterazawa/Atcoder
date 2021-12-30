# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:00:01 2021

@author: terad
"""

S = list(input())
on = []
xn = []
un = []

for i in range(10):
    if S[i] == 'o':
        on.append(str(i))
    elif S[i] == 'x':
        xn.append(str(i))
    else:
        un.append(str(i))
ans = 0

def judge(s):
    for o in on:
        if not(o in s):
            return False
    for x in xn:
        if x in s:
            return False
    return True

    
for i in range(10000):
    s = str(i).zfill(4)
    if judge(s) :
        ans += 1
        
print(ans)
