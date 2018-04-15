#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:22:54 2018

@author: k3sekido
"""
testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
        
def timesFive(a):
    return a * 5

#applyToEach(testList, timesFive)

def absDivideFive(a):
    print(a)
    if a > 0:
        return int(a/5)
    else:
        return int(a/-5)
    
#applyToEach(testList, absDivideFive)

def powerabs(a):
    return a * a
applyToEach(testList, powerabs)
print(testList)        