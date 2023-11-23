import os 
import pandas as pd
import time
import subprocess
import pymysql
import time
from datetime import datetime
import logging


conn = pymysql.connect(
    host='localhost',
    user='abhishek',
    password='abhi',
    db='ob-ib',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


folder = r"/home/administrator/data"
file = "evening_ob.csv"

df = pd.read_csv('/home/administrator/data/evening_ob.csv' , dtype=str)
df.fillna('N/A', inplace=True)

try:
   for index , row in df.iterrows():
    DOCK = row["DOCK"]
    TRIP = row[" TRIP ID"]
    VEHICLE = row["VEHICLE NO"]
    DESTINATION = row["Destination"]
    STATUS = row["Status"]
    CONNECTION_TYPE = row[" Connection type"]
    AGEING = row["Ageing"]
    LH1 = row["Unnamed: 10"]
    LH2 = row[" LH REMARK"]
    DOCKIN = row["DOCK IN TIME"]
    DOCKOUT = row["DOCK OUT TIME"]
    GV = row["Grid Visibility"]
    BAGS = row["Bags"]
    SL = row["SL"]
    realAgeing = row['Real Ageing']
    with conn.cursor() as cursor:
        sql = "INSERT INTO evening(DOCK , TRIP , VEHICLE , DESTINATION , STATUS , CONNECTIONTYPE , AGEING , LH1 , LH2 , DOCKIN , DOCKOUT , GV , BAGS , SL , realAgeing) VALUES (%s ,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s )"
        cursor.execute(sql , (DOCK , TRIP , VEHICLE , DESTINATION , STATUS , CONNECTION_TYPE , AGEING , LH1 , LH2 ,  DOCKIN , DOCKOUT, GV , BAGS , SL , realAgeing ) )
    conn.commit()
except Exception as e:
    logging.warning(f"Unable to update the OB File to MySQL   \n Error:  {e}")
    
    
