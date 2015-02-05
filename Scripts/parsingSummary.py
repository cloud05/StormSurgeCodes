# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04 15:59:58 2015

@author: Windows User
"""
import csv,os,fnmatch
from collections import defaultdict

root = r'C:\Users\Windows User\Desktop\Work\Typhoons\Summaries'
outfile = root+r'\summary.csv'
files = os.listdir(root)
#csvf = r'C:\Users\Windows User\Desktop\Work\Typhoons\Station 1 Summary.csv'
data = defaultdict(list)
dic = {}
st = []
ht = []

provCode = {'DS':'Davao del Sur','DO': 'Davao Oriental','SN':'Surigao del Norte', 'BG': 'Benguet', 'BA': 'Bataan', 'DI': 'Dinagat Islands', 'TR': 'Tarlac', 'BN': 'Batanes', 'BO': 'Bohol', 'BI': 'Biliran', 'BK': 'Bukidnon', 'BT': 'Batangas', 'BU': 'Bulacan', 'SS': 'Surigao del Sur', 
            'BS': 'Basilan', 'DV': 'Davao del Norte', 'ST': 'Surigao del Norte', 'DR': 'Davao del Sur', 'LG': 'Laguna', 'IB': 'Isabela', 'MT': 'Mountain', 'LN': 'Lanao del Norte', 'TT': 'Tawi-Tawi', 
            'NC': 'Cotabato', 'ND': 'Negros Occidental', 'NE': 'Nueva Ecija', 'ZS': 'Zamboanga del Sur', 'QZ': 'Quezon', 'SK': 'Sultan Kudarat', 'LU': 'La Union', 'ZM': 'Zambales', 'LS': 'Lanao del Sur', 'NR': 'Negros Oriental', 'IF': 'Ifugao', 
            'PN': 'Pangasinan', 'IS': 'Ilocos Sur', 'NV': 'Nueva Vizcaya', 'PM': 'Pampanga', 'RO': 'Romblon', 'GU': 'Guimaras', 'AB': 'Abra', 'QR': 'Quirino', 'CN': 'Camarines Norte', 
            'CM': 'Camiguin', 'CL': 'Compostela Valley', 'ZN': 'Zamboanga del Norte', 'CB': 'Cebu', 'AK': 'Aklan', 'SL': 'Southern Leyte', 'CG': 'Cagayan', 'AL': 'Albay', 'AN': 'Agusan del Norte', 
            'AQ': 'Antique', 'AP': 'Apayao', 'AS': 'Agusan del Sur', 'LE': 'Leyte', 'AU': 'Aurora', 'ZY': 'Zamboanga-Sibugay', 'IN': 'Ilocos Norte', 'CS': 'Camarines Sur', 'MD': 'Misamis Occidental', 'CP': 'Capiz', 'CV': 'Cavite', 'ES': 'Eastern Samar', 
            'CT': 'Catanduanes', 'II': 'Iloilo', 'KA': 'Kalinga', 'NS': 'Northern Samar', 'MC': 'Occidental Mindoro', 'MB': 'Masbate', 'DC': 'Davao Occidental', 'SR': 'Sorsogon', 'SQ': 'Siquijor', 
            'MN': 'Misamis Oriental', 'SU': 'Sulu', 'RI': 'Rizal', 'MG': 'Maguindanao', 'MM': 'Metropolitan Manila', 'MQ': 'Marinduque', 'PW': 'Palawan', 'SM': 'Samar', 'MR': 'Oriental Mindoro', 'SC': 'South Cotabato', 'SG': 'Sarangani','SF':'Shariff Kabunsuan'}

for a in files:
    if a in fnmatch.filter(files,'*.csv'):
        csvf = os.path.join(root,a)
#        print csvf
        with open(csvf,'rb') as dataf:
            reader = csv.DictReader(dataf)
            for row in reader:
                cc = row['maximum']
                code = row['Station'][-2:]
#                try:
                aa = provCode[code]
#                except KeyError:
#                    continue
                data[aa].append(cc)
                
        for x in data.keys():
            maxx = max(data[x])
            dic[x] = maxx

st.append(dic.keys())
ht.append(dic.values())        
#fieldnames = ['Station','Max Surge Height(m)']
#with open(outfile,'wb') as out:
#    dw = csv.DictWriter(out, delimiter = ' ', fieldnames = fieldnames )
#    dw.writeheader()
#    for row in dic:
#        dw.writerow(row)
    
#test = open(outfile,'wb')
#csvwriter = csv.DictWriter(test, delimiter = ' ',fieldnames = fieldnames)
#csvwriter.writeheader(fieldnames)
#for row in dic:
#    csvwriter.writerow(row)
#test.close()
#with open(outfile,'wb') as out:
#    csv_out = csv.writer(out)
#    csv_out.writerow(['MUNICIPALITY','SURGE HEIGHT (meters)'])
#    for row in final:
#        csv_out.writerow(row)
#    out.close()