# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:21:35 2014

@author: cloud
"""
"""
This code is used to compare tide measurements from NAMRIA and harmonic tidal prediction.
"""

import datetime
import fnmatch
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
from scipy import interpolate
import math
import re
import string
import sys
### Big-assed dictionary
dic = {'REAL': ['14-40-16.59N', '121-36-48.71E'], 'SAN CARLOS': ['10-28-40.35N', '123-25-22.79E'], 'JOSE_P': ['14-18-52.07N', '122-40-27.67E'], 'CATBALOGAN': ['11-47N', '124-53E'], 
       'MARIVELES': ['14-26-12.15N', '120-30-28.39E'], 'SUBIC': ['14-45-56.06N', '120-15-03.23E'], 'ODIONGAN': ['12-24-8.21N', '121-28-50.29E'], 'PULUPANDAN': ['10-31N', '122-48E'], 'BULAN': ['12-39-52.84N', '123-52-16.29E'], 
       'P.PRINCESA': ['09-44-37.35N', '118-43-41.14E'], 'TAGBILARAN': ['09-39N', '123-51E'], 'BALANACAN': ['13-32-0.93N', '121-51-54.67E'], 'PAGADIAN': ['07-49-05.19N', '123-26-20.84E'], 
       'SN JSE N.SAMAR': ['12-31-58.42N', '124-29-12.15E'], 'CEBU': ['10-17-34.81N', '123-54-29.19E'], 'BALINTANG': ['09-20-51.95N', '118-07-30.22E'], 'CAGDEORO': ['08-30-03.65N', '124-39-51.14E'], 
       'BONGAO': ['05-02-04.41N', '119-46-29.08E'], 'CAMIGUIN': ['09-14-37.25N', '124-44-14.97E'], 'LUBANG': ['13-49N', '120-12E'], 'ELNIDO': ['11-10-52.17N', '119-23-12.07E'], 'BALER': ['15-46N', '121-36E'], 
       'BATANES': ['20-27N', '121-58E'], 'VIRAC': ['13-34-54.45N', '124-14-03.60E'], 'CATICLAN': ['11-56N', '121-57E'], 'GUIUAN': ['11-02N', '125-43E'], 'LEGASPI': ['13-08-46.21N', '123-45-29.25E'], 
       'MANILA': ['14-35-07.40N', '120-58-02.97E'], 'CURRIMAO': ['17-59-16.41N', '120-29-15.67E'], 'BATANGAS': ['13-45-26.27N', '121-02-25.51E'], 'SAN VICENTE': ['18-30-32.5N', '122-09-0.7E'], 
       'CALAPAN': ['13-25-39.56N', '121-11-40.78E'], 'SAN FERNANDO': ['16-36-21.00N', '120-17-29.69E'], 'SN JSE ANTIQUE': ['10-44-17.58N', '121-56-18.29E'], 'SN JSE MINDORO': ['12-20N', '121-05E'], 
       'GENSAN': ['06-05-29.92N', '125-09-15.06E'], 'CORON': ['11-59-26.65N', '120-12-40.49E'], 'SURIGAO': ['09-47-26.04N', '125-29-49.35E'], 'DUMAGUETE': ['09-18N', '123-19E'], 'ZAMBOANGA': ['06-54-54.77N', '122-02-16.89E'], 
       'TACLOBAN': ['11-15-08.43N', '125-00-09.46E'], 'MASBATE': ['12-22-11.85N', '123-36-55.67E'], 'MAMBURAO': ['13-13-38.55N', '120-34-03.17E'], 'TANDAG': ['09-05-4.95N', '126-11-49.43E'], 'DAVAO': ['07-07-17.83N', '125-39-45.84E'], 
       'BROOKES PT': ['08-46-17.37N', '117-49-42.31E'], 'MATI': ['06-57N', '126-13E']}

def strToDate(s, fmt='%d%m%Y'):
    return datetime.datetime.strptime(s, fmt)
    
    
def dateToStr(s, fmt='%m/%d/%Y %H:%M'):
    return datetime.datetime.strftime(s, fmt)

### Observed Vlues ###
def readTideTxt(tidePath):
    """
    Read Tide data in text files in the format [mm/dd/yyyy HH:MM	value(m)]
    and stores data into a dict.
    Time is not converted.
    Tide station name is the filename of the text file.
    tideStationDict={tide_station1:{time1:value1,
                                    time2:value2,
                                    time3:value3
                                    ...},
                     tide_station2:{time1:value1,
                                    time2:value2,
                                    time3:value3
                                    ...},
                     ...}
    """
    print 'Reading tide data...\n'
    xtideFileList = glob.glob(os.path.join(tidePath, '*.txt'))
    tideStationDict = {}
    for filename in sorted(xtideFileList):
        print 'Processing', os.path.basename(filename)
        with open(filename, 'r') as tideFile:
            tideData = tideFile.readlines()
        cleanedTideData = [line.strip('\n').split('\t') for line in tideData]
        tideStation = os.path.splitext(os.path.basename(filename))[0]
        tideValueDict = {}
        for i in range(len(cleanedTideData)):
            dataTime = datetime.datetime.strptime(cleanedTideData[i][0], 
                                                  '%m/%d/%Y %H:%M')
            try:
                tideValueDict[dataTime] = float(cleanedTideData[i][1])
            except ValueError:
                tideValueDict[dataTime] = np.nan
        tideValues = [tideValueDict[t] for t in tideValueDict.keys()]# if t.month in drymonths]
        tideValues = [value for value in tideValues if not np.isnan(value)]
        meanTide = np.mean(tideValues)
        for t in tideValueDict.keys():
            tideValueDict[t] = tideValueDict[t] - meanTide
        tideStationDict[tideStation] = tideValueDict
    print '\nDone reading tide data...\n'
    return tideStationDict
    
### Forecasted Values ###
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
    return tideLevels 
    
def parse_lonlat(y,x):
    for c in y:
        if c in string.ascii_letters:
            y = y.replace(c,'')
            if len(y)<7:
                y = y+'-00'
#                print y
    for d in x:
        if d in string.ascii_letters:
            x = x.replace(d,'')
            if len(x)<7:
                x = x+'-00'
#                print x

    coord = "( {}\"E, {}\"N)".format(y,x)
    latlon_regex = r"\(\s*(\d+)-(\d+)-([\d.]+)\"([WE]),\s*(\d+)-(\d+)-([\d.]+)\"([NS])\s*\)"
    m = re.match(latlon_regex, coord)
    parts = m.groups()
    lat = int(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600
    if parts[3] == 'W':
        lat *= -1
    lon = int(parts[4]) + float(parts[5]) / 60 + float(parts[6]) / 3600
    if parts[7] == 'S':
        lon *= -1
    return (lon, lat)   
    
    
if __name__ == '__main__':
    while True:
        try:
            mainDir = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH'#raw_input("Enter the root directory: ")#raw_input("Enter the station folder you want to compare: ")
            folders = os.path.normpath(mainDir)
            for root, dirnames, filenames in os.walk(folders):
                for filename in fnmatch.filter(filenames, '*.txt'):
                    start_year = int(root[-9:-5])
                    end_year = int(root[-4:])
                    filename = filename[:-6] 
            #            print filename
                    print "Comparing tides from {} to {} in {}.".format(start_year, end_year, filename)
                    try:
                        lonz = dic[filename][1]#raw_input("Enter longtitude of station: ")
                        latz = dic[filename][0]#raw_input("Enter latitude of station: ")       
            #                print lonz,latz
                    except KeyError:
                        print "No key"
                        continue
                    lonlat = parse_lonlat(lonz,latz)
                    lon = round(lonlat[1],2)#input("Enter longtitude of station: ")
                    lat = round(lonlat[0],2)#input("Enter latitude of station: ")
                    print lon,lat
                    while start_year < (end_year +1):
                        for i in range(1,13):
                            print 'path: ' + root   
                            path = root
                            months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',
                                      8:'August',9:'September',10:'October',11:'November',12:'December'}
                                      
                            # Forecasted
                            x = i #input("Input the month in digit: ")
                            z = months[x]
                            yr = str(start_year)
                            y = yr[-2:]#raw_input("Enter last two year digits: ")
                            startDate = datetime.datetime(start_year,x,1,0,0)
                            print startDate
                            if not os.path.exists(path +'\{0}{1}.png'.format(z,yr)):
                                tides = tideForecast(lon,lat,startDate,60,720,8)
                                timez = [m for m in tides.keys()]
                                timez.sort()  
                                valuez = [tides[m] for m in timez]                        
                                print "Forecast done."                        
                                
                            # Observed                            
                                outPath = path + '\{0}{1}.txt'.format(filename,y)
                                print outPath
                                tidePath = os.path.dirname(outPath)
                                var = readTideTxt(tidePath)
                                try:                                
                                    station = var['{0}{1}'.format(filename,y)]
                                except KeyError:
                                    print "No key"
                                    continue
                                times = [t for t in station.keys() if t.month == x]
                                times.sort()
            #                                print times
                                values = [station[t] for t in times]
                                plt.figure(figsize = (18,7))
                                plt.plot(timez,valuez,'-',label = 'Forecast {0} {1} {2}'.format(filename,z,yr))                        
                                plt.plot(times, values, '-', label='Observed {0} {1} {2}'.format(filename,z,yr))
                                plt.title('Comparison of Forecasted and Observed Data')
                                plt.xlabel('Date')
                                plt.ylabel('Tide Level in meters')
                                plt.legend()
                                try:
                                    plt.savefig(path +'\{0}{1}.png'.format(z,yr))
                                except ValueError:
                                    print "Value Error"
                                    sys.exc_clear()
                                plt.close()
                            else:
                                print "File exists."
                        start_year += 1
                        print start_year
        except Exception:
            sys.exc_clear()
        else:
            break
            
            
    
    
    
    
    
    