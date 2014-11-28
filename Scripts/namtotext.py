# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 09:36:57 2014

@author: Windows User
"""



import datetime
import fnmatch
import os
import numpy as np
import matplotlib.pyplot as plt
import glob


def strToDate(s, fmt='%d%m%Y'):
    return datetime.datetime.strptime(s, fmt)
    
    
def dateToStr(s, fmt='%m/%d/%Y %H:%M'):
    return datetime.datetime.strftime(s, fmt)

def namriaToTxt(sourcePath, outPath):
    sourceFile = open(sourcePath, 'r')
    source = sourceFile.readlines()
    source = [line.strip('\n') for line in source]
    with open(outPath, 'w') as out:
        for dataLine in source:
            dataValues = dataLine[:72]
            dataDate = dataLine[-6:].replace(' ','0')
            try:
                if int(dataDate[-2:]) > 13:
                    dataDate = dataDate[0:4] + '19' + dataDate[4:]
                else:
                    dataDate = dataDate[0:4] + '20' + dataDate[4:]
            except ValueError:
                print sourcePath
                pass
            
            dataValues = [dataValues[i:i + 3] for i in range(0, len(dataValues), 3)]
            dataValues = [float(value) / 100.0 for value in dataValues]
            hour = 0    
            for waterLevel in dataValues:
                dateNow = strToDate(dataDate) + datetime.timedelta(hours=hour)
                if waterLevel != 9.99:
                    out.write(dateToStr(dateNow) + '\t' + str(waterLevel) + '\n')
                else:
                    out.write(dateToStr(dateNow) + '\t' + 'No data' + '\n')
                hour += 1
       
def readTideTxt(tidePath, drymonths=[2, 3]):
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
        tideValues = [tideValueDict[t] for t in tideValueDict.keys() if t.month in drymonths]
        tideValues = [value for value in tideValues if not np.isnan(value)]
        meanTide = np.mean(tideValues)
        for t in tideValueDict.keys():
            tideValueDict[t] = tideValueDict[t] - meanTide
        tideStationDict[tideStation] = tideValueDict
    print '\nDone reading tide data...\n'
    return tideStationDict
       
if __name__ == '__main__':      
#    mainDir = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH_orig'
#    for root, dirnames, filenames in os.walk(mainDir):
#        for filename in fnmatch.filter(filenames, '*.*'):
#            if len(filename) <= 9:
#                y = os.path.join(root, filename)
#                sourcePath = y
#                if os.path.isfile(y[:-4] + '_parsed.txt'):
#                    print "file exist"
#                else:
#                    outPath = y[:-4] + '_parsed.txt'
#                    namriaToTxt(sourcePath, outPath)

    
    
    
    
    
#    sourcePath = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH_orig\ZAMBOANGA 2003-2012\ZAMBOANGA12.TXT'
    outPath = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH_orig\ZAMBOANGA 2003-2012\ZAMBOANGA11.TXT'
#    namriaToTxt(sourcePath, outPath)
    tidePath = os.path.dirname(outPath)
    var = readTideTxt(tidePath)
    guiuan = var['ZAMBOANGA11']
    times = [t for t in guiuan.keys()]# if t.month == 1]
    times.sort()
    values = [guiuan[t] for t in times]
    plt.plot_date(times, values, '-', label='ZAMBOANGA11')
    plt.legend()
    plt.show()
