#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:53:58 2018

@author: k3sekido
"""

def dict_invert(d):
    o={}
    for key in d.keys():
        if d[key] in o.keys():
            a=o[d[key]]
        else:
            a=[]
        a.append(key)
        a.sort()            
        o[d[key]]=a
    return o
    
    
d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))