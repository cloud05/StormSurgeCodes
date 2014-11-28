# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 16:32:14 2014
MAKE HVT FROM GET* 
@author: phillip
"""

import glob
import os
import numpy as np


def hvt(csvPath, outPathDir):
    outPath = os.path.join(csvPath, outPathDir)
    try:
        os.mkdir(outPath)
    except OSError:
        pass
    print outPath
    csvList = glob.glob(os.path.join(csvPath, '*.xls'))
    for csv in csvList:
        hvtfname = os.path.basename(csv).replace('.xls', '.hvt')
        hvt = os.path.join(outPath, hvtfname)
        with open(csv, 'r') as infile:
            data = infile.readlines()
    #    data = data[0].strip().split('\r')
        data = [l.strip('\n').split('\t') for l in data]
        values = np.array([d[4] for d in data]).astype(np.float)
        index = np.arange(0, len(values)) - np.where(values==max(values))[0][0]
    #    print index
        d = dict(zip(index, values))
        with open(hvt, 'w') as outfile:
            for i in range(-36, 1):
                if (i + 36) / 6.0 > 72.0:
                    break
                else:
                    outfile.write(str((i + 36) / 6.0) + '\t' + str(d[i]) + '\r\n')
