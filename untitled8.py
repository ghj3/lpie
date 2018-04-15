#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:56:47 2018

@author: k3sekido
"""

x = [1, 2, [3, 'John', 4], 'Hi'] 
print(x[0])
print(type(x[0]))

print(x[2])
print(type(x[2]))

print(x[-1])
print(type(x[-1]))

print(x[2][2])
print(type(x[2][2]))

print(x[0:1])
print(type(x[0:1]))

print(2 in x)
print(type(2 in x))

print(3 in x)
print(type(3 in x))

x[0] = 8
print(x)