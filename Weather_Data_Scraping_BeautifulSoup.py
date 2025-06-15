# -*- coding: utf-8 -*-
"""
Created on Fri May 30 09:57:08 2025

@author: kanmani
"""

from bs4 import BeautifulSoup
import requests

URL = "https://www.timeanddate.com/weather/canada/halifax"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

print(soup.title.string)

#Extract the temprature
temperature = soup.find("div", class_="h2").get_text(strip=True)

# Extract the weather description
description = soup.find("p").get_text(strip=True)

print(f"Current Temperature in Halifax: {temperature}")
print(f"Condition: {description}")