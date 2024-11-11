# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:57:12 2021

@author: BACKUPPC
"""

import pypyodbc
import pandas as pd

con = pypyodbc.connect("Driver={SQL Server Native Client 11.0};Server=192.168.1.67;database=cidb3840;uid=sa;pwd=@abc123;")

df = pd.read_sql_query("select * from item",con)