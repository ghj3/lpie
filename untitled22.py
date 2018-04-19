#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:46:29 2018

@author: k3sekido
"""

def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

print(fancy_divide([0, 2, 4], 1))
print(fancy_divide([0, 2, 4], 4))
print(fancy_divide([0, 2, 4], 0))