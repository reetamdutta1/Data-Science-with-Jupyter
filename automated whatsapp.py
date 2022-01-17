# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:37:32 2020

@author: REETAM
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("E:/ACADEMICS/SPYDER + JUPYTER/chromedriver")
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver, 600)
target =' "Swarnava Sinha" '
string1 = "Bokachoda Sisso !!!!."

x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))    
target.click()
input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(100):
    input_box.send_keys(string1+Keys.ENTER)
    
#search=driver.find_element_by_class_name('vW7d1 message-out')
#search=driver.find_element_by_link_text('https://youtu.be/sVDHOi3Nsok')
#search.click()
#target =' "Maa JIO" '
#string2 = "Are you ?"

#x_arg='//span[contains(@title, '+ target + ')]'
#target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))    
#target.click()
#input_box=driver.find_element_by_class_name('_1Plpp')

#for i in range(10):
#    input_box.send_keys(string2+Keys.ENTER)

#target =' "Maa JIO" '    
#string3 = "If not then be ready !"

#x_arg='//span[contains(@title, '+ target + ')]'
#target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))    
#target.click()
#input_box=driver.find_element_by_class_name('_1Plpp')

#f#or i in range(10):
#    input_box.send_keys(string3+Keys.ENTER)