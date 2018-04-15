#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:02:12 2018

@author: k3sekido
"""

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print(listA.sort())

listA.insert(0, 100)
listA.remove(3)
listA.append(7)

print(listA)

print(listA + listB)
listB.sort() 
print(listB.pop())

print(listB.count('a'))

#listB.remove('a')

listA.extend([4, 1, 6, 3, 4])
print(listA.count(4))
print(listA.index(1))
print(listA.pop(4))
print(listA.reverse())
print(listA)