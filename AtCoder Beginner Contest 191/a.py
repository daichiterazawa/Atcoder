# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:45:31 2022

@author: terad
"""

V,T,S,D = map(int,input().split())

print('No' if V*T <= D <= V*S else 'Yes')