#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:55:04 2018

@author: k3sekido
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
print(a(False, 2, 3))
print(type(a(False, 2, 3)))

print(b(3, 2))
print(type(b(3, 2)))




a = 10
def f(x):
    return x + a
a = 3
print(f(1))


x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
print(g(x))