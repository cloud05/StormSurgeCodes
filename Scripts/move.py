# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 15:44:54 2014

@author: user
"""

import os,shutil,fnmatch
source = r'I:\Daram flo2d\Zuma_C'
dest = r"I:\Daram flo2d\Zuma_C_2"
try:
    os.mkdir(dest)
except:
    pass
for root, dirs, files in os.walk(source):
    for item in files:
        if item in fnmatch.filter(files,'*.*'):
            print item
            a = os.path.join(root,item)
            try:
                shutil.move(a,dest)
            except:
                continue