#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:41:13 2018

@author: k3sekido
"""
s="azcbobobegghakl"
i=0
counter=0
while i <=len(s)-3:
    if s[i:i+3]=="bob":
        counter+=1
    i+=1
print("Number of times bob occurs is: "+str(counter))