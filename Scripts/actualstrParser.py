# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 18:56:02 2014

@author: cloud
"""
import csv
filename1 = r'C:\Users\Windows User\Desktop\Work\Typhoons\Actual_strength_summary_5.csv'
#filename2 = r'.csv'
#filename3 = r'.csv'
#filename4 = r'.csv'


reader1 = csv.reader(open(filename1))
#reader2 = csv.reader(open(filename2))
#reader3 = csv.reader(open(filename3))
#reader4 = csv.reader(open(filename4))

#pseudocode
for row in reader1:
    if 'SS' in row[0].strip()[-2:]:
        print row[0]
    if 'ST' in row[0].strip()[-2:]:
        print row[0]