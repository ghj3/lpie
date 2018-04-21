#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:23:33 2018

@author: k3sekido
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    r=b
    i=0
    while r<=x:
        r=r*b
        i=i+1
    return i

print(myLog(16,2))