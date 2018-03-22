#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:41:13 2018

@author: k3sekido
"""
s="azcbobobegghakl"
bf=""
output=""
output2=""
for aaa in s:
    if bf <= aaa:
        output+=aaa            
    else:
        if len(output) > len(output2):
            output2=output
        output=aaa            
    bf=aaa    
if len(output) > len(output2):
    output2=output
print("Longest substring in alphabetical order is: " + output2)