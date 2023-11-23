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
    db='grafana',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


folder = r"/home/administrator/data"
file = "tracking_logs.csv"
primary = "YKB-Station-Wise-ABHI.csv"
secondary = "ykb_secondary_station_wise_abhi.csv"

interval = 2

def truncate_table(table_name):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE {table_name}")
            conn.commit()
            print(f"Table '{table_name}' truncated")
    except Exception as e:
        print(f"Error truncating the table: {e}")



while True:
    file_path  = os.path.join(folder , file)
    if os.path.exists(file_path):
        print("File Found")
        if os.path.getsize(file_path) == 0:
            os.remove(file_path)
            print("Empty EE file Deleted")
            continue
        try:
            df = pd.read_csv(file_path, dtype=str)
            df.fillna('N/A', inplace=True)
            with conn.cursor() as cursor:
                for index, row in df.iterrows():
                    Department = row['Department']
                    Casper = "ca."+ row['Casper ID']
                    Shipment = row['Shipment/Bag ID']
                    Seal = row['Seal ID']
                    Device = row['Device #']
                    sql = "INSERT INTO ee (Department, Casper, Shipment, Seal, Device) VALUES (%s, %s, %s, %s, %s)"
                    sql1 = "INSERT INTO ee1 (Department , Casper , Shipment , Seal , Device) VALUES (%s , %s , %s , %s , %s)"
                    cursor.execute(sql, (Department, Casper, Shipment, Seal, Device))
                    cursor.execute(sql1 , (Department , Casper , Shipment , Seal , Device))
            conn.commit()
            os.remove(file_path)
        except:
            logging.warn("Reading Eagle Eye File Failed")

    primaryStation = os.path.join(folder, primary)
    if os.path.exists(primaryStation):
        if os.path.getsize(primaryStation) == 0:
            os.remove(primaryStation)
            print("Empty Primary File Deleted")
            continue
        try:
            truncate_table("fdp")
            print("Primary Station File Found")
            df1 = pd.read_csv(primaryStation)
            os.remove(primaryStation)
            with conn.cursor() as cursor:
                for index, row in df1.iterrows():
                    station = row['processing_station_current']
                    p_processing = row['tracking_id_ekart']
                    if station.startswith("ZO"):
                        zo_station = station
                        zo_p_processing = p_processing
                        print(f"ZO Processing: {zo_station} :  {zo_p_processing}" ) 
                        sql1 = "INSERT INTO fdp (Station , processing) VALUES (%s , %s)"
                        cursor.execute(sql1 , (zo_station , zo_p_processing))
                        conn.commit()
                    if station.startswith("PrimaryVDS"):
                        b5_station = station
                        b5_p_processing = p_processing
                        print(f'B5 Processing:  {b5_station} :  {b5_p_processing}')
                        sql2 = "INSERT INTO fdp (Station , processing) VALUES (%s , %s)"
                        cursor.execute(sql2 , (b5_station , b5_p_processing))
                        conn.commit()
        except:
            print("Reading Secondary File Failed")           

    secondaryStation = os.path.join(folder, secondary)
    if os.path.exists(secondaryStation):
        if os.path.getsize(secondaryStation) == 0:
            os.remove(secondaryStation)
            print("Empty Secondary File Deleted")
            continue
        try:
            print("Secondary Station File Found")
            df1 = pd.read_csv(secondaryStation)
            os.remove(secondaryStation)
            with conn.cursor() as cursor:
                for index, row in df1.iterrows():
                    s_station = row['processing_station_current']
                    s_processing = row['tracking_id_ekart']
                    if s_station.startswith("ZO"):
                        zo_s_station = s_station
                        zo_s_processing = s_processing
                        print(f"ZO Secondary Processing: {zo_s_station} :  {zo_s_processing}" ) 
                        sql1 = "INSERT INTO fdp (Station , processing) VALUES (%s , %s)"
                        cursor.execute(sql1 , (zo_s_station , zo_s_processing))
                        conn.commit()
                    if s_station.startswith("VStation"):
                        b5_s_station = s_station
                        b5_s_processing = s_processing
                        print(f'B5 Secondary Processing:  {b5_s_station} :  {b5_s_processing}')
                        sql2 = "INSERT INTO fdp (Station , processing) VALUES (%s , %s)"
                        cursor.execute(sql2 , (b5_s_station , b5_s_processing))
                        conn.commit()
                    if s_station.startswith('NZStation') or s_station.startswith('SZStation'):
                        cbs1_s_station = s_station
                        cbs1_s_processing = s_processing
                        sql3 = "INSERT INTO fdp (Station , processing) VALUES (%s ,%s)"
                        cursor.execute(sql3 , (cbs1_s_station , cbs1_s_processing))
        except:
            print("Reading Secondary File Failed")       
            


    print(f"File '{file}' not found. Retrying in {interval} seconds ....")
    time.sleep(interval)
