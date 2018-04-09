#!/usr/bin/env python
from __future__ import print_function

import pymysql



conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='bank')

cur = conn.cursor()
sno=1
i=2

cur.execute("SELECT * FROM table2")
rows = cur.fetchall()
for row in rows:
   r=0.0
   if ((row[4]!= 0)&(row[5]!= 0)):
       a= (row[6]+row[7]) if((row[6]+row[7])>0) else 1
       b= (row[2]+row[3]) if((row[2]+row[3])>0) else 1
       r=(((0.35)*(row[4]/(row[4]+row[5])))+((0.30)*(row[2]/b))+((0.20)*(row[6]/(a))+((0.15)*(row[8])))*100
   elif ((row[2]!= 0)&(row[3]!= 0)&(row[6]== 0)):
        b= (row[2]+row[3]) if((row[2]+row[3])>0) else 1
        r=(((0.65)*(row[2]/b))+((0.35)*(row[8])))*100   
   elif ((row[6]!= 0)&(row[7]!= 0)&(row[2]== 0)):
         b= (row[6]+row[7]) if((row[6]+row[7])>0) else 1
         r=(((0.75)*(row[6]/b))+((0.25)*(row[8])))*100
   else:
       r= 50;
   query2 ="UPDATE table2 SET Points='%d' WHERE sno='%d'"% (r,sno)
   cur.execute(query2)
   sno+=1
  
    
cur.close()
conn.close()







