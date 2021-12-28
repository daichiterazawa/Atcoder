# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 20:17:41 2021

@author: terad
"""

n,x = map(int,input().split())
l_list = [0]
a_list = [0]
ans = 0
num = 1

def product(i,j,ans,num):
    print(i,j)
    #リストのフローを除外
    if not(1<=i<=n) or not(1<=j<=l_list[i]):
        return
    #総積がXかどうかの判定
    elif i == n and num*a_list[i][j]==x:
        ans += 1
        return
    
    num *= a_list[i][j]
    print(num)
    product(i+1,j,ans,num)
    product(i,j+1,ans,int(num/a_list[i][j]))
        
    
for _ in range(n):
    l,*a = map(int,input().split())
    l_list.append(l)
    a_list.append([0]+a)

#スタートを宣言
si,sj = 1,1
product(si,sj,ans,num)

print(ans) 
    