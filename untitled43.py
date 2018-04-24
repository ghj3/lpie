#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 23:28:10 2018

@author: k3sekido
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, e):
        ee=intSet()
        for v in self.vals:
            if v in e.vals:
                ee.vals.append(v)                
        return ee
    def __len__(self):
        return len(self.vals)
s1=intSet()
s1.vals=[-19,-15,-12,-4,3,11,12,16,18]
s2=intSet()
s2.vals=[-13,-10,-9,0,3,6,11,12,16]
print(s1.intersect(s2))
print(len(s1))
