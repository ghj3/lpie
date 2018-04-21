#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:35:01 2018

@author: k3sekido
"""

def getSublists(L, n):
    a = []
    s=0
    e=n
    for i in range(len(L)-n+1):        
        a.append(L[s:e])
        s+=1
        e+=1
    return a
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n=4
print(getSublists(L,n))