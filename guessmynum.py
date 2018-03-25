#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:21:29 2018

@author: k3sekido
"""
st=0
ed=100
print("Please think of a number between 0 and 100!")
while True:
    hp = int((ed + st) / 2)
    print("Is your secret number " + str(hp) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans =='h':
        ed = hp
    elif ans == 'l':
        st = hp
    elif ans == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(hp))

