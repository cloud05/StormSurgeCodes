# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 14:36:00 2014

@author: GEOS_SS1
"""

import os
import shutil

p = r'C:\Users\GEOS_SS1\Desktop\prinsepe\OrMindoro\Naujan_20m\Flo2d\Naujan_2m'

def listdir_fullpath(p):
    return [os.path.join(p, d) for d in os.listdir(p)]
#def getDirs(path):
#    l =  [d for d in listdir_fullpath(path) if os.path.isdir(d)]
#    return l

src = r'C:\Users\GEOS_SS1\Desktop\prinsepe\OrMindoro\Naujan_20m\Flo2d\Naujan_2m'
dest = os.makedirs
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)