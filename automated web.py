# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver 
browser = webdriver.Chrome("E:/ACADEMICS/SPYDER + JUPYTER/chromedriver")
browser.get("https://www.facebook.com/reetam.dutta.12")
#elem=browser.find_element_by_link_text('Photos')
#elem.click()
browser.implicitly_wait(5)
search=browser.find_element_by_id('email')
search.send_keys('9432254787')
browser.implicitly_wait(5)
search=browser.find_element_by_id('pass')
search.send_keys('7874522349')

#elem=browser.find_element_by_link_text('Log In')
#elem.click()
browser.implicitly_wait(5)
search=browser.find_element_by_id('loginbutton')
search.click()
search=browser.find_element_by_link_text('Create post')
search.click()
browser.implicitly_wait(5)
search=browser.find_element_by_id('js_5')
search.click()