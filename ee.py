from selenium import webdriver
import os 
from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC3
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import os
from idna import valid_contextj
from datetime import datetime, timedelta


op = webdriver.ChromeOptions()
# op.add_argument('headless')
# op.add_argument('--window-size=1920,1080')
prefs = {
    'profile.default_content_settings.popups': 0,
    'download.default_directory' : r"C:\Users\abhishek.h1\Downloads\ee_data",
    'directory_upgrade': True
}
op.add_experimental_option('prefs' , prefs)
driver = webdriver.Chrome(options=op)
driver.get("https://eagleeye.portalonewifi.com/login")
time.sleep(5)
print(driver.title)

current_time = time.localtime()
current_datetime = datetime(*current_time[:6])
new_datetime = current_datetime - timedelta(minutes=5)

realtime = current_datetime.strftime("%H:%M")
date = new_datetime.strftime("%Y-%m-%d")
delayed_time = new_datetime.strftime("%H:%M")


print(date)
print(realtime)
print(delayed_time)
driver.maximize_window()


def login():
    username = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/input")
    username.send_keys("162575")
    password = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/input")
    password.send_keys("123456")
    sign_in = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/button")
    sign_in.click()
    return True

def date_time():
    from_date = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/input[2]")
    from_date.clear()
    from_date.send_keys(date)
    to_date = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/input[2]")
    to_date.clear()
    to_date.send_keys(date)
    time.sleep
    d_time = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/input[2]")
    time.sleep(1)
    d_time.clear()
    time.sleep(1)
    d_time.send_keys(delayed_time)
    time.sleep(1)
    r_time = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/input[2]")
    r_time.clear()
    time.sleep(1)
    r_time.send_keys(realtime)

def filter():
    facility = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/button")
    facility.click()
    time.sleep(2)
    type_facility =driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input")
    time.sleep(2)
    type_facility.send_keys("MotherHub" )
    time.sleep(1)
    type_facility.send_keys("_YKB")
    print("Selected YKB")
    time.sleep(3)
    click_facility = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/a[1]")
    click_facility.click()
    time.sleep(5)

    filter_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/button")
    driver.execute_script("arguments[0].scrollIntoView(true);", filter_button)
    time.sleep(1)
    ActionChains(driver).move_to_element(filter_button).click(filter_button).perform()
    print("Filtered Data")
    
    time.sleep(1)
    download_button = driver.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div[1]/div/button[2]")
    driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
    time.sleep(3)
    ActionChains(driver).move_to_element(download_button).click(download_button).perform()
    print("Clicked on Download Button")

    
login()
time.sleep(5)
date_time()
filter()
time.sleep(10)
driver.quit()
print("File got Downloaded")
