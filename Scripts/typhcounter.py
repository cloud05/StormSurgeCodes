# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 12:52:54 2014

@author: Windows User
"""

import csv
from collections import Counter
from collections import defaultdict

csvfile = r'C:\Users\Windows User\Desktop\LaUnionIlocosField Work\Ilocos.csv'
bagyo = []
points = {}
station = []
data = defaultdict(list)
data2 = defaultdict(list)
#with open(csvfile,'rb') as dataf:
#    reader = csv.DictReader(dataf)
#    next(reader)
#    for row in reader:
#        a =  row['Estimated Dates and Times of Peaks']
#        station.append(a)
#        station.sort()
#        data[row['Station Name']].append(row['Surge + Tide (m)'])
#        data[row['Station Name']].append(row['Surge + Tide (m)'])
#        bagyo.append(row['Flood Event'])
#        new = [x for x in bagyo if x != '']
#        data[row['Municipality']].append(row['Flood Event'])
#        data2[row['Municipality']].append(row['Barangay'])
#    for name in data2.keys():
#        print name+': '
#        print  str(set(data2[name]))
#    for x in data.keys():
#        y = [z for z in data[x] if z !='' and z != '-']
#        print x +': '+ str(len(y))
        
read = csv.reader(open(csvfile))
next(read)
for row in read:
#    key = row[1][3:]
#    points[key] = row[0]
    
#    a = row[0].split()
#    if len(a) > 3:
#        del a[:2]
#    else:
#        del a[0]
#        print a
        
    key = row[3]
    points[key] = row[6]
    bagyo.append(row[6])
new = [x for x in bagyo if x != '']
c = Counter(new)
print 'in : '
print c.most_common()

