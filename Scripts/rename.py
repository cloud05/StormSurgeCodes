# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:45:45 2014

@author: Windows User
"""
#f = open('folderlist.txt','w')
import os, fnmatch,glob,re
import shutil
#from string import digits
DIC = {'DBL':'BALANACAN','ABR':'BALER','DBR':'BALER','ABQ':'BALINTANG','DBS':'BATANES','BT':'BATANGAS', 
        'ABP':'BROOKES PT','DBP':'BROOKES PT','ABN':'BULAN','DCD':'CDO','DCP':'CALAPAN','ACG':'CAMIGUIN',
        'CG':'CAMIGUIN','ACT':'CATBALOGAN','DCN':'CATICLAN','ACB':'CEBU','DCB':'CEBU','XCB':'CEBU','CO':'CORON','DCO':'CORON',
        'DCD':'CURRIMAO','XDV':'DAVAO','DV':'DAVAO','DG':'DUMAGUETE','DEN':'ELNIDO','DGS':'GENSAN','DGU':'GUIAN',
        'AJP':'JOSE_P','LG':'LEGASPI','XLG':'LEGASPI','DLB':'LUBANG','AMM':'MAMBURAO','ML':'MANILA','XML':'MANILA',
        'MV':'MARIVELES','XMV':'MARIVELES','AME':'MASBATE','DME':'MASBATE','AMT':'MATI','APG':'PAGADIAN','IR':'PORT IRENE','LIR':'PORT IRENE',
        'PW':'P.PRINCESA','LPW':'P.PRINCESA','APD':'PALUPANDAN','DRL':'REAL','XRL':'REAL','ASC':'SAN CARLOS','DSF':'SAN FERNANDO','XSF':'SAN FERNANDO',
        'SJ':'SN JSE MINDORO','SA':'SN JSE ANTIQUE','ASN':'SN JSE N.SAMAR','SN':'SN JSE N.SAMAR','SV':'SN VICENTE','DSV':'SN VICENTE','SB':'SUBIC',
        'SR':'SURIGAO','LSR':'SURIGAO','TB':'TACLOBAN','ATN':'TAGBILARAN','TG':'TANDAG','DTG':'TANDAG','DTW':'TAWITAWI','DVC':'VIRAC',
        'ZB':'ZAMBOANGA','DZB':'ZAMBOANGA'}
        
        
        
        
randshit = ['Butag Bay', 'Gubat', 'Port Boca Engano, Burias Isl', 'San Bernardino Island', 'Santa Cruz Harbor', 'Tabaco, Tabaco Bay', 'Torrijos', 'Virac, Catanduances Isl']      
key = [y for y in DIC.keys()]
val = [DIC[y] for y in key]
count = 0
while count < 7:
    path = raw_input('Enter: ')#r'C:\Users\Windows User\Desktop\Work\Fieldworks\CagayanOutputs\Tides\Karen2008'
#edit HVT files
#for root, dirnames, filenames in os.walk(path):
#    for filename in fnmatch.filter(filenames, '*.hvt'):
#        print filename
#listDir = os.listdir(path)
#for item in listDir:
#    pather = os.path.join(path,item)
#    f = open(pather, 'r+')
#    text = f.read()
#    text = re.sub('\n', '', text)
#    f.seek(0)
#    f.write(text)
#    f.truncate()
#    f.close()
####
#new = []
#with open(path,"r+") as f:
#    old = f.readlines()
#    f.seek(0)
#    for line in old:
#        if not line.strip():
#            continue
#        else:
#            new.append(line)
#    f.write("".join(new))
#print "".join(new)
#f.close()
# Get file contents
#fd = open(path)
#contents = fd.readlines()
#fd.close()
#
#new_contents = []
#
## Get rid of empty lines
#for line in contents:
#    # Strip whitespace, should leave nothing if empty line was just "\n"
#    if not line.strip():
#        continue
#    # We got something, save it
#    else:
#        new_contents.append(line)
#
## Print file sans empty lines
#print "".join(new_contents)
#!/usr/bin/python

#import fileinput
#for lines in fileinput.FileInput(path, inplace=1): 	
# 	lines = lines.strip()
# 	if lines == '': continue
# 	print lines
#dest = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH\BALANACAN 2008-2012\2009'
#for root, dirnames, filenames in os.walk(x):
#    for item in dirnames:
#        print item
#        start_year = item[-9:-5]
#        end_year = item[-4:]
#        print start_year
#        print end_year
#    for item in filenames:
#        if '2009' in item:
#            fil = os.path.join(root,item)
#            shutil.move(fil,dest)
            
#    for item in filenames:
#        filez.append(item)
#print len(filez)
        
#        a = item.translate(None, digits)
#        b = a[:-2]
#        f.write('%s\n'%b)
#    f.close()
    
    

    for root, dirnames, filenames in os.walk(path):
#    for filename in fnmatch.filter(filenames, '*.txt'):
        
#        if filename[:-4] not in randshit:
#            print filename[:-4]
            

##        print filename[-6:] 
#            w = os.path.join(root, filename)
#            os.remove(w)
        
#        print filename[:-6]
#        print filename[-6:]
#        z = os.rename(w,w+'.txt')
#           
#        print filename
#        print filename[:-6]
        for filename in filenames:
            if not filename in fnmatch.filter(filenames, '*.txt'):
                print filename
                w = os.path.join(root, filename)
                os.rename(w,w+'.txt')
    count +=1
    print count
##            os.remove(w)
#        if 'X' in filename:
#            aa = filename.strip('X')
#            print aa
#            w = os.path.join(root, filename)
#            ww = os.path.join(root, aa)
#            zz = os.rename(w,ww)
#        for y in key:
##        print y
#            try:
#                w = os.path.join(root, filename)
#                z = os.rename(w,w.replace(y,DIC[y]))
##                z = os.rename(w,w.replace('IR','PORT'))
#            except:
#                continue
            
#            os.remove(w)
#    elif len(filename) < 6:
#        print "none"
        
#      y = os.path.join(root, filename)
#        z = os.rename(y,os.path.join(root, filename.upper()))
#      print z , y
      
#      if  not os.path.isfile(z[:-4] + '.txt'):
#          os.rename(z, z[:-4] + '.txt')
          #print 'file exist'
#      else:
#          os.rename(y, y[:-4] + '.txt')
          
#def rename2text(mainDir): 
#    for root, dirs, files in os.walk(mainDir):  
#        for filename in files:
#            print 'a'+filename
#            for filename in glob.iglob(os.path.join(mainDir, '*.*')):
#                print filename
#                os.rename(filename, filename[:-4] + '.txt')
#        
#rename2text(x)


#cur_dir = r'C:\Users\Windows User\Desktop\Work\tide\TIDAL DATA\NOAH'
#extensions = ('.DEC', '.LEV', '.JUL', '.AUG')
#new_ext = '.txt'
#def change_multi_file_ext(cur_dir, extensions, new_ext):
#    for root, dirs, files in os.walk(cur_dir):
#        for filename in files:
#            file_ext = os.path.splitext(filename)[1]
#            for ext in extensions:
#                if ext == file_ext:
#                    oldname = os.path.join(root, filename)
#                    newname = oldname.replace(ext, new_ext)
#                    os.rename(oldname, newname)
#                    
#change_multi_file_ext(cur_dir, extensions, new_ext)


      
      