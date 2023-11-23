import subprocess
import schedule
import time
import threading
import pymysql
import logging

logging.basicConfig(format='%(asctime)s %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p' )

downloader = r'C:\Users\abhishek.h1\Downloads\ee_data\data_downloader.py'
fdp_downloader = 'fdp.py'
evening_ob = 'csv_to_ob_sql.py'


conn = pymysql.connect(
    host='localhost',
    user='abhishek',
    password='abhi',
    db='grafana',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


def truncate_table(table_name):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE {table_name}")
            conn.commit()
            print(f"Table '{table_name}' truncated")
    except Exception as e:
        print(f"Error truncating the table: {e}")


def run_downloader():
    try:
        subprocess.run(["python3" , downloader])
        print("Sucessfully Start Data Downloader")
    except Exception as e:
        print(f"Error running data downloader.py:  {e}")

def run_fdp_downloader():
    try:
        subprocess.run(['python3' , fdp_downloader])
        print("Sucessfully Executed FDP Downloader")
    except Exception as e:
        print("Error in running fdp downloader")


def run_ob_evening():
    try:
        subprocess.run('python3' , evening_ob)
        logging.warning("Sucess: OB Evening")
    except:
        logging.warning("Failed: OB Evening")
        


schedule.every(4).minutes.do(run_fdp_downloader)
# schedule.every(10).minutes.do(run_ob_evening)

# schedule.every(2).minutes.do(run_downloader)
# schedule.every().hour.at(":00").do(truncate_table , "ee")
# schedule.every().day.at("06:30").do(truncate_table, "ee1")
# schedule.every().day.at("15:30").do(truncate_table, "ee1")
# schedule.every().day.at("22:00").do(truncate_table, "ee1")

# run_downloader()
run_fdp_downloader()
# run_ob_evening()

while True:
    schedule.run_pending()
