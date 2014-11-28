def readXTide(tidePath):
    """
    Get tide values from Wxtide.
    One value coressponds to an entry on the list.
    Times are converted to PST
    entry format : [value(m), HH:MM, time_format, MM/DD/YYYY]
    
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
        tideStation = alphanum(tideData[0])
        tideData = tideData[3:]
        cleanedTideData = []
        for i in range(len(tideData)):
            tideData[i] = tideData[i].replace('\r\n', '').split()
            if tideData[i]:
                cleanedTideData.append(tideData[i])
        for i in range(len(cleanedTideData)):
            if len(cleanedTideData[i]) < 4:
                cleanedTideData[i].append(cleanedTideData[i - 1][3])
        tideValueDict = {}
        for i in range(len(cleanedTideData)):
            if len(cleanedTideData[i][1]) < 5:
                cleanedTideData[i][1] = '0' + cleanedTideData[i][1]
            dataTime = datetime.datetime.strptime(cleanedTideData[i][3] +
                       cleanedTideData[i][1], '%Y-%m-%d%H:%M') + (
                       datetime.timedelta(hours=8))
            tideValueDict[dataTime] = float(cleanedTideData[i][0])
        tideValues = [tideValueDict[t] for t in tideValueDict.keys()]
        meanTide = np.mean(tideValues)
        for t in tideValueDict.keys():
            tideValueDict[t] = tideValueDict[t] - meanTide
        tideStationDict[tideStation] = tideValueDict
    print '\nDone reading tide data...\n'
    return tideStationDict