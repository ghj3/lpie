#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:38:31 2018

@author: k3sekido
"""


def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
        
x = "pi"
y = "pie"
x, y = y, x


a = f(3)
print(type(a))