# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 03:43:52 2014

@author: GEOS_SS1
"""

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True
    
#print long_substr(['Oh, hello, my friend.',
#                   'I prefer Jelly Belly beans.',
#                   'When hell freezes over!'])
print