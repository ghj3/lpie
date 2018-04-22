#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:23:50 2018

@author: k3sekido
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    l=0
    for v in hand.values():
        l+=v
    return l
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
print(calculateHandlen(hand))