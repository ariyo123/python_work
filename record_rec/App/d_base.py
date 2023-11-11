import os
from unittest import result
import csv
import datetime
import time
import mysql.connector as msql
from mysql.connector import Error

import smtplib,ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#from datetime import date, timedelta
import time
print("\n\n\n\n")
print("you're about to see the status of your webservices")
#get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#get cureent date
CurrentDate=datetime.date.today()  
days = datetime.timedelta(30)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date) 
CurrentDate1=datetime.date.today()  
days1 = datetime.timedelta(0)

new_date1 = CurrentDate1 - days1
final_date1= new_date1.strftime('%Y-%m-%d')
print(final_date1)


path1='C:/python_work/record_rec/App/bank_code.csv'
with open(path1, 'r') as file_object:
    lines=file_object.read()
        #print(lines)
    banks=lines.split()
    print(banks)
    fieldnames=['BVN','first_name','Middle_name','Surname','DOB','Account','Bank']
    
    for bank in banks[:]:
        with open(f"C:/python_work/record_rec/icad_data{bank}.txt.csv", 'w', newline = '') as csvfile:
                
                my_writer = csv.writer(csvfile, delimiter = ',')
                my_writer.writerow(fieldnames)
        conn = msql.connect(host='127.0.0.1', database='housing_data', user='root', password='Magfum12@')

        # get cursor object
        cursor= conn.cursor()
        sql=f"SELECT BVN,upper(first_name),upper(Middle_name),upper(Surname),DOB,Account,Bank FROM housing_data.icad where Bank = '{bank}' order by bvn ;"

        # execute your query
        cursor.execute(sql)

        # fetch all the matching rows 
        result = cursor.fetchall()
        #print(result)
        
        with open(f"C:/python_work/record_rec/icad_data{bank}.txt.csv", 'a', newline = '') as csvfile:
                
                my_writer = csv.writer(csvfile, delimiter = ',')
               
                  
                
                
            # loop through the rows
                for row in result:
                    print(row)
                    #print("\n")
                    my_writer.writerow(row)
    cursor.close() 

    # with open(path1, 'r') as file_object:
    #     lines=file_object.read()
    #         #print(lines)
    #     banks=lines.split()
    #     print(banks)
BVN_fieldnames=['BVN','first_name','Middle_name','Surname','DOB']
        
        # for bank in banks[:]:
with open(f"C:/python_work/record_rec/bvn_data.txt.csv", 'w', newline = '') as csvfile:
        
        my_writer = csv.writer(csvfile, delimiter = ',')
        my_writer.writerow(BVN_fieldnames)
conn = msql.connect(host='127.0.0.1', database='housing_data', user='root', password='Magfum12@')

# get cursor object
cursor= conn.cursor()
sql=f"SELECT BVN,upper(first_name),upper(Middle_name),upper(Surname),DOB FROM housing_data.bvn_2 order by bvn ;"

# execute your query
cursor.execute(sql)

# fetch all the matching rows 
result = cursor.fetchall()
#print(result)

with open(f"C:/python_work/record_rec/bvn_data.txt.csv", 'a', newline = '') as csvfile:
        
        my_writer = csv.writer(csvfile, delimiter = ',')
    
        
        
        
    # loop through the rows
        for row in result:
            print(row)
            #print("\n")
            my_writer.writerow(row)
cursor.close() 
import breading
import comparism


