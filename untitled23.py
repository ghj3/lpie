#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:48:02 2018

@author: k3sekido
"""

def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

print(fancy_divide([0, 2, 4], 1))
print(fancy_divide([0, 2, 4], 4))
print(fancy_divide([0, 2, 4], 0))