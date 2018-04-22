#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:36:49 2018

@author: k3sekido
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    t=0
    while True:
        print("Current Hand:  ", end="")
        displayHand(hand)
        print('Enter word, or a "." to indicate that you are finished: ', end="")
        word=input()
        if word==".":
            print("Goodbye! Total score: "+str(t)+" points.")
            break
        if isValidWord(word, hand, wordList)==True:
            p=getWordScore(word,n)
            t=t+p
            print('"'+word+'" earned '+str(p)+' points. Total: '+str(t)+' points')
            hand=updateHand(hand,word)
            if calculateHandlen(hand)==0:
                print("Run out of letters. Total score: "+str(t)+" points.")
                break
        else:
            print("Invalid word, please try again.")
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
wordList = loadWords()
playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)