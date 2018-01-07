#!usr/bin/env python3

from selenium import webdriver
import time
import json
from rbmq_client import rbmq_module
from bs4 import BeautifulSoup

class WhatsappMessenger:

	def __init__(self):
		self.rbmq_module = rbmq_module()
		self.web = webdriver.Chrome("/home/sanjana/Project-WhatsNews/chromedriver")
		self.web.get("https://web.whatsapp.com/")
		input("press enter")

	def get_message(self, contact):
		message = {}
		message = self.rbmq_module.subscribe()
		if message:
			self.send(contact, message)

	def send(self,contact, message):
		message = json.loads(message.decode())
		self.web.find_element_by_xpath('//span[@title="Jithu"]').click()
		input_elem = self.web.find_elements_by_class_name('input-container')
		input_elem[0].send_keys(message["headlines"])
		input_elem[0].send_keys('\n')

if __name__ == '__main__':
	what_mes = WhatsappMessenger()
	while(1):
		what_mes.get_message("Jithu")
