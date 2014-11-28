# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 10:14:16 2014

@author: Windows User
"""

# -*- coding: latin-1 -*-
import re
lon = raw_input("Enter lon: ")
lat = raw_input("Enter lat: ")


def parse_lonlat(coord):
    """ Pass in string in degrees like "( 24d37'55.25\"W, 73d42'10.75\"S)"
    Returns decimal tuple (lon, lat)
    """
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
 
val = parse_lonlat("( {}\"E, {}\"N)".format(lon,lat))
print val
#print parse_lonlat("( 121d02'25.51\"E, 13d45'26.27\"N)")
#121-02-25.51