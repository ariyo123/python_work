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
#open the location list and convert to a python list
with open(path2, 'r') as file_object:
    reader = csv.reader(file_object, delimiter=',', quotechar='"')
    for row in reader:
        try:
            #print(row)
            source=str(row[0])
            #print(source)
            
            dest=f"{str(row[1])}{month}/"
            os.mkdir(dest)
            print(f"copying {source}  to  {dest}\n")
            print("Done copying\n")
            shutil.copy2(source,dest)
        
            
        except:
            continue
    
for path in os.listdir("c:/python_work/record_rec"):
    print(path)