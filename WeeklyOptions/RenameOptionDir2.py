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
    folder_name = folder_name.replace('19','20')
    folder_name = folder_name.replace('\\','/')
    dst = folder_name
    src = i.replace('\\','/')
    print('1' + src)
    #print(parent_dir + '/NIFTY02MAY19' + csv_file)
    #print(i.replace('\\','/'))
    os.rename(src, dst)
