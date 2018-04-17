#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:13:36 2018

@author: k3sekido
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for c in list(secretWord):
        if c not in lettersGuessed:
            return False
    
    return True
    
secretWord = 'durian' 
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
print(isWordGuessed(secretWord, lettersGuessed))
    