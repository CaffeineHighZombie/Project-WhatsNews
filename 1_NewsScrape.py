#!/bin/env python3

import requests
from bs4 import BeautifulSoup

webpage=requests.get("http://www.thehindu.com/")
print(webpage.status_code)
soup=BeautifulSoup(webpage.content,"lxml")
samples=soup.find_all('a')
print(samples[0])