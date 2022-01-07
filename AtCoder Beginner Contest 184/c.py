# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 11:43:25 2022

@author: terad
"""

a,b = map(int,input().split())
c,d = map(int,input().split())

#0手を調べる
if a == c and b == d :
    print(0)

elif a+b == c+d or a-b == c-d or abs(a-c)+abs(b-d) <= 3:
    print(1)

elif a-4-abs(d-b) <= c <= a+4+abs(d-b) and b-4-abs(c-a) <= d <= b+4+abs(c-a):
    print(2)
elif (a == c and abs(b-d)<=6) or (abs(a-c) <= 6 and b==c):
    print(2)
elif (abs(a-c) <= 5 and abs(b-d) <= 2) or (abs(a-c) <= 2 and abs(b-d) <= 5):
    print(2)
elif (a+b+c+d) // 2 == 0:
    print(2)    
else:
    print(3)