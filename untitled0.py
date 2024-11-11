# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:40:13 2021

@author: BACKUPPC
"""

import random

print(random.randrange(10,20))

x = ['a','b','c','d','e','f']

print(random.choice(x))

random.shuffle(x)

print(x)

print(random.random())