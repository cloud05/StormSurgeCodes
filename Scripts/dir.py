# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:04:04 2014

@author: Windows User
"""

# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
a = raw_input("Enter the root directory: ")
b = os.path.normpath(a)
dirs = []
filez = []
for dirName, subdirList, fileList in os.walk(b):
    dirs.append(dirName)
    print dirName
    y = os.path.normpath(dirName)
    x = []
    x.append(y)
    print x
#    print('Found directory: %s' % dirName)
    for fname in fileList:
        filez.append(fname)
#        print('\t%s' % fname)

##for fileList in os.walk(a):
##    files.append(fileList)
##filez = os.listdir(a)
#
##f = open('names.txt', 'w')
##filez = []
##for root, dirs, files in os.walk(a):
##    for newname in files:
##        filename = os.path.join(newname)
##        filez.append(filename)
##	
#		
#
##		newstring = filename + '\n'
##		f.write(newstring)

# traverse root directory, and list directories as dirs and files as files
#for root, dirs, files in os.walk(b):
#    path = root.split('/')
#    print (len(path) - 1) *'---' , os.path.basename(root)       
#    for file in files:
#        print len(path)*'---', file             