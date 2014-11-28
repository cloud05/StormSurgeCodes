# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 11:03:30 2014

@author: Windows User
"""
import os
os.chdir('C:\Users\Windows User\Desktop')
with open('euler.txt','r') as f:
    read = f.read()
    x = read.replace('\n' , '')
#print x

if __name__ == '__main__':
    max_prod = -1
    for i in range(len(x)-12):
        product = int(x[i]) * int(x[i+1]) * int(x[i+2]) * int(x[i+3]) * int(x[i+4]) * int(x[i+5]) * int(x[i+6]) * int(x[i+7]) * int(x[i+8]) * \
         int(x[i+9]) * int(x[i+10]) * int(x[i+11]) * int(x[i+12])
        if product > max_prod:
            max_prod = product
    print max_prod
        
