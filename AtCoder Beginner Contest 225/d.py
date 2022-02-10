# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 22:02:14 2022

@author: terad
"""
"""
双方向連結リストをつかう
リスト２つ用意して前後関係を保存するだけ
"""

N,Q = map(int,input().split())
pre = [-1] * (N+1)
post = [-1] * (N+1)

for i in range(Q):
    q,*xy = map(int,input().split())
    
    if q == 1:
        x,y = xy
        pre[y] = x
        post[x] = y

            
    elif q == 2:
        x,y = xy
        pre[y] = -1
        post[x] = -1
        
                   
    else:
        p = xy[0]
        while True:
            if pre[p] != -1:
                p = pre[p]
            else:
                break
        
        ans = []
        while True:
            if p != -1:
                ans.append(p)
                p = post[p]
            else:
                print(len(ans),*ans)
       
            
            
        
            
            
            
        