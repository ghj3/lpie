#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:54:06 2018

@author: k3sekido
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word not in wordList:
        return False
    dic={}
    for k in hand:
        dic[k]=hand[k]    
    for w in word:
        a=dic.get(w,0)
        if a > 0:
            dic[w]=a-1
        else:
            return False
    return True
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList
wordList=loadWords()
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
word = "rapture"


print(isValidWord(word,hand,wordList))