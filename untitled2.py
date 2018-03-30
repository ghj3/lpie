#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:48:43 2018

@author: k3sekido
"""
def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  
print(a(6))
print(type(a(6)))
print(a(-5.3))
print(type(a(-5.3)))
print(a(a(a(6))))
print(type(a(a(a(6)))))
print(c(a(1), b(1)))
print(type(c(a(1), b(1))))
print(e(a(3), b(4), c(3, 4)))
print(type(e(a(3), b(4), c(3, 4))))
print(f)
print(type(f))