#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 09:29:37 2018

@author: k3sekido
"""
balance = 3926
annualInterestRate = 0.2

def whetherPaidoff(b,r,p):
    for month in range(12):
        b = float(b) - float(p)
        b = float(b) + float(b) * r
    
    return b <= 0.0
minPayment=10
monthlyInterestRate=annualInterestRate/12.0
while True:
    if whetherPaidoff(balance,monthlyInterestRate,minPayment):
        break
    minPayment+=10
    
print("Lowest Payment: "+str(minPayment))
            