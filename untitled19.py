#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:27:56 2018

@author: k3sekido
"""

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)
  
