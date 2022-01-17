# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:20:55 2020

@author: REETAM
"""


from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://gmail.com")

driver.find_element_by_id("identifierId").send_keys('rinagdutta1')
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys('196319731999')
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

driver.get("https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")
driver.find_element_by_xpath('//button[normalize-space()="Sign out"]').click()
driver.close()