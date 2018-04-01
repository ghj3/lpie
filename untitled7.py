#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:25:09 2018

@author: k3sekido
"""

balance = 999999
annualInterestRate = 0.18

def whetherPaidoff(b,r,p):
    for month in range(12):
        b = float(b) - p
        b = float(b) + float(b) * r
    
    return b
monthlyInterestRate=annualInterestRate/12.0
lowpayment=balance/12
upperpayment=balance*(1+monthlyInterestRate)**12/12.0
print("low"+str(lowpayment))
print("upp"+str(upperpayment))

while True:
    minPayment=(upperpayment+lowpayment)/2.0
    if lowpayment >= minPayment or upperpayment <= minPayment:
        break
    ret=whetherPaidoff(balance,monthlyInterestRate,minPayment)
    print("ret"+str(ret))    
    if ret > 0.0:
        lowpayment=minPayment
    else:
        upperpayment=minPayment
print("Lowest Payment: "+str(round(minPayment,2)))