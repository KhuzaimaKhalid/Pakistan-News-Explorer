# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 23:06:07 2025

@author: Administrator
"""

import requests
import json

print("============================  NEWS APP  =======================================")
GNEWS_API_KEY = "ad7fcb63e0242aadaf1920e26a67441a"  

query = input("What type of news do you want: ")
print("****************************************************************************")

url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=pk&max=10&apikey={GNEWS_API_KEY}"

response = requests.get(url)
news = json.loads(response.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("===========================================================================================")