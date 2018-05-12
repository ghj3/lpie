#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:15:28 2018

@author: k3sekido
"""
class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')


def faa(n):
    def g(m):
        m = 0
        for i in range(m):
            print(m)
    for i in range(n):
        g(n)

n=10
for i in range(0):
    print(n)
