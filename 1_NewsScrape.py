#!/bin/env python3

import json
import requests
from bs4 import BeautifulSoup
from rbmq_client import rbmq_module

class NewsScrape:
	def __init__(self):
		self.rbmq_module = rbmq_module()

	def scrape_data(self):
		webpage=requests.get("http://www.thehindu.com/")
		print(webpage.status_code)
		soup=BeautifulSoup(webpage.content,"lxml")
		samples=soup.find_all("a",href=True)
		for link in samples:
			try:
				text = link.text.strip()
				if text:
					data = {}
					data["headlines"] = text
					self.rbmq_module.publish(json.dumps(data))
			except KeyboardInterrupt:
				break			

if __name__ == '__main__':
	newsScrape = NewsScrape()
	newsScrape.scrape_data()
