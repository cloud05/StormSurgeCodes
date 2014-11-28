# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 14:06:15 2014

@author: Windows User
"""
import os
typhs = []
counter = 0
noSim = 3
while counter < noSim:
    while True:
#        try:
        typh  = raw_input("Enter the path of the base model/s: ")
        if not os.path.isdir(typh):
            print "Enter a valid path."
            True
        else:                
            typhs.append(typh)
            print typhs
            counter += 1
            break
                
#        
#        corHVT = raw_input("Enter the hvt path corresponding to the model/s: ")
#        corsHVT.append(corHVT)
#        counter += 1