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
driver.get("https://m.facebook.com/story.php?story_fbid=259962408652452&id=100039160840291")
#wait=WebDriverWait(driver, 600)
#elem=browser.find_element_by_link_text('Photos')
#elem.click()
driver.implicitly_wait(5)
search=driver.find_element_by_class_name('_54k8 _56bs _4n43 _6gg6 _901w _56bu _52jh').click()
#elem = driver.find_element_by_class_name('foo').click()
search.send_keys('7596985078')
driver.implicitly_wait(5)
search=driver.find_element_by_id('pass')
search.send_keys('chattingrdbot')

#elem=browser.find_element_by_link_text('Log In')
#elem.click()
driver.implicitly_wait(5)
search=driver.find_element_by_id('loginbutton')
search.click()
target =' "Tathagata Dey" '
string1 = "I am ready with my bot."

#x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))    
target.click()
input_box=driver.find_element_by_class_name('_30yy _7oam')
for i in range(10):
    input_box.send_keys(string1+Keys.ENTER)