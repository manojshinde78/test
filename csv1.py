# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:38:01 2021

@author: BACKUPPC
"""

import csv

open('heart.csv') as testcsvfile
csv_reader = csv.reader(testcsvfile, delimiter=',')
line_count = 0
for row in csv_reader:
    print(row[1])