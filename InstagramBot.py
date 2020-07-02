# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:07:22 2020

@author: Stuart
"""

from time import sleep
from selenium import webdriver

firefoxdriverpath = 'geckodriver.exe'
browser = webdriver.Firefox()

browser.get('https://www.instagram.com/')

sleep(5)

browser.close()