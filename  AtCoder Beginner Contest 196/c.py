# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:57:16 2022

@author: terad
"""

N = int(input())
na = len(str(N)) #桁数の判定
ans = 0

#少なくとも以下の数は含まれる
ans += 10**((na-1)//2) - 1

#Nの前半桁後半桁を取得
if na%2 == 0:   
    top,down = divmod(N,10**(na//2))
    a = top - 10**(na//2-1) + 1
    b = down - 10**(na//2-1) + 1
    if a >= 0 and b >= 0:
        if a <= b:
            ans += a
        else:
            ans += b

print(ans)
    





