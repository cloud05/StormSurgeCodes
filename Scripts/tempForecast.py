# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 09:15:35 2014

@author: cloud
"""

import os
#import glob
import numpy as np
import datetime
import math
import matplotlib.pyplot as plt
from scipy import interpolate

def inside(x, y, lowerLeft, upperRight):
    if lowerLeft[0] <= x <= upperRight[0] and lowerLeft[1] <= y <= upperRight[1]:
        return True
    else:
        return False
        
def readConstituents(path=r'C:\Users\Windows User\Desktop\Work\tide\tidal_constituents_0.125deg\constituents_phl.txt'):
    home = os.path.expanduser('~')
    constPath = os.path.join(home, path)
    with open(constPath, 'r') as c:
        const = eval(c.readline())
    return const
    
def tideForecast(lon, lat, startDate, interval, steps, timeoffset):
    """
    lon and lat in degrees, interval in minutes, startDate:
    """
    frequencyTable = {'K1': 15.0410686,
                      'K2': 30.0821373,
                      'M2': 28.9841042,
                      'M4': 57.9682084,
                      'N2': 28.4397295,
                      'O1': 13.9430356,
                      'P1': 14.9589314,
                      'Q1': 13.3986609,
                      'S1': 15.0,
                      'S2': 30.0
                      }
    constituentsTable = readConstituents()
    epoch = datetime.datetime(year=1900, month=1, day=1)
#    startDate += datetime.timedelta(hours=timeoffset)
    t0 = (startDate - epoch).days * 24 - timeoffset
    constituents = ['K1', 'K2', 'M2', 'M4', 'N2', 'O1', 'P1', 'Q1', 'S1', 'S2']
    dates = [startDate + i * datetime.timedelta(minutes=interval) for i in xrange(steps)]
    tideLevels = {}
    for d in dates:
        tideLevels[d] = 0
    
    for constName in constituents:
        amp = constName + 'amp'
        pha = constName + 'pha'
        
        # Compute amplitude
        cgrid = constituentsTable[amp]
        X, Y = zip(*(cgrid.keys()))
        values = [cgrid[(i, j)] for i, j in zip(X, Y)]
        points = np.array([X, Y]).transpose()
        A = interpolate.griddata(points, values, (lon, lat), method='cubic')   
        
        # Compute phase
        cgrid = constituentsTable[pha]
        X, Y = zip(*(cgrid.keys()))
        values = [cgrid[(i, j)] for i, j in zip(X, Y)]
        points = np.array([X, Y]).transpose()
        C = interpolate.griddata(points, values, (lon, lat), method='cubic')

        # Get Frequency
        B = frequencyTable[constName]           
    
        for d in dates:
#            print d, epoch + datetime.timedelta(hours=t0)
            tideLevels[d] += A * math.cos(math.radians(B * t0 - C))
            t0 += interval / 60.0
            
        #Set back to initial time for next constituent iteration    
        t0 = (startDate - epoch).days * 24 - timeoffset   
        tides = tideLevels
        timez = [t for t in tides.keys()]
        timez.sort()
        valuez = [tides[t] for t in timez]
        plt.plot(timez,valuez,'-', label = 'Forecast BALANACAN 2008')
        plt.legend()
        plt.show()        
        return tideLevels , valuez, timez

    
startDate = datetime.datetime(2008,10,1,0,0)
tideForecast(121.86,13.53,startDate,60,720,8)   
    
#if __name__ == '__main__':
#    startDate = datetime.datetime(2008,10,1,0,0)
#    x = tideForecast(121.86,13.53,startDate,60,720,8)    
#    timez = [t for t in x.keys()]
#    timez.sort()
#    valuez = [x[t] for t in timez]
#    plt.plot(timez,valuez,'-', label = 'Forecast BALANACAN 2008')
#    plt.legend()
#    plt.show()

    
