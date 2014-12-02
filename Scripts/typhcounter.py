# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 12:52:54 2014

@author: Windows User
"""

import csv
from collections import Counter

csvfile = r'C:\Users\Windows User\Desktop\LaUnionIlocosField Work\Ilocos.csv'
bagyo = []
read = csv.reader(open(csvfile))
next(read)
for row in read:
    bagyo.append(row[6])
new = [x for x in bagyo if x != '']
c = Counter(new)
#print 'Ilocos : '
print c.most_common()