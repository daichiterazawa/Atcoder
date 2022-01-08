# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:45:03 2022

@author: terad
"""

t = int(input())


f = t**2 + 2*t + 3
ff = f**2 + 2*f + 3
fft = (f+t)**2 + 2*(f+t) + 3
fff = (fft+ff)**2 + 2*(fft+ff) + 3

print(fff)

