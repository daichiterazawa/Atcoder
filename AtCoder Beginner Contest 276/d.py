# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:51:02 2022

@author: terad
"""
import sys

def get_amari(A):
    cnt2,cnt3 = 0,0
    while (A%2==0 and A!=1):
        A /= 2
        cnt2 += 1
        
    while (A%3==0 and A!=1):
        A /= 3
        cnt3 += 1
        
    return A,cnt2,cnt3
        
        
N = int(input())
a_list = list(map(int,input().split()))
cnt2,cnt3 = [0 for i in range(N)],[0 for i in range(N)]
A1,cnt2[0],cnt3[0] = get_amari(a_list[0])
cnt2_min,cnt3_min = cnt2[0],cnt3[0]
for i in range(1,N):
    A,cnt2[i],cnt3[i]= get_amari(a_list[i])
    if A1 != A:
        print(-1)
        sys.exit()
        
    if cnt2_min > cnt2[i]:
        cnt2_min = cnt2[i]
    
    if cnt3_min > cnt3[i]:
        cnt3_min =cnt3[i]
        
ans = 0
for c2,c3 in zip(cnt2,cnt3):
    ans += c2-cnt2_min + c3-cnt3_min
    
print(ans)
    
        
    
    
