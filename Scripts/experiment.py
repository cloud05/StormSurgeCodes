# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 14:46:00 2014

@author: GEOS_SS1
"""
import os, fnmatch, re,string

def changeHVTone():
    mainhvtPath = raw_input("Enter the hvt path: ")#r'C:\Users\GEOS_SS1\Desktop\prinsepe\OrMindoro\hvt\HVT_REMING_MINDORO\balatasanbulalacaomr.hvt'
    print os.listdir(mainhvtPath)    
    prompt_a = raw_input("Choose the station to use: ")
    hvtPath = os.path.join(mainhvtPath,prompt_a)
    for root, dirnames, filenames in os.walk(origPath):
        for files in fnmatch.filter(filenames,'*.hvt'):
            filePath = os.path.join(origPath,files)
            print filePath
            x = open(hvtPath,"r+")
            f = open(filePath,'r+')
            txtin = x.read()
            txtout = f.read()
            res = ''.join([i for i in txtout if i.isalpha()])
            txtout = re.sub('',txtin,res)
            f.seek(0)
            f.write(txtout)
            f.truncate()
            f.close()
            x.close()
    print "Done!"


def changeHVTmulti():
    count = 1
    hvts  = [] #hvt's to be used to change the output
    points = [] #F2D-GDS hvts
    stations = [] #range of points for a certain station
    mainhvtPath = raw_input("Enter the hvt path: ")#r'C:\Users\GEOS_SS1\Desktop\prinsepe\OrMindoro\hvt\HVT_CALOY_MINDORO'
    print os.listdir(mainhvtPath)
    for root, dirnames, filenames in os.walk(origPath):
        for files in fnmatch.filter(filenames,'*.hvt'):
            points.append(files)
    while len(hvts) < promt:
        print count
        promt_e = raw_input("Choose station to use: ")
        prompt_b = promt_e + '.hvt'
        prompt_c = raw_input("Enter the STARTING point of {}: ".format(prompt_b))
        prompt_d = raw_input("Enter the ENDPOINT of {}: ".format(prompt_b))
        zipper = tuple((prompt_c,prompt_d))
        stations.append(zipper)
        hvtPath = os.path.join(mainhvtPath,prompt_b)
        hvts.append(hvtPath)
        dic = dict(zip(hvts,stations))
        count  += 1
        
#    for j in dic.keys():
#        for i in range(int(dic[j][0]),int(dic[j][1])+1):
                
    for point in points:
        for j in dic.keys():
            print j
            for i in range(int(dic[j][0]),int(dic[j][1])+1):
#            for i in range(int(prompt_c),int(prompt_d)+1):
                if " {}.HVT".format(str(i)) in point:
                    print point                                                                                        
                    filePath = os.path.join(origPath,point)
                    print filePath
                    print hvtPath
                    x = open(hvtPath,"r+")
                    f = open(filePath,'r+')
                    txtin = x.read()
                    txtout = f.read()
                    res = ''.join([i for i in txtout if i.isalpha()])
                    txtout = re.sub('',txtin,res)
                    f.seek(0)
                    f.write(txtout)
                    f.truncate()
                    f.close()
                    x.close()
    print "Done!"
changeHVTmulti()
#if __name__ == '__main__':
#    count = 0
#    noSim = input("How many typhoons will you simulate?: ")
#    while count < noSim:
#        origPath = raw_input("Enter the original path of the model: ")#r'C:\Users\GEOS_SS1\Desktop\prinsepe\OrMindoro\Calapan_20m\Flo2d\Calapan_reming'
#        while True:
#            try:
#                promt = int(raw_input('Enter the EXACT number of stations: '))
#            except ValueError:
#                print "Number only!"
#                continue
#            else:
#                break
#        if promt == 1:
#            changeHVTone()
#        elif promt > 1:
#            changeHVTmulti()
#        count += 1
#        
    
    

    
# 
#for root, dirnames, filenames in os.walk(origPath):
#   for files in fnmatch.filter(filenames,'*.hvt'):
#        filePath = os.path.join(origPath,files)
#        with open(filePath,)
#        f = open(filePath, 'r+')
#        text = f.read()
#        res = ''.join([i for i in text if i.isalpha()])
#        print res.replace(" ","")
##        s = re.sub(r's+',"",res)
##        text = re.sub('\n', '', text)
##        print text#.replace(" ","")
##        text = re.sub()
#        f.close()
        
         

#listDir = os.listdir(outPathDir)
#for item in listDir:
#    pather = os.path.join(outPathDir,item)
#    f = open(pather, 'r+')
#    text = f.read()
#    text = re.sub('\n', '', text)
#    f.seek(0)
#    f.write(text)
#    f.truncate()
#    f.close()
