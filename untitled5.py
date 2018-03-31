#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 23:11:01 2018

@author: k3sekido
"""

# code for eDX course, 2018


# library with tan function and math constans
import math

# definition of the functon, n - number of sides, s - side lentght
def polysum(n, s):
    '''
    function to calculate area plus square perimeter
    '''
    # perimeter of polysum is equal borders lenght
    perimeter=n*s

    # from definition of aquare area:
    area=0.25*n*s*s/math.tan(math.pi/n)
    
    total=area+perimeter*perimeter

    #function round leaves result with 4 numbers after dot
    return round(total, 4)