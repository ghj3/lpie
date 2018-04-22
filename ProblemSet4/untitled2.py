#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:28:10 2018

@author: k3sekido
"""
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    dic={}
    for k in hand:
        dic[k]=hand[k]
        
    for w in word:
        a=dic.get(w,0)
        a-=1
        dic[w]=a
    return dic        
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
print(updateHand(hand, 'quail'))
print(updateHand(hand, 'quail'))
