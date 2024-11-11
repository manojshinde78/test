# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:29:55 2021

@author: BACKUPPC
"""

import os
import numpy as np
import pandas as pd

PATH = '';

def read_csv(filename):
    file = os.path.join(PATH, filename)
    return pd.read_csv(file)

train = read_csv("train.csv")
train["Age"].value_counts()
print(train["Cabin"].value_counts())