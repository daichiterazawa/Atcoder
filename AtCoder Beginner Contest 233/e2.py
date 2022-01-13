# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:05:17 2022

@author: terad
"""
from itertools import accumulate
def solve():
    X = list(input())
    Y = [int(x) for x in X]
    Z = list(accumulate(Y))[::-1]
    
    res = 0
    rem =[]
    
    for z in Z:
        res += z
        rem.append(res%10)
        res //= 10
        
        
    while res != 0:
        rem.append(res%10)
        res //= 10
        
    ans = rem[::-1]
    print(*ans, sep='')

if __name__ == '__main__':
    solve()
