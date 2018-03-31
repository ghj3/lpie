#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 19:16:47 2018

@author: k3sekido
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    big = 0
    small = 0
    while True:
        if a > b:
            big = a
            small = b
        else:
            big = b
            small = a
        aa = big % small
        if aa == 0:
            break
        a = small
        b = aa
    return small
def isIn(char, aStr):
    print(aStr)
    if len(aStr)==0:
        return False
    if len(aStr)==1:
        pos = 0
    else:
        pos = int(len(aStr)/2)
    if aStr[pos] == char:
        return True
    elif aStr[pos] > char:
        return isIn(char, aStr[0:pos])
    else:
        if pos+1>=len(aStr):
            return False
        else:
            return isIn(char, aStr[pos+1:len(aStr)])
    
print(isIn('d', 'bbcefghhkmmmnoxy'))    
    