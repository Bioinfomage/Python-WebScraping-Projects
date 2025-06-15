# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 20:26:34 2025

@author: kanmani
"""

import json
import urllib.request
import yfinance as yf
import pandas as pd
amd = yf.Ticker("AMD")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
output_file = "amd.json"

urllib.request.urlretrieve(url, output_file)
print(f"Downloaded {output_file} successfully!")

with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(amd_info))
amd_info

amd_info['country']
amd_info['sector']
amd_data = amd.history(period="max")
amd_data.reset_index(inplace=True)
print(amd_data.iloc[0]["Volume"])
print(amd_info['country'], amd_info['sector'])