#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:40:16 2018

@author: k3sekido
"""

def score(word, f):
    dic="abcdefghijklmnopqrstuvwxyz"
    i=0
    sc=[]
    for w in word.lower():
        sc.append(i*(dic.find(w)+1)) 
        i=i+1
    sc.reverse()
    return f(sc[0],sc[1])

def sfafs(a,b):
    return a+b

print(score("AAAAA",sfafs))
