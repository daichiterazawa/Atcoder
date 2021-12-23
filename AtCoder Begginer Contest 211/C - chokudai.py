# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:39:28 2021

@author: terad
"""

S = [False] + list(input())
T = [False,'c','h','o','k','u','d','a','i']

#dp[i][j]を'chokudai'のi文字目をSのj文字目で表現すると定義
dp = [[0]*(len(S)) for _ in range(9)]


for j in range(len(S)):
    dp[0][j] = 1

    
for i in range(1,9):
    for j in range(1,len(S)):
        if S[j] == T[i]:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            
        else:
            dp[i][j] = dp[i][j-1]
            
print(dp[8][len(S)-1] %(10**9+7))
