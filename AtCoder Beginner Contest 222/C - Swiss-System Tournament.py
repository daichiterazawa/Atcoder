# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:24:13 2021

@author: terad
"""

N,M = map(int,input().split())
A = []
win_num = []

#勝利数、個人識別
for i in range(2*N):
    win_num.append([0,i])

#入力受け取り
for n in range(2*N):
    A.append(list(input()))

#出す手を数字に変換
D = {
     'G':{'C':1,'P':2},
     'C':{'G':2,'P':1},
     'P':{'G':1,'C':2}
     }

#勝負開始
for m in range(M):
    for n in range(N):
        #人
        h1 = win_num[2*n][1]
        h2 = win_num[2*n+1][1]
        #手
        t1 = A[h1][m]
        t2 = A[h2][m]
        
        if t1 != t2:
            battle = D[t1][t2]
            if battle == 1:
                win_num[2*n][0] -= 1
            else :
                win_num[2*n+1][0] -= 1
                
    #勝利数でソート
    win_num.sort()
    
for i in range(2*N):
    print((win_num[i][1])+1)
    
    
    