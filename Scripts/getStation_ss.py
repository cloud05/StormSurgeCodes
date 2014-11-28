# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 11:47:15 2014

@author: Windows User
"""

f1 = r'C:\Users\Windows User\Desktop\Work\ss\JMA_storm_surge\data\complete_stations\station.txt'
f2 = r'C:\Users\Windows User\Desktop\Work\ss\JMA_storm_surge\data\complete_stations\station_MR.txt'
with open(f1) as f:
    with open(f2,'w') as ff:
        for line in f:
            if 'MR' in line:
                ff.write(line)
print "Done"
