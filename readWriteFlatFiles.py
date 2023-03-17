# -*- coding: utf-8 -*-
"""
Reading and Writing CSVs and .xlsx files in Python
@author: Adam Fisher
"""

# import modules 
import pandas as pd
import os 

# check working directory
print(os.getcwd())

# read csv into variable
csv = pd.read_csv('TickerList.csv')

# read xlsx into variable
xlsx = pd.read_excel('TickerList.xlsx')

'''
perform operations
'''

# write csv from variable 
csv.to_csv('TickerList2.csv')

# write xlsx from variable 
xlsx.to_excel('TickerList2.xlsx')
