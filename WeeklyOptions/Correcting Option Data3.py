#import libraries

import sys
import csv
import glob
import os

#Program Flow below
#Go to current directory
#Get list of all folder
#For every folder
    #Find list of all csv files
    #For every file in csv
        #open a temp file
        #write new row with changed attribute into it
        #del original file
        #rename temp file as old file


parent_dir = './Weekly Options/2020'
folder_list = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]
print(folder_list)
for i in folder_list:
    current_dir = parent_dir + '/' + i + '/'
    print('Searching in ' + current_dir)
    csv_file_list = glob.glob(current_dir + '/*.csv')
    for j in csv_file_list:
        current_csv_file_path = j
        current_csv_file_path = current_csv_file_path.replace('\\', '/')
        print(current_csv_file_path)
        temp_file_path = current_dir + 'temp.csv'
        with open(current_csv_file_path) as csv_file, open(temp_file_path,'w', newline='') as temp_file:
            current_csv_file = current_csv_file_path.replace(current_dir , '')
            current_csv_file = current_csv_file.replace('.csv' , '')
            csv_writer = csv.writer(temp_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for k in csv_reader:
                csv_writer.writerow([current_csv_file, k[1], k[2], k[3], k[4], k[5], k[6], k[7]])
            csv_file.close()
            temp_file.close()
            os.remove(current_csv_file_path)
            os.rename(temp_file_path,current_csv_file_path)