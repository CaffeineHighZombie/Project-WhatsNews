#!/bin/env python3

import requests
from bs4 import BeautifulSoup

webpage=requests.get("http://www.thehindu.com/")
print(webpage.status_code)
soup=BeautifulSoup(webpage.content,"lxml")
samples=soup.find_all("a",href=True)

data={}
for link in samples:
	try:
		soup=BeautifulSoup(requests.get(link['href']).content,"lxml")
		if soup.find("p",{"class":"s4-3x100-text s4x-100-ls-text hidden-xs hidden-sm hidden-md"}).text==None:
			continue
		data["headlines"]=soup.find("div",{"class":"intro"}).text
		data["description"]=soup.find("p",{"class":"s4-3x100-text s4x-100-ls-text hidden-xs hidden-sm hidden-md"}).text
		print (data)
	except KeyboardInterrupt:
		break
	except Exception:
		continue