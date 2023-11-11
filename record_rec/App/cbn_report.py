import csv
import os
import shutil
from shutil import copytree, rmtree
from time import time, ctime
import calendar
import time
import datetime 
import pandas as pd
import glob

#get the unique variable to defferentiate date
#date=input("enter date: yyyy-mm-dd: ")    
CurrentDate=datetime.date.today()  
days = datetime.timedelta(27)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#hff
#%d is for date  dd
#%m is for month  mm
#Y is for Year  yyyy
date=final_date
print(final_date)

from datetime import datetime

# get today's datetime
now = datetime.now()
print('DateTime:', now)

print('Month Number:', now.month)
print('Month full name:', now.strftime('%B'))
print('Month short name:', now.strftime('%b'))
month=f"{now.strftime('%B')}"
#path2 is the location of where we are copying from and where we are copying to
path2='App/locations.csv'
path='App/bank_code_cbnmove.csv'
with open(path, 'r') as file_object:
    reader = csv.reader(file_object, delimiter=',', quotechar='"')
    for row1 in reader:
        print(f'{row1[:]}')
        
        print(str(f"'{row1}'"), sep=",")

        try:
            
            source=f'C:/python_work/record_rec/Comparism_report{row1[0]}.csv'
            dest=f'C:/python_work/record_rec/CBN/Comparism_report_{row1[1]}.csv'
            source1=f'C:/python_work/record_rec/summary_report{row1[0]}.csv'
            dest1=f'C:/python_work/record_rec/CBN/summary_report_{row1[1]}.csv'
            source2=f'C:/python_work/record_rec/invalid_BVN_on_ICAD_{row1[0]}.csv'
            dest2=f'C:/python_work/record_rec/CBN/invalid_BVN_on_ICAD_{row1[1]}.csv'
            shutil.copy2(source,dest)
            shutil.copy2(source1,dest1)
            shutil.copy2(source2,dest2)
            
                
                
            
                
        except:
            continue
    
