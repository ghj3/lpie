#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:02:33 2018

@author: k3sekido
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
print(rem(2, 5))
print(rem(5, 5))
print(rem(7, 5))