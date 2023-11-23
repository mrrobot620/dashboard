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
import logging


logging.basicConfig(format='%(asctime)s %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p' )

op = webdriver.ChromeOptions()
op.add_argument("user-data-dir=/home/administrator/.config/google-chrome/Default")
op.add_argument('--headless=new')
prefs = {
    
    'profile.default_content_settings.popups': 0,
    'download.default_directory' : r"/home/administrator/data",
    'directory_upgrade': True
}
op.add_experimental_option('prefs' , prefs)
driver = webdriver.Chrome(options=op)
driver.get("https://script.google.com/a/macros/flipkart.com/s/AKfycbyJxFzir-KQrETK_3Cr0Cs9Uat7JL3xMJmBCidYqURSApGy0_HOfMQpF39nWk-qT2pehA/exec?action=download")
time.sleep(15)
logging.warning("Downloaded: Evening OB Report")
driver.close()