#import libraries

import sys
import csv
import glob
import os

#Program Flow below
#Enter correct path to current month
#Get list of all csv
#For every csv
    #Remove everything except name from path
    #Make new name
    #Replace old name with new name


parent_dir = './Weekly Options/2019/Expiry 28th March'
current_dir_csvlist = glob.glob(parent_dir + '/*.csv')
for i in current_dir_csvlist:
    csv_file = i
    print(csv_file)
    csv_file = csv_file.replace(parent_dir + '\\', '')
    CE_PE = csv_file[0:2]
    STRIKE = csv_file[3:8]
    dst = parent_dir + '/NIFTY28MAR19' + STRIKE + CE_PE + '.csv'
    print('1' + dst)
    src = i.replace('\\','/')
    #print(parent_dir + '/NIFTY02MAY19' + csv_file)
    #print(i.replace('\\','/'))
    os.rename(src, dst)