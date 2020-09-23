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

parent_dir = './Weekly Options/2020'
folderlist = glob.glob(parent_dir + '/*')
for i in folderlist:
    folder_name = i
    folder_name = folder_name.replace(parent_dir + '\\Expiry ', '')
    day = folder_name[0:2]
    month = folder_name[5:8]
    month = month.upper()
    folder_name = day + month + '19'
    dst = parent_dir + '/' + folder_name
   # print('1' + dst)
    src = i.replace('\\','/')
    #print(parent_dir + '/NIFTY02MAY19' + csv_file)
    #print(i.replace('\\','/'))
    os.rename(src, dst)
