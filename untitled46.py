#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 00:10:20 2018

@author: k3sekido
"""

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
print(Accio())