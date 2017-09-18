#!usr/bin/env python3

from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_condition
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome("/home/chz/Project/Project-WhatsNews/chromedriver")

web.get("https://web.whatsapp.com/")
input('Wait for sometime before pressing enter')

elem = web.find_element_by_xpath('//span[contains(text(),"Sanjana Iyyappan")]')
elem.click()
elem1 = web.find_elements_by_class_name('input')
elem1[0].send_keys(time.strftime('%m-%d-%y_%H-%M-%S'))
elem1[0].send_keys('\n')

# web.find_element_by_class_name('send-container').click()



# wait = WebDriverWait(driver, 600)

# target = '"Sanjana Iyyappan"'

# msg = time.strftime('%m-%d-%y_%H-%M-%S')

# x_arg = '//span[contains(@title,' + target + ')]'
# group_title = wait.until(EC.presence_of_element_located((
#     By.XPATH, x_arg)))
# group_title.click()
# inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
# input_box = wait.until(EC.presence_of_element_located((
#     By.XPATH, inp_xpath)))
# for i in range(100):
#     input_box.send_keys(string + Keys.ENTER)
#     time.sleep(1)

    