# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:30:45 2014

@author: cloud
"""

def automate():
    """
        Automates the process of changing the HVT files used in flo2D modeling. Based from the original
        changeHvt code.
    """   
    ### Variables used to run the program ###
    import os
    a = raw_input("Enter the original Outflow path: ")
    b = raw_input("Enter the new path for the Outflow file: ")
    c = raw_input("Enter HVT path: ")
    d = os.path.normpath(a)
    e = os.path.normpath(b)
    f = os.path.normpath(c)
    outflowPath = os.path.join(d, 'OUTFLOW.DAT')
    newoutflowPath = os.path.join(e, 'OUTFLOW.DAT')
    time = raw_input("Input the time of the HVT file you want to use(i.e. 6 or 12): ")
    height = input("Input the minimum height of the HVT file you want to use(i.e. 2,3,4 or 5 only!: ")
    x = len(e)
    change = e[x-2]    
    
    ### Main body of the code ###
    while height < 6:
        change_newoutflowPath = newoutflowPath.replace(change, str(height))
        print change_newoutflowPath
        hvtPath = os.path.join(f,'{0}hrs_{1}m_Timeseries.hvt'.format(time,height))
        with open(outflowPath, 'r') as of:
            ofdata = of.readlines()
            
        with open(hvtPath, 'r') as hvt:
            hvtdata = hvt.readlines()
            
        hvtdata = [l.strip('\r\n').split('\t') for l in hvtdata[1:]]
        hvtdata = ['S' + 14 * ' ' + '{:.9}'.format(l[0]) + (14 - len('{:.9}'.format(l[0]))) * ' ' + '{:E}'.format(float(l[1])) + '\n' for l in hvtdata]

        index = [i for i, l in enumerate(ofdata) if l.startswith('S')
        ]

        cindex = []
        for i in range(len(index)):
            try:    
                if index[i] - index[i - 1] == 1 and index[i + 1] - index[i] == 1:
                    pass
                else:
                    cindex.append(index[i])
            except IndexError:
                pass
        cindex.append(index[-1])
        cindex = [cindex[i:i + 2] for i in range(0, len(cindex), 2)]
        cindex = [(l[0], l[1] + 1) for l in cindex]

        first = True
        for idx, r in enumerate(cindex):
            if first:
                first = False
            else:
                if r[1] - r[0] != len(hvtdata):
                    subtract = r[1] - r[0] - len(hvtdata)
                    for i in range(len(cindex)):
                        cindex[i] = (cindex[i][0] - subtract, cindex[i][1] - subtract)
            ofdata[cindex[idx][0]:cindex[idx][1]] = hvtdata
                    
        with open(change_newoutflowPath, 'w') as out:
            for l in ofdata:
                out.write(l)
        height += 1
    print "Done!"   
    raw_input("Press ENTER to exit")
automate()

