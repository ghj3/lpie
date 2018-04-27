#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:08:30 2018

@author: k3sekido
"""
class genPrimes(object):

    def __init__(self):
        self.primes = []
        self.IDX=0
    def __iter__(self):
        return self
    def genPrimes(self):
        return self
    def __next__(self):
        if len(self.primes)==0:
            self.primes.append(2)
            self.IDX=0
            return 2
        a=self.primes[self.IDX]
        
        while True:
            a+=1
            flg=False
            for n in self.primes:
                if a%n==0:
                    flg=True
            if flg==False:
                break
            
        self.primes.append(a)
        self.IDX+=1            
        return a
primeGenerator = genPrimes()
print(primeGenerator.__next__())