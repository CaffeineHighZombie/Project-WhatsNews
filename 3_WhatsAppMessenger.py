#!usr/bin/env python3

from selenium import webdriver

driver = webdriver.Chrome("/home/chz/Project/Project-WhatsNews/chromedriver")
driver.implicitly_wait(5)

driver.get("https://web.whatsapp.com/")
