# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 19:58:49 2025

@author: kanmani
"""
import json
import urllib.request
import yfinance as yf
import pandas as pd
apple = yf.Ticker("AAPL")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
output_file = "apple.json"

urllib.request.urlretrieve(url, output_file)
print(f"Downloaded {output_file} successfully!")

with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info

apple_info['country']
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")
apple.dividends.plot()
