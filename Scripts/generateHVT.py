# -*- coding: utf-8 -*-

"""
This code is use to generate the hvt files that are used in flo2D for simulating historical typhoon surges.
The inputs are: 
    root: the root folder of tides.txt files generated from wxTide. The text files should be inside a folder
          with name formatted as TyphoonDATE i.e. Yolanda2013
    provCode: the code used in determining the province
    
"""
import os,fnmatch,re
import glob
import datetime
import itertools
import shutil
from interpolate import alphanum
from interpolate import surgetotide_dict
from interpolate import interpolator_generator
#from interpolate import prov
#from phillip import listdir_fullpath
from makeHvt import hvt
import numpy as np

##Do not forget to change the provinvial code!
##
root = raw_input("Enter the root of tidepath: ")
provCode = raw_input("Enter the code for the province: ")
listDir = os.listdir(root)
count = 0
for folder in listDir: 
    TIDEPATH = os.path.join(root,folder) #raw_input("Enter the tidepath: ") #r'C:\Users\Windows User\Desktop\Work\Fieldworks\SorsogonOutputs\Tides\Reming2006'

##for root, dirnames, filenames in os.walk(TIDEPATH):
##    for filename in fnmatch.filter(filenames, '*.txt'):
##        print "root: " + root
    getName = os.path.abspath(os.path.join(TIDEPATH,'..','..',''))
#    print getName
    getProv = os.path.split(getName)
    prov = getProv[1][:-7]
#    print "prov: "+ prov
    #
    ##Path to tide text files
    aa = os.path.split(TIDEPATH)
    print aa[0]
    TARGETPATH = os.path.abspath(os.path.join(TIDEPATH,'..','..','HVT','%s'%aa[1][:-4].lower()))
#    TARGETPATH = os.path.abspath(os.path.join(TIDEPATH,'..','..','%s'%aa[1][:-4].lower()))
    print "targetpath: "+ TARGETPATH
#     Path where output (surge + tide) will be saved
    try:
        hvtFolder = os.mkdir(os.path.join(aa[0],'..','HVT'))
    except WindowsError:
        pass
    if not os.path.isdir(TARGETPATH):         
        target = os.mkdir(TARGETPATH)             
        csvPath = os.path.abspath(os.path.join(TARGETPATH, 'total'))
        outPathDir = os.path.abspath(os.path.join(csvPath, 'HVT_{}_{}'.format(aa[1][:-4].upper(),prov.upper()))) # Path where HVT will be saved
        #print TARGETPATH
        # Typhoon name
        tyname = '{}_{}'.format(aa[1][-4:],aa[1][:-4].lower())

    
    

#### Old code
##TARGETPATH = r'C:\Users\Windows User\Desktop\Work\Fieldworks\AlbayOutputs\caloy'
##csvPath = os.path.join(TARGETPATH, 'total')
### Path where HVT will be saved
##outPathDir = os.path.join(csvPath, 'HVT_CALOY_ALBAY')
### Typhoon name
##tyname = '2006_caloy'
####----------
#
##STATIONLISTPATH = [r'C:\Users\Windows User\Desktop\Work\MindoroOutputs\JMA_Simulation\chanchu\timeseries']
        STATIONLISTPATH = [r'G:\Actual Strength Simulation',
           r'H:\ACTUAL STRENGTH SIMULATIONS']
##STATIONLISTPATH = [r'/home/phillip/Desktop/JMA_simulated/rammayan']
#
##davaoOriental = ["Banao, Baganga, DO",  "Baon, Sn Isidro, DO",  "Batobato, Sn Isidro, DO",  "Baybay, Cateel, DO",   "Bitaogan, Sn Isidro, DO",  "Bobon, Mati , DO", "Bobonao, Baganga, DO", "Cabangcalan, Banaybanay, DO",  "Cabasagan, Boston, DO",    "Cabuaya, Mati , DO",   "Calapagan, Lupon, DO", "Calubihan, Banaybanay, DO",    "Cawayanan, Boston, DO",    "Central, Manay, DO",   "Central, Tarragona, DO",   "Concepcion, Manay, DO",    "Crispin Dela Cruz, Gov. Generoso, DO", "Dahican, Mati , DO",   "Dapnan, Baganga, DO",  "Dn Aurelio Chicote, Gov. Generoso,DO", "Don Enrique Lopez, Mati , DO", "Holy Cross, Manay, DO",    "Jovellar, Tarragona, DO",  "Kinablangan, Baganga, DO", "Lambajon, Baganga, DO",    "Langka, Mati , DO",    "Lantawan, Lupon, DO",  "Lavigan, Gov. Generoso, DO",   "Limbahan, Lupon, DO",  "LU, Sn Isidro, DO",    "Luban, Mati , DO", "Lucatan, Tarragona, DO",   "Luzon, Gov. Generoso, DO", "Macambol, Mati , DO",  "Macangao, Lupon, DO",  "Manuel Roxas, Gov. Generoso, DO",  "Mogbongcogon, Banaybanay, DO", "Monserrat, Gov. Generoso, DO", "Nangan, Gov. Generoso, DO",    "Palma Gil, Caraga, DO",    "Pbcn., Boston, DO",    "Pbcn., Caraga, DO",    "Pbcn., Cateel, DO",    "Pbcn., Gov. Generoso, DO", "Pbcn., Lupon, DO", "Pundaguitan, Gov. Generoso, DO",   "Punta Linao, Banaybanay, DO",  "Rang-Ay, Banaybanay, DO",  "Salingcomot, Baganga, DO", "Santiago, Caraga, DO", "Sn Antonio, Cateel, DO",   "Sn Ignacio, Manay, DO",    "Sn Isidro, Manay, DO", "Sn Luis, Caraga, DO",  "Sn Miguel, Caraga, DO",    "Sn Victor, Baganga, DO",   "Sta. Filomena, Cateel, DO",    "Surop, Gov. Generoso, DO", "Tagabebe, Gov. Generoso, DO",  "Tagbinonga, Mati , DO",    "Talisay, Sn Isidro, DO",   "Tamban, Gov. Generoso, DO",    "Tamisan, Mati , DO",   "Tibanban, Gov. Generoso, DO",  "Tiblawan, Gov. Generoso, DO",  "Zaragosa, Manay, DO"]
##leyteGroup5 = ["Bahay, Abuyog, LE", "Bgy. 58, Tacloban , LE", "Bgy. 83-A , Tacloban , LE",  "Bgy. 83-B, Tacloban , LE", "Bgy. 85 , Tacloban , LE",  "Bgy. 86, Tacloban , LE", "Bgy. 89, Tacloban , LE", "Bislig, Tanauan, LE",  "Buaya, Abuyog, LE",  "Buenavista, Abuyog, LE", "Bulak, Abuyog, LE",  "Bunga, Abuyog, LE",  "Buntay , Abuyog, LE",  "Candao , Dulag, LE", "Casalungan, Javier, LE", "Gen. Antonio Luna, Mayorga, LE", "Imelda, Tolosa, LE", "Lawa-An, Abuyog, LE",  "Luan, Dulag, LE",  "Malaguicay, Abuyog, LE", "Maya, Macarthur, LE",  "Opong, Tolosa, LE",  "Pbcn. District 2, Macarthur, LE",  "Pbcn. Zone 1, Mayorga, LE",  "RI, Dulag, LE",  "Sabang Daguitan, Dulag, LE", "Salvacion, Basey, SM", "Santo Nino Pbcn. , Tanauan, LE", "Sn Fernando, Palo, LE",  "Sn Francisco, Abuyog, LE", "Sn Joaquin, Palo, LE", "Sn Pedro, Macarthur, LE",  "Sn Rafael, Dulag, LE", "Sn Roque , Tanauan, LE", "Sn Roque, Abuyog, LE", "Sn Roque, Tolosa, LE", "Sta. Cruz, Mayorga, LE", "Sta. Cruz, Tanauan, LE", "Sta. Lucia , Abuyog, LE",  "Tanghas, Tolosa, LE",  "Telegrafo, Tolosa, LE",  "Tib-O, Abuyog, LE",  "Union, Mayorga, LE"]
##metroManila = ["Baclaran, Paranaque, MM",  "Bgy. 275, MM, MM", "Bgy. 649, MM, MM", "n.a, Las Pinas, MM", "n.a, MM, MM",  "n.a, Pasay , MM",  "North Bay Blvd., South, Navotas, MM",  "Sn Jose, Navotas, MM", "Tambo, Paranaque, MM", "Tangos, Navotas, MM",  "Tanza, Navotas, MM"]
##manilaBay = ["Alangan, Limay, BA",    "Amaya II, Tanza, CV",    "Baclaran, Paranaque, MM",    "Balut , Orion, BA",    "Balut I, Pilar, BA",    "Bambang, BU, BU",    "Bancaan, Naic, CV",    "Bantan Munti, Pilar, BA",    "Bgy. 11 , CV , CV",    "Bgy. 275, MM, MM",    "Bgy. 49 , CV , CV",    "Bgy. 53 , CV , CV",    "Bgy. 62 , CV , CV",    "Bgy. 649, MM, MM",    "Bgy. 8 , CV , CV",    "Binuangan, Obando, BU",    "BT II, Mariveles, BA",    "Cabcaben, Mariveles, BA",    "Calibuyo, Tanza, CV",    "Camachile, Orion, BA",    "Capipisa, Tanza, CV",    "Halayhay, Tanza, CV",    "Labac, Naic, CV",    "Lamao, Limay, BA",    "Lucanin, Mariveles, BA",    "Mabatang, Abucay, BA",    "Masukol, Paombong, BU",    "Munting Mapino, Naic, CV",    "Muzon II, Rosario, CV",    "n.a, Las Pinas, MM",    "n.a, MM, MM",    "n.a, Pasay , MM",    "North Bay Blvd., South, Navotas, MM",    "Omboy, Abucay, BA",    "Pamarawan, Malolos , BU",    "Pbcn., Limay, BA",    "Perez, BU, BU",    "Pugad, Hagonoy, BU",    "Sapang Kawayan, Masantol, PM",    "Sn Jose, Navotas, MM",    "Sn Juan II, Ternate, CV",    "Sn Pascual, Hagonoy, BU",    "Sn Rafael II, Noveleta, CV",    "Sn Roque, Hagonoy, BU",    "St. Francis II, Limay, BA",    "Sta. Cruz, Paombong, BU",    "Sta. Elena, Orion, BA",    "Sta. Ines, BU, BU",    "Tambo, Paranaque, MM",    "Tangos, Navotas, MM",    "Tanza, Navotas, MM",    "Tibaguin, Hagonoy, BU",    "Tortugas, Balanga , BA",    "Townsite, Mariveles, BA",    "Villa Angeles , Orion, BA"]
##samarLeyte = ["Amambucale, Marabut, SM",	"Amandayehan, Basey, SM",	"Bacubac, Basey, SM",	"Basiao, Basey, SM",	"Bgy. 58, Tacloban , LE",	"Bgy. 83-A , Tacloban , LE",	"Bgy. 83-B, Tacloban , LE",	"Bgy. 85 , Tacloban , LE",	"Bgy. 86, Tacloban , LE",	"Bgy. 89, Tacloban , LE",	"Binongtu-an, Basey, SM",	"Binukyahan, Marabut, SM",	"Bislig, Tanauan, LE",	"Candao , Dulag, LE",	"Canyoyo, Marabut, SM",	"Ferreras, Marabut, SM",	"Iba, Basey, SM",	"Imelda, Tolosa, LE",	"Legaspi, Marabut, SM",	"Loyo , Basey, SM",	"Luan, Dulag, LE",	"Mabuhay, Marabut, SM",	"Nouvelas Occidental, Basey, SM",	"Opong, Tolosa, LE",	"Osmena, Marabut, SM",	"Pbcn. Zone 1, Mayorga, LE",	"RI, Dulag, LE",	"Sabang Daguitan, Dulag, LE",	"Salvacion, Basey, SM",	"Santo Nino Pbcn. ,  Marabut, SM",	"Santo Nino Pbcn. , Tanauan, LE",	"Sn Antonio, Basey, SM",	"Sn Fernando, Palo, LE",	"Sn Joaquin, Palo, LE",	"Sn Rafael, Dulag, LE",	"Sn Roque , Tanauan, LE",	"Sn Roque, Marabut, SM",	"Sn Roque, Tolosa, LE",	"Sta. Cruz, Tanauan, LE",	"Sta. Rita, Marabut, SM",	"Tanghas, Tolosa, LE",	"Telegrafo, Tolosa, LE",	"Tinaogan, Basey, SM",	"Tingib, Basey, SM",	"Veloso, Marabut, SM"]
##easternSamarGroup1 = ["Bacjao, Balangiga, ES", "Balud, Salcedo, ES", "Banaag, Guiuan, ES", "Betaog, Lawaan, ES", "Bgy. Pbcn. V, Balangiga, ES",  "Biga, Giporlos, ES", "Bobon, Mercedes, ES",  "Bolusao, Lawaan, ES",  "Buenavista, Guiuan, ES", "Bungtod, Guiuan, ES",  "Cagaut, Salcedo, ES",  "Camanga, Salcedo, ES", "Camparang, Guiuan, ES",  "Campoyong, Guiuan, ES",  "Cantomoja, Salcedo, ES", "Carapdapan, Salcedo, ES",  "Gigoso, Giporlos, ES", "Guinob-An, Lawaan, ES",  "Maliwaliw, Salcedo, ES", "Maslog, Lawaan, ES", "Parina, Giporlos, ES", "Paya, Giporlos, ES", "Salug, Guiuan, ES",  "Sn Jose, Guiuan, ES",  "Sn Miguel, Balangiga, ES", "Sn Pedro, Guiuan, ES", "Sta. Margarita, Quinapondan, ES",  "Sulangan, Guiuan, ES", "Taguite, Lawaan, ES",  "Trinidad, Guiuan, ES", "Victory Island, Guiuan, ES", "Canawayon, Guiuan, ES",  "Culasi, Guiuan, ES", "Inapulangan, Guiuan, ES"]
##easternSamarGroup2 = ["Abejao, Salcedo, ES", "Abucay , Sulat, ES", "Aguinaldo, Gen. Macarthur, ES",  "Alog, Salcedo, ES",  "Ando, Borongan , ES",  "Anuron, Mercedes, ES", "Asgad, Salcedo, ES", "Bagua, Guiuan, ES",  "Baras, Guiuan, ES",  "Barbo, Guiuan, ES",  "Batang, Hernani, ES",  "Batiawan, Taft, ES", "Bato, Borongan , ES",  "Baybay , Sulat, ES", "Beri, Arteche, ES",  "Bgy. 12 , Dolores, ES",  "Bgy. 2 Pbcn., Mercedes, ES", "Bgy. 4 , Hernani, ES", "Bgy. No. 1 , Sn Policarpo, ES",  "Bgy. No. 3 , Sn Policarpo, ES",  "Bgy. No. 3 Pbcn., Sn Julian, ES",  "Bgy. No. 5 , Sn Policarpo, ES",  "Bgy. Pbcn. 7, Maydolong, ES",  "Binalay, Gen. Macarthur, ES",  "Binogawan, Sn Policarpo, ES",  "Buenavista, Quinapondan, ES",  "Bugas, Borongan , ES", "Burak, Salcedo, ES", "Cajagwayan, Sn Policarpo, ES", "Canciledes, Hernani, ES",  "Canjaway, Borongan , ES",  "Cansangaya, Can-Avid, ES", "Canteros, Can-Avid, ES", "Carapdapan, Arteche, ES",  "Caridad, Salcedo, ES", "Carolina, Can-Avid, ES", "Dacul, Taft, ES",  "Dapdap, Dolores, ES",  "Del Remedio, Sulat, ES", "Divinubo, Borongan , ES",  "Domrog, Gen. Macarthur, ES", "Garawon, Hernani, ES", "Garden , Arteche, ES", "Habag, Guiuan, ES",  "Hilabaan, Dolores, ES",  "Jagnaya, Salcedo, ES", "Japitan, Dolores, ES", "Lalawigan, Borongan , ES", "Locso-On, Borongan , ES",  "Malingon, Oras, ES", "Maramag, Balangkayan, ES", "Matarinao, Salcedo, ES", "Maybocog, Maydolong, ES",  "Mina-anod, Llorente, ES",  "Naga, Quinapondan, ES",  "Natividad, Sn Policarpo, ES",  "Nato, Taft, ES", "Naubay, Llorente, ES", "Ngolos, Guiuan, ES", "Omawas, Maydolong, ES",  "Pagbabangnan, Guiuan, ES", "Pagbabangnan, Sn Julian, ES",  "Pagnamitan, Guiuan, ES", "Pbcn. Bgy. 1, Taft, ES", "Pbcn. Bgy. 2, Gen. Macarthur,ES",  "Pbcn. I, Balangkayan, ES", "Piliw, Llorente, ES",  "Punta Maria, Borongan , ES", "Rawis, Can-Avid, ES",  "Sabang North, Borongan , ES",  "Santo Nino, Sulat, ES",  "Sapao, Guiuan, ES",  "Saugan, Oras, ES", "Sn Francisco, Sulat, ES",  "Sn Luis, Taft, ES",  "Sn Roque , Salcedo, ES", "Sn Roque, Llorente, ES", "Sn Vicente, Sulat, ES",  "Songco, Borongan , ES",  "Sta. Monica, Oras, ES",  "SUan, Guiuan, ES", "Suribao, Borongan , ES", "Tabo, Sn Policarpo, ES", "Tabok, Llorente, ES"]
##aklan = ["Afga, Tangalan, AK", "Agbago, Ibajay, AK", "Alegria, Buruanga, AK", "Alimbo-Baybay, Nabas, AK","Argao, Malay, AK", "Aslum, Ibajay, AK","Bachaw Norte, Kalibo, AK", "Bachaw Sur, Kalibo, AK",   "Bagongbayan, Buruanga, AK",    "Balabag, Malay, AK",   "Balusbus, Malay, AK",  "Baybay, Makato, AK",   "Baybay, Tangalan, AK", "Bel-Is, Buruanga, AK", "Buenasuerte, Nabas, AK",   "Bugtongbato, Ibajay, AK",  "Buswang New, Kalibo, AK",  "Camanci Norte, Numancia, AK",  "Caticlan, Malay, AK",  "Cawayan, New Washington, AK",  "Colongcolong, Ibjaya, AK", "Dapdap, Tangalan, AK", "Dumatad, Tangalan, AK",    "Fatima, New Washington, AK",   "Gibon, Nabas, AK", "Habana, Nabas, AK",    "Jawili, Tangalan, AK", "Katipunan, Buruanga, AK",  "Libertad, Nabas, AK",  "Mabilo, Kalibo, AK",   "Mambuquiao, Batan, AK",    "Manoc-Manoc, Malay, AK",   "Naasug, Malay, AK",    "Naisud, Ibajay, AK",   "Napti, Batan, AK", "Navitas, Numancia, AK",    "Ochando, New Washington, AK",  "Ondoy, Ibajay, AK",    "Panilongan, Buruanga, AK", "Pbcn., Nabas, AK", "Pbcn., New Washington, AK",    "Pbcn., Tangalan, AK",  "Pook, Kalibo, AK", "Pusiw, Numancia, AK",  "Sn Isidro, Ibajay, AK",    "Songcolan, Batan, AK", "Tagbaya, Ibajay, AK",  "Tambak, New Washington, AK",   "Tigum, Buruanga, AK",  "Toledo, Nabas, AK",    "Unidos, Nabas, AK",    "Union, Nabas, AK", "Yapak, Malay, AK"]
##antique = ["Abiera, Sebaste, AQ", "Aguila, Sebaste, AQ", "Amparo, Patnongon, AQ", "Apgahan, Patnongon, AQ",  "Aras-Asan, Sebaste, AQ",   "Aras-Asan, Tobias Fornier, AQ",    "Arobo, Tobias Fornier, AQ",    "Asluman, Hamtic, AQ",  "Atabay, Tobias Fornier, AQ",   "Bacalan, Sebaste, AQ", "Bagongbayan, Laua-An, AQ", "Bahuyan, Barbaza, AQ", "Balac-Balac, Culasi, AQ",  "Banawon, Hamtic, AQ",  "Banban, Laua-An, AQ",  "Batbatan Island, Culasi, AQ",  "Batonan Sur, Culasi, AQ",  "Baybay, Pandan, AQ",   "Bayo Grande, Anini-Y, AQ", "Bgy. 4 , Sn Jose, AQ", "Bitadton Norte, Culasi, AQ",   "Borocboroc, Belison, AQ",  "Bulanao, Libertad, AQ",    "Butuan, Anini-Y, AQ",  "Calala, Hamtic, AQ",   "Callan, Sebaste, AQ",  "Camangahan, Bugasong, AQ", "Caridad, Culasi, AQ",  "Carit-An, Patnongon, AQ",  "Casay, Anini-Y, AQ",   "Centro Pbcn., Culasi, AQ", "Centro Weste , Libertad, AQ",  "Diclum, Tobias Fornier, AQ",   "Dumrog, Pandan, AQ",   "Durog, Sn Jose, AQ",   "Duyong, Pandan, AQ",   "Funda, Hamtic, AQ",    "Funda-Dalipe, Sn Jose, AQ",    "Gua, Barbaza, AQ", "Guija, Bugasong, AQ",  "Guisijan, Laua-An, AQ",    "Iba, Anini-Y, AQ", "Idiacacan, Pandan, AQ",    "Idio, Sebaste, AQ",    "Igbarawan, Patnongon, AQ", "Igcagay, Libertad, AQ",    "Ilaures, Bugasong, AQ",    "La Paz, Hamtic, AQ",   "La Paz, Tibiao, AQ",   "Lindero, Laua-An, AQ", "Lipata, Culasi, AQ",   "Lisub B, Anini-Y, AQ", "Mabasa, Patnongon, AQ",    "Madrangca, Sn Jose, AQ",   "Mag-Aba, Pandan, AQ",  "Magdalena, Anini-Y, AQ",   "Magsaysay, Patnongon, AQ", "Malabor, Tibiao, AQ",  "Malalison Island, Culasi, AQ", "Mapatag, Hamtic, AQ",  "Martinez, Tibiao, AQ", "Masayo, Tobias Fornier, AQ",   "Maybato Sur, Sn Jose, AQ", "Naba, Culasi, AQ", "Nato, Anini-Y, AQ",    "Nauhon, Sebaste, AQ",  "Oloc, Laua-An, AQ",    "Paciencia, Tobias Fornier, AQ",    "Paliwan, Bugasong, AQ",    "Palma, Barbaza, AQ",   "Patria, Pandan, AQ",   "Paz, Libertad, AQ",    "Pbcn. , Laua-An, AQ",  "Pbcn., Barbaza, AQ",   "Pbcn., Belison, AQ",   "Pbcn., Patnongon, AQ", "Pbcn., Sebaste, AQ",   "Pbcn., Tibiao, AQ",    "Pu-Aoc, Hamtic, AQ",   "Pucio, Libertad, AQ",  "Salvacion, Anini-Y, AQ",   "Salvacion, Belison, AQ",   "Sn Antonio, Barbaza, AQ",  "Sn Antonio, Culasi, AQ",   "Sn Fernando, Sn Jose, AQ", "Sn Francisco, Anini-Y, AQ",    "Sn Isidro, Tibiao, AQ",    "Sn Pedro, Sn Jose, AQ",    "Sn Roque, Anini-Y, AQ",    "Sn Roque, Libertad, AQ",   "Talisayan, Anini-Y, AQ",   "Tinigbas, Libertad, AQ",   "Union, Libertad, AQ",  "Zaldivar, Pandan, AQ"]
##capiz = ["Agojo, Panay, CP", "Balaring, Ivisan, CP", "Balogo, Pilar, CP","Basiao, Ivisan, CP","Baybay, Roxas , CP","Binaobawan, Pilar, QZ","Buntod, Panay, CP","Butacal, Panay, CP", "Cagay, Roxas , CP",    "Casanayan, Pilar, CP", "Cogon, Roxas , CP",    "Culasi, Roxas , CP",   "Dayhagan, Pilar, CP",  "Dulangan, Pilar, QZ",  "Libas, Roxas , CP",    "Lonoy, Sapi-An, CP",   "Natividad, Pilar, CP", "Navitas, Panay, CP",   "Olotayan, Roxas , CP", "Pawa, Panay, CP",  "Pbcn., Sapi-An, CP",   "Pinamihagan, President Roxas, CP", "Punta Cogon, nRoxas , CP", "Sn Esteban, Pilar, CP",    "Sn Ramon, Pilar, CP",  "Talon, Roxas , CP",    "Tanza, Roxas, CP" ]
##iloiloGroup1 = ["Alegre, Oton, II",  "Atabayan, Tigbauan, II",   "Bacauan, Miagao, II",  "Balabago, Sn Joaquin, II", "Baras, Guimbal, II",   "Baybay, Sn Joaquin, II",   "Bongol Sn Vicente, Guimbal, II",   "Buyu-An, Tigbauan, II",    "Cabanbanan, Oton, II", "Calampitao, Guimbal, II",  "Calaparan, II , II",   "Cata-An, Sn Joaquin, II",  "Generosa-Cristobal Colon, Guimbal,II", "Guibongan Bayunan, Sn Joaquin, II",    "Guibongan, Miagao, II",    "Igcadium, Sn Joaquin, II", "Igcondao, Sn Joaquin, II", "Lawigan, Sn Joaquin, II",  "Maninila, Miagao, II", "Namocon, Tigbauan, II",    "Oyungan, Miagao, II",  "Parara Sur, Tigbauan, II", "Pbcn. South, Oton, II",    "Purok I , Sn Joaquin, II", "Santo Nino Sur, II , II",  "Sapa , Miagao, II",    "Sinogbuhan, Sn Joaquin, II",   "Siwaragan, Sn Joaquin, II",    "Sn Rafael, Miagao, II",    "Tan Pael, Tigbauan, II",   "Tiolas, Sn Joaquin, II",   "Trapiche, Oton, II"]
##iloiloGroup2 = ["Bigke, Leganes, II",    "Sapao, Dumangas, II"]
##iloiloGroup3 = ["Agdaliran, Sn Dionisio, II",    "Alipata, Carles, II",  "Bacay, Dumangas, II",  "Bacjawan Norte, Concepcion, II",   "Bagongon, Concepcion, II", "Banban, Batad, II",    "Bancal, Carles, II",   "Barosbos, Carles, II", "Barosbos, Carles, II", "Barrido, Ajuy, II",    "Bato Biasong, Ajuy, II",   "Bay-Ang, Ajuy, II",    "Bayas , Estancia, II", "Binon-An, Batad, II",  "Bito-On, Carles, II",  "Borongon, Sn Dionisio, II",    "Botlog, Concepcion, II",   "Buaya, Carles, II",    "Buenavista, Carles, II",   "Cabuguana, Carles, II",    "Culasi, Ajuy, II", "Dangula-An, Anilao, II",   "Dayhagan, Carles, II", "Dayhagan, Carles, II", "Dungon, Concepcion, II",   "Guinticgan, Carles, II",   "Guinticgan, Carles, II",   "Igbon, Concepcion, II",    "Isla De Cana, Carles, II", "Jalaud, Barotac Nuevo, II",    "Lanas, Barotac Nuevo, II", "Loguingot , Estancia, II", "Lo-Ong, Concepcion, II",   "Macatunao, Concepcion, II",    "Malangabang, Concepcion, II",  "Malayu-An, Ajuy, II",  "Maliogliog, Concepcion, II",   "Manipulon, Estancia, II",  "Nanding Lopez, Dumangas, II",  "Nasidman, Ajuy, II",   "Nipa, Concepcion, II", "Nipa, Sn Dionisio, II",    "Odiongan, Sn Dionisio, II",    "Paloc Sool, Dumangas, II", "Pbcn., Carles, II",    "Pbcn., Sn Dionisio, II",   "Pili, Ajuy, II",   "Polopina, Concepcion, II", "PPS, Barotac Viejo, II",   "Punta , Carles, II",   "Punta Buri, Ajuy, II", "Santo Domingo, Barotac Viejo, II", "Silagon, Ajuy, II",    "Sn Carlos, Anilao, II",    "Sn Fernando, Carles, II",  "Sn Francisco, Barotac Viejo, II",  "Sn Salvador, Banate, II",  "Sta. Rita, Anilao, II",    "Sua, Sn Dionisio, II", "Tabugon, Carles, II",  "Tagubanhan, Ajuy, II", "Talingting, Carles, II",   "Talisay, Barotac Nuevo, II",   "Talotu-An, Concepcion, II",    "Tambaliza, Concepcion, II",    "Tanao, Batad, II", "Tanza, Estancia, II",  "Tarong, Carles, II",   "Tiabas, Sn Dionisio, II",  "Tinigban, Carles, II", "Zona Sur, Banate, II"]
##mindoroOriental = ['Aclan River Entr', 'Aguasa Bay', 'Anilao, Balayan Bay', 'Apo Island, Mindoro Str', 'Calapan Bay', 'Cangouac Point, Sibuyan Isl', 'Mangarin', 'Port Concepcion, Maestre de Campo I', 'Port Galera', 'Port Silanguin', 'San Jose']
##sorsogon = ['Batuan Bay, Ticao Isl', 'Biri Island', 'Butag Bay', 'Gubat', 'Port Boca Engano, Burias Isl', 'Port San Miguel, Ticao Isl', 'San Bernardino Island', 'Santa Cruz Harbor', 'Santo Nino, Santo Nino Isl', 'Tabaco, Tabaco Bay', 'Torrijos', 'Virac, Catanduances Isl']
#albay = ['Butag Bay', 'Gubat', 'Port Boca Engano, Burias Isl', 'San Bernardino Island', 'Santa Cruz Harbor', 'Tabaco, Tabaco Bay', 'Tabgon Bay', 'Torrijos', 'Virac, Catanduances Isl']    
#
#        print 'Reading tide data...'
#        xtideFileList = glob.glob(os.path.join(TIDEPATH, '*.txt'))
#        tideStationDict = {}
#        for filename in sorted(xtideFileList):
#            print 'Processing', os.path.basename(filename)
#            with open(filename, 'r') as tideFile:
#                tideData = tideFile.readlines()
#            tideStation = alphanum(tideData[0])
#            for i in range(len(tideData)):
#                if tideData[i].strip('\r\n') == '':
#                    break
#            tideData = tideData[i:]
#            cleanedTideData = []
#            for i in range(len(tideData)):
#                tideData[i] = tideData[i].replace('\r\n', '').split()
#                if tideData[i]:
#                    cleanedTideData.append(tideData[i])
#            for i in range(len(cleanedTideData)):
#                if len(cleanedTideData[i]) < 4:
#                    cleanedTideData[i].append(cleanedTideData[i - 1][3])
#            tideValueDict = {}
#            for i in range(len(cleanedTideData)):
#                if len(cleanedTideData[i][1]) < 5:
#                    cleanedTideData[i][1] = '0' + cleanedTideData[i][1]
#                dataTime = datetime.datetime.strptime(cleanedTideData[i][3] +
#                           cleanedTideData[i][1], '%Y-%m-%d%H:%M') + (
#                           datetime.timedelta(hours=8))
#                tideValueDict[dataTime] = cleanedTideData[i][0]
#            tideStationDict[tideStation] = tideValueDict
#        print '\nDone reading tide data...\n'
        
        print 'Reading tide data...\n'
        xtideFileList = glob.glob(os.path.join(TIDEPATH, '*.txt'))
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

        
        stationListGroup = ['Station List 1',
                            'Station List 2',
                            'Station List 3',
                            'Station List 4',
                            'Station List 5',
                           ]
                           
        stations = itertools.product(STATIONLISTPATH, stationListGroup)
        try:
            os.mkdir(TARGETPATH)
        except:
            pass
        for stationCombination in stations:
            station = os.path.join(stationCombination[0], stationCombination[1])
            if not os.path.exists(station):
                continue
            f = []
            a = os.listdir(station)
            for files in sorted(a):
                etc = os.path.join(station,files)
                final = f.append(etc)
                
            for storm in sorted(f):        
                if tyname in os.path.basename(storm).lower():
                    print storm
                    tsPath = os.path.join(storm, 'timeseries')
                    for ts in glob.glob(os.path.join(tsPath, '*.txt')):
                        print ts
                        with open(ts, 'r') as tsfile:
                            header = tsfile.readline()
                            staName = header[21:59].strip()
                        # Filter to specific provinces
                        if staName.endswith(provCode.upper()):
                            print staName
                            try:
                                destFile = os.path.join(TARGETPATH ,
                                                        os.path.basename(storm) +
                                                        '_' + os.path.basename(ts)
                                                       )
                                shutil.copyfile(ts, destFile)
                            except:                        
                                pass
                        else:
                            continue
                        print destFile
                else:
                    continue
        
        
        jmaFileList = glob.glob(os.path.join(TARGETPATH , '[0-9]*.txt'))
        try:
            os.mkdir(os.path.join(TARGETPATH , 'total'))
            os.mkdir(os.path.join(TARGETPATH , 'maximum'))
        except OSError:
            pass
        #~ Get surge values from JMA output
        #~ One value corresponds to an entry on the list.
        #~ entry format : [YYYY/MM/DD, HH:MM, value(cm)]
        #~ surgeStationDict={surge_station1:{time1:value1,
                                           #~ time2:value2,
                                           #~ time3:value3
                                           #~ ...},
                           #~ surge_station2:{time1:value1,
                                           #~ time2:value2,
                                           #~ time3:value3
                                           #~ ...},
                           #~ ...}
        surgeStationDict = {}
        for filename in jmaFileList:
            with open(filename, 'r') as surgeFile:
                surgeData = surgeFile.readlines()
            header = surgeData[0]
            surgeStation = alphanum(header[21:59])
            surgeData = surgeData[1:]
            surgeData = [data.replace('\n', '').split()[1:4] for data in surgeData]
            surgeValueDict = {}
            for line in surgeData:
                dataTime = datetime.datetime.strptime(line[0] +
                           line[1], '%Y/%m/%d%H:%M') + (
                           datetime.timedelta(hours=8))
                surgeValueDict[dataTime] = float(line[2]) / 100
            surgeStationDict[surgeStation] = surgeValueDict
        
        firstMax = True
        for station in sorted(surgeStationDict.keys()):
            surgeValueDict = surgeStationDict[station]
            for longStation in surgetotide_dict.keys():
                if station in longStation:
                    matchStation = longStation
        
            vertex1 = alphanum(surgetotide_dict[matchStation]['V1'])
            vertex2 = alphanum(surgetotide_dict[matchStation]['V2'])
            vertex3 = alphanum(surgetotide_dict[matchStation]['V3'])
            tideValue1Dict = tideStationDict[vertex1]
            tideValue2Dict = tideStationDict[vertex2]
            tideValue3Dict = tideStationDict[vertex3]
            interpolate = interpolator_generator(
                              surgetotide_dict[matchStation]['V1_LONG'],
                              surgetotide_dict[matchStation]['V1_LAT'],
                              surgetotide_dict[matchStation]['V2_LONG'],
                              surgetotide_dict[matchStation]['V2_LAT'],
                              surgetotide_dict[matchStation]['V3_LONG'],
                              surgetotide_dict[matchStation]['V3_LAT'],
                              surgetotide_dict[matchStation]['LONG'],
                              surgetotide_dict[matchStation]['LAT']
                          )
        
            interpolatedTideDict = {}
            for dataTime in list(set(tideValue1Dict.keys())&set(tideValue2Dict.keys())&set(tideValue3Dict.keys())):
                interpolatedTideDict[dataTime] = interpolate(
                                               float(tideValue1Dict[dataTime]),
                                               float(tideValue2Dict[dataTime]),
                                               float(tideValue3Dict[dataTime])
                                               )
                                               
            interpolatedTideTimeList, interpolatedTideValueList = zip(*interpolatedTideDict.items())
            maxInterpolatedTide = max(interpolatedTideValueList)
        
            surgeTimeList, surgeValueList = zip(*surgeValueDict.items())
            maxSurge = max(surgeValueList)
        
            """
            #Uncomment this section if you want to align the maximums
            maxTideTime = interpolatedTideTimeList[interpolatedTideValueList.index(maxInterpolatedTide)]
            maxSurgeTime = surgeTimeList[surgeValueList.index(maxSurge)]
            newsurgevalue_dict={}
            for dataTime in surgeValueDict.keys():
                newsurgevalue_dict[dataTime-maxSurgeTime+maxTideTime]=surgeValueDict[dataTime]
            del surgeValueDict
            surgeValueDict=newsurgevalue_dict
            del newsurgevalue_dict
            """
        
            commonTime = list(set(interpolatedTideDict.keys())&set(surgeValueDict.keys()))
            commonTime.sort()
            print matchStation
        
            filename = matchStation + '.xls'
            first = True
            stormTide = [str(surgeValueDict[dataTime]) + '\t' + str(interpolatedTideDict[dataTime])
                         + '\t' + str(interpolatedTideDict[dataTime] + surgeValueDict[dataTime])
                         for dataTime in commonTime]
            for dataTime, stormTideValue in zip(commonTime, stormTide):
                dataLine = dataTime.strftime('%m-%d-%Y\t%H:%M\t') + (stormTideValue)
                if first:
                    outputFile = open(os.path.join(TARGETPATH , 'total', filename), 'w')
                    outputFile.write(dataLine + '\n')
                    outputFile.close()
                    first = False
                else:
                    outputFile = open(os.path.join(TARGETPATH , 'total', filename), 'a') 
                    outputFile.write(dataLine + '\n')
                    outputFile.close()
        
            maxStormTide = max(stormTide)
            maxTime = commonTime[stormTide.index(maxStormTide)]
            if firstMax:
                maxFile = open(os.path.join(TARGETPATH , 'maximum/maxStormTide.csv'), 'w')
                line = (surgetotide_dict[matchStation]['VERBOSE_NAME'] + '\t' +
                        str(maxStormTide) + '\t' + maxTime.strftime('%m-%d-%Y %H:%M, ')
                       )
                maxFile.write(line + '\n')
                maxFile.close()
                firstMax = False
            else:
                maxFile = open(os.path.join(TARGETPATH , 'maximum/maxStormTide.csv'), 'a')
                line = (surgetotide_dict[matchStation]['VERBOSE_NAME'] + '\t' +
                        str(maxStormTide) + '\t' + maxTime.strftime('%m-%d-%Y %H:%M, ')
                       )
                maxFile.write(line + '\n')
                maxFile.close()
                
        hvt(csvPath, outPathDir)
        listDir = os.listdir(outPathDir)
        for item in listDir:
            pather = os.path.join(outPathDir,item)
            f = open(pather, 'r+')
            text = f.read()
            text = re.sub('\n', '', text)
            f.seek(0)
            f.write(text)
            f.truncate()
            f.close()
    else:
        print "Directory exist"