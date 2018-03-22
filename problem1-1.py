#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:41:13 2018

@author: k3sekido
"""
s="azcbobobegghakl"
counter=0
for value in s:
    if value=='a' or value=='i' or value=='u' or value=='e' or value=='o':
        counter+=1
print("Number of vowels: " + str(counter))