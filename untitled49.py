#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:51:42 2018

@author: k3sekido
"""

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]
#print(a[0])
#print(b[1])
#print(a[a[1]])
#print(b[b[2]])
#print(a[b[2]])
#print(c[a[b[3]]])
#print(a[c[a[b[0]]]])
#print(a[c[a[b[3]]]])


def foo(L):
    val = L[0]
    while (True):
        val = L[val]
#foo(c)

num = 0
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

#print(val)

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
    
print(modSwapSort(a))