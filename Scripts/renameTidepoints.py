# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 16:14:36 2014

@author: cloud
"""
"""
A code to rename tide files into text files
"""
import os, fnmatch

tidepath = raw_input("Enter tide path: ")
for root, dirnames, filenames in os.walk(tidepath):
    for filename in filenames:
        if filename not in fnmatch.filter(filenames, '*.txt'):
            print filename
            w = os.path.join(root,filename)
            os.rename(w,w+'.txt')
        else:
            print filename + " already exists."