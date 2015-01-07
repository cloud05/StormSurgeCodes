# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 23:57:31 2014

@author: cloud
"""
import csv
height = 1.5

input_file = r'C:\Users\Windows User\Desktop\Work\Typhoons\Actual_strength_summary_5.csv'
final = []
y = []
reader = csv.DictReader(open(input_file))
for row in reader:
    if 'SN' in row['Station'][-2:]:
        x = ['%s:%s' % (f, row[f]) for f in reader.fieldnames]
        y.append(x)
#for lis in y:
#    for item in lis[1:len(lis)]:
#        try:
#            if float(item.split(':')[1]) > height:
#                print item
#        except:
#            pass
#for i in range(len(y)): 
for i in range(len(y)):
    for item in y[i][1:len(y[i])]:
        try:
            if float(item.split(':')[1]) > height:
                print y[i][0] + ':' + item
        except ValueError:
            continue
#    final.append(z)
#        for val in x:
#            if 
#        keys = x[0]
#        dic[keys] = x[1:len(x)]
        