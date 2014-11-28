# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 12:46:54 2014

@author: Windows User
"""
import string,re,os,fnmatch
dic = {'REAL': ['14-40-16.59N', '121-36-48.71E'], 'SAN CARLOS': ['10-28-40.35N', '123-25-22.79E'], 'JOSE_P': ['14-18-52.07N', '122-40-27.67E'], 'CATBALOGAN': ['11-47N', '124-53E'], 
       'MARIVELES': ['14-26-12.15N', '120-30-28.39E'], 'SUBIC': ['14-45-56.06N', '120-15-03.23E'], 'ODIONGAN': ['12-24-8.21N', '121-28-50.29E'], 'PULUPANDAN': ['10-31N', '122-48E'], 'BULAN': ['12-39-52.84N', '123-52-16.29E'], 
       'PORT IRENE': ['09-44-37.35N', '118-43-41.14E'], 'TAGBILARAN': ['09-39N', '123-51E'], 'BALANACAN': ['13-32-0.93N', '121-51-54.67E'], 'PAGADIAN': ['07-49-05.19N', '123-26-20.84E'], 
       'SN JSE N.SAMAR': ['12-31-58.42N', '124-29-12.15E'], 'CEBU': ['10-17-34.81N', '123-54-29.19E'], 'BALINTANG': ['09-20-51.95N', '118-07-30.22E'], 'CAGDEORO': ['08-30-03.65N', '124-39-51.14E'], 
       'BONGAO': ['05-02-04.41N', '119-46-29.08E'], 'CAMIGUIN': ['09-14-37.25N', '124-44-14.97E'], 'LUBANG': ['13-49N', '120-12E'], 'ELNIDO': ['11-10-52.17N', '119-23-12.07E'], 'BALER': ['15-46N', '121-36E'], 
       'BATANES': ['20-27N', '121-58E'], 'VIRAC': ['13-34-54.45N', '124-14-03.60E'], 'CATICLAN': ['11-56N', '121-57E'], 'GUIUAN': ['11-02N', '125-43E'], 'LEGASPI': ['13-08-46.21N', '123-45-29.25E'], 
       'MANILA ': ['14-35-07.40N', '120-58-02.97E'], 'CURRIMAO': ['17-59-16.41N', '120-29-15.67E'], 'BATANGAS': ['13-45-26.27N', '121-02-25.51E'], 'SAN VICENTE': ['18-30-32.5N', '122-09-0.7E'], 
       'CALAPAN': ['13-25-39.56N', '121-11-40.78E'], 'SAN FERNANDO': ['16-36-21.00N', '120-17-29.69E'], 'SN JSE ANTIQUE': ['10-44-17.58N', '121-56-18.29E'], 'SN JSE MINDORO': ['12-20N', '121-05E'], 
       'GENSAN': ['06-05-29.92N', '125-09-15.06E'], 'CORON': ['11-59-26.65N', '120-12-40.49E'], 'SURIGAO': ['09-47-26.04N', '125-29-49.35E'], 'DUMAGUETE': ['09-18N', '123-19E'], 'ZAMBOANGA': ['06-54-54.77N', '122-02-16.89E'], 
       'TACLOBAN': ['11-15-08.43N', '125-00-09.46E'], 'MASBATE': ['12-22-11.85N', '123-36-55.67E'], 'MAMBURAO': ['13-13-38.55N', '120-34-03.17E'], 'TANDAG': ['09-05-4.95N', '126-11-49.43E'], 'DAVAO': ['07-07-17.83N', '125-39-45.84E'], 
       'BROOKES PT': ['08-46-17.37N', '117-49-42.31E'], 'MATI': ['06-57N', '126-13E']}


def parse_lonlat(y,x):
    for c in y:
        if c in string.ascii_letters:
            y = y.replace(c,'')
            if len(y)<7:
                y = y+'-00'
                print y
    for d in x:
        if d in string.ascii_letters:
            x = x.replace(d,'')
            if len(x)<7:
                x = x+'-00'
                print x

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
    
    
#if __name__ == '__main__':
#    mainDir = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH'#raw_input("Enter the root directory: ")#raw_input("Enter the station folder you want to compare: ")
#    folders = os.path.normpath(mainDir)
#    for root, dirnames, filenames in os.walk(folders):
#        for filename in fnmatch.filter(filenames, '*.txt'):
#            start_year = int(root[-9:-5])
#            end_year = int(root[-4:])       
#            filename = filename[:-6] 
##            print filename
#            print "Comparing tides from {} to {} in {}.".format(start_year, end_year, filename)
#            try:
#                lonz = dic[filename][1]#raw_input("Enter longtitude of station: ")
#                latz = dic[filename][0]#raw_input("Enter latitude of station: ")       
##                print lonz,latz
#            except KeyError:
#                print "No key"
#                continue
#            lonlat = parse_lonlat(lonz,latz)
#            lon = round(lonlat[1],2)#input("Enter longtitude of station: ")
#            lat = round(lonlat[0],2)#input("Enter latitude of station: ")
#            print lon,lat
            
            
            
#def lat_lon(lat1,lon1):
#    for c in lat1:
#        if c in string.ascii_letters:
#            lat1 = lat1.replace(c,'')
#            print lat1
#    for d in lon1:
#        if d in string.ascii_letters:
#            lon1 = lon1.replace(d,'')
#            print lon1
#    coord = "( {}\"E, {}\"N)".format(lon1,lat1)
#    return coord
#
#def parse_lonlat(coord):
#    """ Pass in string in degrees like "( 24d37'55.25\"W, 73d42'10.75\"S)"
#    Returns decimal tuple (lon, lat)
#    """
#    latlon_regex = r"\(\s*(\d+)-(\d+)-([\d.]+)\"([WE]),\s*(\d+)-(\d+)-([\d.]+)\"([NS])\s*\)"
#    m = re.match(latlon_regex, coord)
#    parts = m.groups()
#    lat = int(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600
#    if parts[3] == 'W':
#        lat *= -1
#    lon = int(parts[4]) + float(parts[5]) / 60 + float(parts[6]) / 3600
#    if parts[7] == 'S':
#        lon *= -1
#    return (lon, lat)   
#
#
#if __name__ == '__main__':
#    o = dic['REAL'][0]
#    p = dic['REAL'][1]    
    
   
import csv
reader = csv.reader(open(r"C:\Users\Windows User\Desktop\Work\Fieldworks\SorsogonOutputs\HVT\sisang\maximum\maxStormTide.csv"))
dic = {}
for row in reader:       
    key = row[0]
#    if key in dic:
##        pass
    dic[key] = row[2]
#    a =  (row[2])
#    lis = a.split("\t")
print dic
#------------------
#def csv_reader(csvFile):
#    reader = csv.reader(csvFile)
#    for row in reader:
#        print (" ".join(row))
#
#if __name__ == "__main__":
#    csv_path = r"C:\Users\Windows User\Desktop\Work\tide\tides.csv"
#    with open(csv_path, "rb") as f:
#        csv_reader(f)
#import string
#a = '120-29-15.67E'
#for c in a:
#    if c in string.ascii_letters:
#        a = a.replace(c,'')
#        print a



#import numpy as np
#import matplotlib.pyplot as plt
#
#A = np.random.rand(34*52).reshape(34,52)
#means = np.average(A,axis=0)
#
#plt.figure()
#
#plt.subplot(2,1,1)
#plt.imshow(A, interpolation='nearest',aspect = 'auto' )
#
#plt.subplot(2,1,2)
#plt.plot(means)
#
#plt.show()

##!/usr/bin/env python
#import numpy as np
#import matplotlib.cm as cm
#import matplotlib.mlab as mlab
#import matplotlib.pyplot as plt
#from pylab import *
#
#delta = 0.025
#x = y = np.arange(-3.0, 3.0, delta)
#X, Y = np.meshgrid(x, y)
#Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
#Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
#Z = Z2-Z1  # difference of Gaussians
#ax = Axes(plt.gcf(),[0,0,1,1],yticks=[],xticks=[],frame_on=False)
#plt.gcf().delaxes(plt.gca())
#plt.gcf().add_axes(ax)
#im = plt.imshow(Z, cmap=cm.gray)
#
#plt.show()