#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 09:14:31 2018

@author: k3sekido
"""
balance=5000.00
monthlyPaymentRate=0.02
annualInterestRate=0.18

for month in range(12):
    balance = balance - (balance*monthlyPaymentRate)
    balance = balance + balance * annualInterestRate / 12.0
    
print("Remaining balance: "+str(round(balance,2)))
    